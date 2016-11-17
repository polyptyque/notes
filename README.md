# notes
notes du projet polyptyque

petits morceaux à copier coller…

### mount sshfs

commande pour monter un rpi en ssh, sur le dossier home/pi

	sudo sshfs -o allow_other,defer_permissions pi@192.168.2.36:/home/pi pi
	
remplacer l'IP par celle du RaspberryPi	