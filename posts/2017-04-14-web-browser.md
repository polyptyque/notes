---
layout: post
title:  "14 avril"
description : "Déclenchement de la prise de vue depuis l’iPad"
date:   2017-04-14 12:00:00 +02:00
author: Arthur Violy
categories: UDP Broadcast
---

Les versions slave-module et master-module progressent. 

Cela signifie qu’aujourd’hui, depuis un navigateur web, via un site accessible en `localhost` (sur les lieux de l’installation, dans une web-app...), on peut saisir le formulaire, puis cliquer sur le declencheur photo sur la dernière étape, et cela envoie une requête HTTP `POST` au master-module. 

À cette requête HTTP, le master-module renvoie lui même un datagram `UDP`, 

en mode `BROADCAST`, c’est à dire à tout ceux qui veulent bien gérer ce message. En l’occurrence tous les slave-module. Aujourd'hui on a fait le test avec un seul CMIO, et ça marche (même en wifi) ! 

Ensuite nous avons implémenté sur le slave-module, à la réception du message UDP, un déclenchement de la prise de vues sur 2 caméras et c’est fonctionnel. reste à optimiser le temps de traitement car les prises de vues étaient faites successivement, avec un temps d'écriture des fichiers, faible, mais réel, environ 1/4 de seconde. 
