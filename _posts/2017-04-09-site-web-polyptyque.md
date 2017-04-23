---
layout: post
title:  "9 avril"
description : "Site web avec démo, algorithme"
date:   2017-04-09 18:00:00 +02:00
author: Arthur Violy
categories: web algorithme blendmode nodejs
---

Le site [polyptyque.photo](http://polyptyque.photo/) était déjà en ligne avec une démo interactive depuis le 29 mars. Mais cette démo utilisait les images assemblées à la main — sur Photoshop® — par Bertrand. Ce soir une nouvelle fonctionnalité est dévellopée, le mélange par mode de fusion (blending mode) et opacité, via la librairie node canvas. 
[mix A-B](http://polyptyque.photo/demo-mix-A-B) et [mix B-A](http://polyptyque.photo/demo-mix-B-A).

L’algorithme est le suivant : 

- On a deux ensembles `A` & `B` composés de 19 images chacun :
	- 1 image centrale, notée `0`
	- 9 images à droite, numérotées de `r1` à `r9`, où `r1` est la plus proche de `0`
	- 9 images à gauche, numérotées de `l1` à `l9`, sur le même principe
- Le mode de fusion utilisé est `darker` (_obscursir_ en français) 
- Côté droit, `A` est fusionné à `B`. Côté gauche, c’est l’inverse, `B` est fusionné à `A`. Au centre, peut importe car l’opacité de fusion est de `100%`
- Sur chaque côté, l’opacité varie en fonction de la position, dans notre cas avec un facteur multiplicateur de `11.11%`. Ainsi la dernière image `r9` est mélangée avec une opacité diminuée de 99.99% (arrondi à 100%, et donc invisible) 

Autre bonne nouvelle de cette fin de semaine, F93 a réceptionné pour le projet 10 Raspberry Pi Compute Module dev kit, ainsi que 20 caméras PiV2 !

