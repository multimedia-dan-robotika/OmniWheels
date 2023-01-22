
<h1 align="center"> Lab Robotika dan Multimedia Universitas Gunadarma</h1>

<h2 align="center" id="title">OmniWheels Documentation</h2>

<p align="center"><img src="https://github.com/fauziallagan/OmniWheels/blob/master/Omniwheel%20Schematic.jpeg" alt="project-image"></p>

<p id="description">Sebuah Robot ber roda 3 yang dapat dikendalikan melalui web browser dan dibekali kecerdasan buatan yang mampu mendeteksi manusia menggunakan kamera.</p>

  
  
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

<p>6. Bila menemukan error seperti Library Tidak terinstal. Maka lakukan instalasi library yang digunakan seperti contoh dibawah : </p>


``` bash
sudo pip3 install imutils
```

<p>7. kalian akan melihat IP address ketika tidak terjadi error saat program `start.py` dijalankan seperti contoh dibawah : </p>

``` http
http://0.0.0.0:5000
```

<p>8. buka Web browser. Pastikan laptop/device kalian terhubung ke jaringan internet yang sama dengan jaringan internet yang ada di raspberry. lalu cari ip address tersebut dengan cara membuka terminal lalu ketikkan seperti dibawah ini :</p>

``` bash
ifconfig
```

<p>9. bila sudah terlihat IP address silahkan kalian copy IP tersebut dan kalian pasti di web browser kalian. jangan lupa tambahkan `:5000` diakhir IP addres. Seperti pada contoh Dibawah :</p>

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
            <span><strong>Flask Framework</strong></span><br>
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
            <span><strong>CSS</strong></span><br>
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

> Note: Kunjungi link tersebut bila terjadi error

