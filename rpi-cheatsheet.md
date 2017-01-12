### mount sshfs

commande pour monter un rpi en ssh, sur le dossier home/pi

	sudo sshfs -o allow_other,defer_permissions pi@192.168.2.32:/home/pi raspberrypi/pi
	
remplacer l'IP par celle du RaspberryPi	

### trouver l’ip du `raspberry pi` via `nmap`

Le Pi est connecté en direct à l’USB via la commande, sur l’adaptateur USB/RJ45 de mon macbookPro :

	nmap -sn 192.168.2.0/24
	
Cette commande sert à scanner les ip sur une plage d’adresse. Il faut installer nmap, car non présent par défaut. 

### MAC addresses

Pi B+

	wlan0 : 00:c1:40:59:0e:59 
	eth0 : b8:27:eb:b4:d2:4b

Pi 2

	eth0 : b8:27:eb:7f:52:0b


### faire une photo de test, via `raspistill`

	raspistill -o cam-test-$(date +%Y-%m-%d_%H-%m-%S).jpg