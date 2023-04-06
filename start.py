import cv2
import imutils
import argparse
import threading
import datetime
import time
import os
import subprocess
import netifaces as ni
import RPi.GPIO as GPIO

from flask import Flask, render_template, Response
from imutils.video import VideoStream

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()
# initialize a flask object
app = Flask(__name__)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/training_data.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

motorA1 = 27
motorA2 = 22
motorB1 = 23
motorB2 = 24
motorC1 = 25
motorC2 = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorA1, GPIO.OUT)
GPIO.setup(motorA2, GPIO.OUT)
GPIO.setup(motorB1, GPIO.OUT)
GPIO.setup(motorB2, GPIO.OUT)
GPIO.setup(motorC1, GPIO.OUT)
GPIO.setup(motorC2, GPIO.OUT)

ni.ifaddresses("wlan0")
# ni.ifaddresses('{AAE133D9-DAD5-481C-8E22-0E07102471C0}') #wifi
ip = ni.ifaddresses("wlan0")[ni.AF_INET][0]["addr"]

vs = VideoStream(src=0).start()
time.sleep(2.0)


@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html")


def detect_motion(frameCount):
    # grab global references to the video stream, output frame, and
    # lock variables
    global vs, outputFrame, lock
    # initialize the total number of frames
    total = 0

    # loop over frames from the video stream
    while True:
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale, and blur it
        frame = vs.read()
        frame = imutils.resize(frame, width=700)  # width= 400
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        # grab the current timestamp and draw it on the frame
        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%d %b %Y (%H:%M:%S)"), (1, frame.shape[0] - 1),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        # update (10, frame.shape[0] - 10 ))

        # continue to process the frame
        if total > frameCount:
            # detect motion in the image
            face = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in face:
                # cv2.imshow("countours", image)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                id, conf = recognizer.predict(gray[y:y+h, x:x+w])

                # if(conf < 60):
                if (id == 1):
                    id = "Praktikan_1"
                if (id == 2):
                    id = "Praktikan_2"
                else:
                    id = "UNKNOWN"
                # Put text describe who is in the picture
                # cv2.rectangle(frame, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
                cv2.putText(frame, str(id), (x+5, y-5),
                            font, 2.0, (0, 255, 0), 2)

        total += 1
        with lock:
            outputFrame = frame.copy()


def generate():
    # grab global references to the output frame and lock variables
    global outputFrame, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route('/maju')
def maju():

    GPIO.output(motorA1, GPIO.HIGH)
    GPIO.output(motorA2, GPIO.LOW)
    GPIO.output(motorB1, GPIO.HIGH)
    GPIO.output(motorB2, GPIO.LOW)
    GPIO.output(motorC1, GPIO.LOW)
    GPIO.output(motorC2, GPIO.LOW)

    return render_template('index.html', ip=ip)


@app.route('/mundur')
def mundur():

    GPIO.output(motorA1, GPIO.LOW)
    GPIO.output(motorA2, GPIO.HIGH)
    GPIO.output(motorB1, GPIO.LOW)
    GPIO.output(motorB2, GPIO.HIGH)
    GPIO.output(motorC1, GPIO.LOW)
    GPIO.output(motorC2, GPIO.LOW)

    return render_template('index.html', ip=ip)


@app.route('/kanan')
def kanan():

    GPIO.output(motorA1, GPIO.LOW)
    GPIO.output(motorA2, GPIO.LOW)
    GPIO.output(motorB1, GPIO.HIGH)
    GPIO.output(motorB2, GPIO.LOW)
    GPIO.output(motorC1, GPIO.LOW)
    GPIO.output(motorC2, GPIO.LOW)

    return render_template('index.html', ip=ip)


@app.route('/kiri')
def kiri():

    GPIO.output(motorA1, GPIO.HIGH)
    GPIO.output(motorA2, GPIO.LOW)
    GPIO.output(motorB1, GPIO.LOW)
    GPIO.output(motorB2, GPIO.LOW)
    GPIO.output(motorC1, GPIO.LOW)
    GPIO.output(motorC2, GPIO.LOW)

    return render_template('index.html', ip=ip)


@app.route('/berhenti')
def berhenti():
    GPIO.output(motorA1, GPIO.LOW)
    GPIO.output(motorA2, GPIO.LOW)
    GPIO.output(motorB1, GPIO.LOW)
    GPIO.output(motorB2, GPIO.LOW)
    GPIO.output(motorC1, GPIO.LOW)
    GPIO.output(motorC2, GPIO.LOW)
    return render_template('index.html', ip=ip)


@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


# check to see if this is the main thread of execution
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--ip", type=str, required=True,
    # 	help="ip address of the device")
    # ap.add_argument("-o", "--port", type=int, required=True,
    # 	help="ephemeral port number of the server (1024 to 65535)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
                    help="# of frames used to construct the background model")
    args = vars(ap.parse_args())

    # start a thread that will perform motion detection
    t = threading.Thread(target=detect_motion, args=(
        args["frame_count"],))
    t.daemon = True
    t.start()
    # start the flask app
    # app.run(host=args["ip"], port=args["port"], debug=True, threaded=True, use_reloader=False)
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True) #debug true is added by fauzi
# release the video stream pointer
vs.stop()
