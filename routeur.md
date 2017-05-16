# Convertir le raspberry pi en routeur wifi

Ce guide est grandement inspiré de [cet article en anglais](http://raspberrypihq.com/how-to-turn-a-raspberry-pi-into-a-wifi-router/).  
Nous utilisons le `raspberry pi 3 model b` qui possède un wifi intégré sur l’interface `wlan0` et un wifi dongle sur l’interface `wlan1`.

## Configuration d'un raspberry Pi en tant que routeur réseau

	apt-get install isc-dhcp-server bind9

Le serveur DHCP va donner les adresses IP aux compute-modules qui n'en ont pas
Le serveur DNS (`bind9`) va associer un nom à une IP (en local uniquement)

### Interfaces réseaux

On configure 2 interfaces pour le wifi. La première pour le wifi intégré, qu’on laisse dans son fonctionnement par défaut, normalement, pas besoin de toucher, on doit avoir ça :

	allow-hotplug wlan0
	iface wlan0 inet manual
    	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

Pour modifier les enregistrements de réseaux connus, il suffit de modifier le fichier `/etc/wpa_supplicant/wpa_supplicant.conf` (se référer à la doc officielle RaspberryPi.)

La seconde interface est celle du routeur wifi, qu’on configure de manière `static` sur l’adresse IP `192.168.93.1`, ce qui donne ça :
    
	allow-hotplug wlan1
	iface wlan1 inet static
		address 192.168.93.1
		netmask 255.255.255.0

### DHCP

La configuration du DHCP se fait dans le fichier `/etc/dhcp/dhcpd.conf`. On l’édite : 

	sudo vim /etc/dhcp/dhcpd.conf

On ajoute les lignes suivantes pour constituer un sous-réseau, avec une plage d’adresses IP. Les plages IP que l’on a arbitrairement choisies pour DHCP vont de `192.168.93.10` à `192.168.93.50`. Le masque de sous-réseau est lui sur `192.168.93.*`.

	subnet 192.168.93.0 netmask 255.255.255.0 {
        range 192.168.93.10 192.168.93.50;
        option broadcast-address 192.168.93.255;
        option routers 192.168.93.1;
        default-lease-time 600;
        max-lease-time 7200;
        option domain-name "polyptyque";
        option domain-name-servers 8.8.8.8, 8.8.4.4;
	}

Les DNS `8.8.8.8` et `8.8.4.4` correspondent aux DNS de google.

Ensuite on modifie la configuration du serveur DHCP :

	sudo vim /etc/default/isc-dhcp-server

on ajoute simplement l’interface `wlan1` : 

	INTERFACES="wlan1"

### NAT (`Network Address Translation`)

j'ai appliqué le transfert d’adresses via NAT.

On active NAT 

Ouvrir `/etc/sysctl.conf` avec :

	sudo vim /etc/sysctl.conf

Ajouter à la fin

	net.ipv4.ip_forward=1

Puis lancer dans le terminal

	sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

redémarrer le réseau

	sudo ifdown wlan1
	sudo ifup wlan1

On va ensuite rediriger les requêtes d’une interface réseau vers un autre.

- de `eth0` vers `wlan1`, pour partager la connectivité ethernet. 
- ainsi que `wlan0` vers `wlan1`, pour partager la connectivité wifi.

avec les commandes suivantes pour `eth0` :

	sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
	sudo iptables -A FORWARD -i eth0 -o wlan1 -m state --state 	RELATED,ESTABLISHED -j ACCEPT
	sudo iptables -A FORWARD -i wlan1 -o eth0 -j ACCEPT

et pour le `wlan0` : 
	
	sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
	sudo iptables -A FORWARD -i wlan0 -o wlan1 -m state --state 	RELATED,ESTABLISHED -j ACCEPT
	sudo iptables -A FORWARD -i wlan1 -o wlan0 -j ACCEPT

pour sauvegarder cette configuration NAT : 

	sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
	
et rajouter à la fin de `/etc/network/interfaces` : 

	up iptables-restore < /etc/iptables.ipv4.nat
	
## Configuration du point d’accès, via `HostAPD`

On va installer le logociel `HostAPD`. Il faut vérifier que votre dongle wifi est bien de type `RTL8188` et utiliser la commande suivante. 

	wget https://github.com/jenssegers/RTL8188-hostapd/archive/v1.1.tar.gz
	tar -zxvf v1.1.tar.gz
	cd RTL8188-hostapd-1.1/hostapd
	sudo make
	sudo make install

### Configuration de `HostAPD`

Afin de paramétrer le point d’accès wifi, on édite le fichier de configuration

	sudo vim /etc/hostapd/hostapd.conf
	
Voici ce qu’on a configurer (le mot de passe est changé !).

	# Basic configuration

	interface=wlan1
	ssid=polyptyque
	channel=11
	#bridge=br0

	# WPA and WPA2 configuration

	macaddr_acl=0
	auth_algs=1
	ignore_broadcast_ssid=0
	wpa=3
	wpa_passphrase=LeMotDePasse
	wpa_key_mgmt=WPA-PSK
	wpa_pairwise=TKIP
	rsn_pairwise=CCMP
	
	# Hardware configuration
	
	driver=rtl871xdrv
	ieee80211n=1
	hw_mode=g
	device_name=RTL8192CU
	manufacturer=Realtek
	
## Démarrage des services

Il ne reste plus qu’à démarrer manuellement les services.

	sudo service isc-dhcp-server start
	sudo service hostapd start
	
Pour ne pas devoir redémarrer ces services à chaque démarrage du rPi, exécuter ces commandes : 

	sudo update-rc.d hostapd enable 
	sudo update-rc.d isc-dhcp-server enable	

## Est-ce que le wifi est visible

Cette commande permet depuis le rPi de scanner les réseaux wifi disponibles et d'obtenir des informations sur ceux-ci. 

	sudo iwlist wlan0 scan	
	
on obtient des résulats de ce type pour notre routeur :

```
  Cell 17 - Address: EC:F0:0E:4B:E5:FD
            Channel:11
            Frequency:2.462 GHz (Channel 11)
            Quality=70/70  Signal level=-5 dBm  
            Encryption key:on
            ESSID:"polyptyque"
            Bit Rates:1 Mb/s; 2 Mb/s; 5.5 Mb/s; 11 Mb/s; 6 Mb/s
                      9 Mb/s; 12 Mb/s; 18 Mb/s
            Bit Rates:24 Mb/s; 36 Mb/s; 48 Mb/s; 54 Mb/s
            Mode:Master
            Extra:tsf=0000000000000000
            Extra: Last beacon: 40ms ago
            IE: Unknown: 000A706F6C79707479717565
            IE: Unknown: 010882848B960C121824
            IE: Unknown: 03010B
            IE: Unknown: 050400010000
            IE: Unknown: 2A0104
            IE: Unknown: 32043048606C
            IE: IEEE 802.11i/WPA2 Version 1
                Group Cipher : TKIP
                Pairwise Ciphers (1) : CCMP
                Authentication Suites (1) : PSK
            IE: WPA Version 1
                Group Cipher : TKIP
                Pairwise Ciphers (1) : TKIP
                Authentication Suites (1) : PSK
            IE: Unknown: 2D1A0C001FFF00000000000000000000000000000000000000000000
            IE: Unknown: 3D160B000000000000000000000000000000000000000000
            IE: Unknown: DD180050F2020101800003A4000027A4000042435D0062322E00

```	
