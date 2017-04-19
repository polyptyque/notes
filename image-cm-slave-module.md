# préparation de l’image du CM slave-module

### modification de l’image

afin d’avoir une image personnalisée prête à l’emploi
il faut modifier l’image téléchargée sur le site [raspberrypi.org](https://www.raspberrypi.org/downloads/raspbian/) 

pour avoir l'*offset* des partitions en bytes

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