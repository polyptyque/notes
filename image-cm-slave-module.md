# préparation de l’image du CM slave-module

### modification de l’image

afin d’avoir une image personnalisée prête à l’emploi
il faut modifier l’image téléchargée sur le site [raspberrypi.org](https://www.raspberrypi.org/downloads/raspbian/) 

pour avoir l'*offset* des partitions en bytes
en une ligne :
	parted 2017-04-10-raspbian-jessie-lite.img unit B print

interactivement :
	parted rasbian-image.img

le terminal affiche une saisie, taper `unit` puis `B` puis `print` 

récupérer la valeur dans la colonne `start` de la partition qu'on veut monter. à partir de cette valeur, taper la commande suivante pour monter l'image dans un `dossier-cible`, avec la commande suivante

	sudo mount -o loop,offset=valeuroffset raspian-image.img dossier-cible

on peut maintenant modifier l'image, ça s'enregistre. 

### configuration réseau

modifier le fichier `/etc/wpa_supplicant/wpa_supplicant.conf`
et rajouter les lignes suivantes. Il est possible d’ajouter plusieurs fichier

	network={
		ssid="F93"
		psk="**********"
		id_str="F93"
		priority=1
	}

### ajouter SSH au démarrage

active le lancement de SSH au démarrage

	sudo update-rc.d ssh enable 5
	
### mise à jour apt-get

	sudo apt-get update

### installation des paquets

Les paquets suivant sont à installer, pour que l’application tourne

	sudo apt-get install python3 python3-pip 
	
Les paquets suivant sont confortable pour du debug

	sudo apt-get install vim git screen vim
	
mise à jour des librairies/dépendances de l’app pour python3

	pip3 picamera requests configparser

### Exemple de modification d'une image avant déploiement sur les modules

On peut modifier les fichier directement après montage, mais pour ajouter des programmes, par exemple, on peut utiliser `chroot` pour être dans le système de fichiers comme s'il était démarré, ou presque.

	mkdir sda2
	parted 2017-04-10-raspbian-jessie-lite.img unit B print
	sudo mount -o offset=47185920,loop 2017-04-10-raspbian-jessie-lite.img sda2
	sudo mount -o offset=4194304,loop 2017-04-10-raspbian-jessie-lite.img sda2/boot
	chroot sda2
	mount  /proc
	apt-get update
	apt-get dist-upgrade
	apt-get install screen vim git python3 python3-pip
	pip3 picamera requests configparser
	sudo update-rc.d ssh enable 5

### Étendre l'image disque

Ajouter 200Mo de zéros à l'image disque :

	dd if=/dev/zero bs=200M count=1 >> 2017-04-10-raspbian-jessie-lite.img

Étendre la partition 2 de 200Mo :

	pas fini !

### Monter l’image pour vérifier/corriger les partitions

on repère l’offset de la partition avec la commande `fdisk`, puis on insert cette valeur en option `-o`.

	sudo losetup -o 47185920 /dev/loop0 2017-04-10-raspbian-jessie-lite.slave-module.img

ensuite on peut la checker et la réparer automatiquement, avec

	sudo e2fsck -f /dev/loop0
	
## Transférer l’image vers le CM

il faut évidement [installer](https://github.com/raspberrypi/usbboot) et utiliser `rpiboot` pour monter le eMMC du CM sur `/dev/sda`.  

Il faut vérifier que c’est bien `/dev/sda`, car parfois c’est `/dev/sdb`. Utiliser la commande `sudo fdisk -l`

	sudo dd bs=4MiB if=2017-04-10-raspbian-jessie-lite.slave-module.img of=/dev/sda	