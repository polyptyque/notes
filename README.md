# notes
notes du projet polyptyque

petits morceaux à copier coller…

### mount sshfs

commande pour monter un rpi en ssh, sur le dossier home/pi

	sudo sshfs -o allow_other,defer_permissions pi@192.168.2.32:/home/pi raspberry/pi
	
remplacer l'IP par celle du RaspberryPi	

### trouver l’ip du `raspberry pi` via `nmap`

Le Pi est connecté en direct à l’USB via la commande, sur l’adaptateur USB/RJ45 de mon macbookPro :

	nmap -sn 192.168.2.0/24
	
Cette commande sert à scanner les ip sur une plage d’adresse. Il faut installer nmap, car non présent par défaut. 

### faire une photo de test, via `raspistill`

	raspistill -o cam-test-$(date +%Y-%m-%d_%H-%m-%S).jpg
	
### synchronisation !

à + ou - 500 ms c’est pas encore ça

`img-2016-11-24_13-51-36_A.jpg` :
![img-2016-11-24_13-51-36_A.jpg](img-2016-11-24_13-51-36_A.jpg)

`img-2016-11-24_13-51-36_B.jpg` :	
![img-2016-11-24_13-51-36_B.jpg](img-2016-11-24_13-51-36_B.jpg)

### montage du 24 novembre

avec les [scripts pythons](python) 

![montage-2016-11-24.jpg](montage-2016-11-24.jpg)