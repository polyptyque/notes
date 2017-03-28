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

	raspistill -o cam-test-$(date +%Y-%m-%d_%H-%m-%S).jpg -cs 0
	
	
### monter la particition de boot (depuis mon PI B+)

Je n'ai pas réussi à faire fonctionner l'utilitaire rpiboot sur mon osx. Du coup, je l’ai fait depuis mon PI B+.
j'ai cloné [usbboot depuis le dépôt github officiel](https://github.com/raspberrypi/usbboot) dans le dossier `~/cm/usbboot/`.
Pour démarrer accéder à la partition de boot, il faut :

- débrancher le CMIO
- mettre le CMIO en mode `SLAVE ENABLE` (sur le CMIO, c’est le cavalier `J15`) 
- connecter depuis le port USB slave du CMIO vers l'USB du rPi B+
- lancer la commande depuis le rPi B+ :

````
sudo ./rpiboot
> Waiting for BCM2835 ...	
````
- ensuite brancher le CMIO, quelque chose comme ça apparaît dans le terminal :

````
Found serial number 0
Found serial = 0: writing file ./usbbootcode.bin
Successful read 4 bytes 
Waiting for BCM2835 ...
Initialised device correctly
Found serial number 1
Found serial = 1: writing file ./msd.elf
Successful read 4 bytes 
````
- ensuite il faut monter la partion de boot `/dev/sda1` sur un dossier qu’on créé si il n'existe pas. Idem pour la partition principale `/dev/sda2` si besoin.

````
cd ~/cm/
mkdir sda1
sudo mount /dev/sda1 ./sda1
mkdir sda2
sudo mount /dev/sda2 ./sda2
````
- on peut alors explorer la partition de boot

````
cd ~/cm/sda1
````

### configurer le boot et le device tree pour `dt-blob-dualcam.bin`

afin de modifier la configuration des pins, il faut recompiler le device tree via `Device Tree Compiler` et donc l’installer :

	sudo apt-get install device-tree-compiler

ensuite on peut compiler un fichier .dts

	dtc -I dts -O dtb -o dt-blob.bin minimal-cm-dt-blob.dts

par exemple, avec le fichier `dt-blob-dualcam.dts` pour la stéréo

	dtc -I dts -O dtb -o dt-blob-dualcam.bin dt-blob-dualcam.dts
	
ou
	
	dtc -I dts -O dtb -o dt-blob-dualcam.dtb dt-blob-dualcam.dts


on modifie ensuite le fichier `config.txt` en ajoutant

	device_tree=dt-blob-dualcam.bin


