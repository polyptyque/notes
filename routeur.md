### Configuration d'un raspberry Pi en tant que routeur réseau

	apt-get install isc-dhcp-server bind9

Le serveur DHCP va donner les adresses IP aux compute-modules qui n'en ont pas
Le serveur DNS (bind9) va associer un nom à une IP (en local uniquement)

## DHCP

/etc/dhcp/dhcpd.conf


