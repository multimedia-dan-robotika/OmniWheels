
<h1 align="center"> Lab Robotika dan Multimedia Universitas Gunadarma</h1>

<h2 align="center" id="title">OmniWheels Documentation</h2>

<p align="center"><img src="https://github.com/fauziallagan/OmniWheels/blob/master/Omniwheel%20Schematic.jpeg" alt="project-image"></p>

<p align="center"><a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&width=435&lines=Sebuah+Robot+roda+3+yang+dapat+;dikendalikan+melalui+web+browser+;dan+dibekali+kecerdasan+buatan+;yang+mampu+mendeteksi+manusia+;menggunakan+kamera." alt="Typing SVG" /></a></p>
  
  
<h2>🧐 Features</h2>

*   Artificial Intelligen base on Object Detection
*   Web base Controller

<h2>🛠️ Installation Steps:</h2>

<p>1. Lakukan Update Pada Raspberry</p>

``` bash
sudo apt-get update
```

<p>2. Lakukan Upgrade pada Raspberry : (Optional)</p>

``` bash
sudo apt-get upgrade
```
<p>3. Clone Project OmniWheels : </p>

``` bash
git clone https://github.com/multimedia-dan-robotika/OmniWheels.git
```
<p>4. cari folder OmniWheels : </p>

``` bash
cd /OmniWheels
```

<p>5. Jalankan perintah berikut :</p>

``` python
python3 start.py
```

<p>6. kalian akan melihat IP address ketika tidak terjadi error saat program `start.py` dijalankan seperti contoh dibawah : </p>

``` http
http://0.0.0.0:5000
```

<p>7. buka Web browser. Pastikan laptop/device kalian terhubung ke jaringan internet yang sama dengan jaringan internet yang ada di raspberry. lalu cari ip address tersebut dengan cara membuka terminal lalu ketikkan seperti dibawah ini :</p>

``` bash
ifconfig
```

<p>8. bila sudah terlihat IP address silahkan kalian copy IP tersebut dan kalian pasti di web browser kalian. jangan lupa tambahkan `:5000` diakhir IP addres. Seperti pada contoh Dibawah :</p>

``` http
http://192.168.1.1:5000
```

<h2>🍰 Contribution Guidelines:</h2>

Bila Terjadi bug / Error pada Logika Program Kalian bisa berkontribusi dengan melakukan Commit dengan kode yang kalian kembangkan :)

  
  
<h2>💻 Built with</h2>

Technologies used in the project:
<table width="320px">
    <tbody>
        <tr valign="top">
            <td width="80px" align="center">
            <span><strong>Python</strong></span><br>
            <img height="32px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
            </td>
            <td width="80px" align="center">
            <span><strong>Javascript</strong></span><br>
            <img height="32" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg">
            </td>
            <td width="80px" align="center">
            <span><strong>HTML</strong></span><br>
            <img height="32" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg">
            </td>
            <td width="80px" align="center">
            <span><strong>CSS</strong></span><br>
            <img height="32px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg">
            </td>
      </tr>
      <tr valign="top">
            <td width="80px" align="center">
            <span><strong>Flask</strong></span><br>
            <img height="32px" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg">
            </td>
            <td width="80px" align="center">
            <span><strong>OpenCV</strong></span><br>
            <img height="32" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg">
            </td>   
            <td width="80px" align="center">
            <span><strong>Numpy</strong></span><br>
            <img height="32" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg">
            </td>  
            <td width="80px" align="center">
            <span><strong>Raspberry</strong></span><br>
            <img height="32px"src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/raspberrypi/raspberrypi-original.svg" >  
            </td>
      </tr>
    </tbody>
</table>
   
Library Used In the Project : 

| Library | Link |
| ------ | ------ |
| Flask | https://flask.palletsprojects.com/en/2.2.x/installation/|
| OpenCV | https://pypi.org/project/opencv-contrib-python/ |
| Imutils | https://pypi.org/project/imutils/ |
| Numpy | https://pypi.org/project/numpy/ |
| netifaces  | https://pypi.org/project/netifaces/|
|  threading  | https://pypi.org/project/threaded/|

> Note: Link diatas merupakan dokumetasi resmi. Silahkan dikunjungi untuk menambah wawasan.


<h2>🧐 Troubleshoot </h2>
<p>Jika Mengalami error seperti dibawah :  </p>

``` bash
Traceback (most recent call last):
  File "/home/pi/OmniWheels/start.py", line 1, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'
```

<p> Solusinya adalah kalian harus menginstall cv2 (OpenCV). berikut command untuk menginstall cv2 </p>
  
  ``` bash
sudo apt-get install python3-pip
```

<p>Jika Mengalami error seperti dibawah :  </p>

``` bash
Traceback (most recent call last):
  File "/home/pi/OmniWheels/start.py", line 2, in <module>
    import imutils
ModuleNotFoundError: No module named 'imutils'
```
<p> Solusinya adalah kalian harus menginstall imutils. berikut command untuk menginstall imutils </p>
  
  ``` bash
sudo pip3 install imutils
```
<p>Jika Mengalami error seperti dibawah :  </p>

``` bash
Traceback (most recent call last):
  File "/home/pi/OmniWheels/start.py", line 9, in <module>
    import netifaces as ni
ModuleNotFoundError: No module named 'netifaces'
```
<p> Solusinya adalah kalian harus menginstall netifaces. berikut command untuk menginstall netiface </p>
  
  ``` bash
sudo pip3 install netifaces
```

