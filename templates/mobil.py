import RPi.GPIO as GPIO
from flask import Flask, render_template
import subprocess
import netifaces as ni

app = Flask(__name__)
motorkiri1 = 27
motorkiri2 = 22
motorkanan1 = 23
motorkanan2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motorkiri1, GPIO.OUT)
GPIO.setup(motorkiri2, GPIO.OUT)
GPIO.setup(motorkanan1, GPIO.OUT)
GPIO.setup(motorkanan2, GPIO.OUT)

ni.ifaddresses("wlan0")
ip = ni.ifaddresses("wlan0")[ni.AF_INET][0]["addr"]


subprocess.Popen(["mjpg_streamer","-i", "input_uvc.so -r 620x380 -d /dev/video0 -f 10 -q 20","-o", "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"])

@app.route('/') 
def index():
	return render_template('mobil.html', ip=ip)

@app.route('/maju')
def maju():
	GPIO.output(motorkiri1, GPIO.HIGH)
	GPIO.output(motorkiri2, GPIO.LOW)
	GPIO.output(motorkanan1, GPIO.HIGH)
	GPIO.output(motorkanan2, GPIO.LOW)
	return render_template('mobil.html', ip=ip)

@app.route('/kanan')
def kiri():
	GPIO.output(motorkiri1, GPIO.LOW)
	GPIO.output(motorkiri2, GPIO.HIGH)
	GPIO.output(motorkanan1, GPIO.HIGH)
	GPIO.output(motorkanan2, GPIO.LOW)
	return render_template('mobil.html', ip=ip)

@app.route('/kiri')
def kanan():
	GPIO.output(motorkiri1, GPIO.HIGH)
	GPIO.output(motorkiri2, GPIO.LOW)
	GPIO.output(motorkanan1, GPIO.LOW)
	GPIO.output(motorkanan2, GPIO.HIGH)
	return render_template('mobil.html', ip=ip)

@app.route('/mundur')
def mundur():
	GPIO.output(motorkiri1, GPIO.LOW)
	GPIO.output(motorkiri2, GPIO.HIGH)
	GPIO.output(motorkanan1, GPIO.LOW)
	GPIO.output(motorkanan2, GPIO.HIGH)
	return render_template('mobil.html', ip=ip)

@app.route('/berhenti')
def berhenti():
	GPIO.output(motorkiri1, GPIO.LOW)
	GPIO.output(motorkiri2, GPIO.LOW)
	GPIO.output(motorkanan1, GPIO.LOW)
	GPIO.output(motorkanan2, GPIO.LOW)
	return render_template('mobil.html', ip=ip)

try:
	if __name__ == "__main__":
		app.run(debug=True, host="0.0.0.0")

except KeyboardInterrupt:
	print "exit"

finally:
	print "done"


