---
layout: post
title:  "31 mai"
description : "Affiché une mire sur la preview caméra"
date:   2017-05-30 00:00:00 +02:00
author: Arthur Violy
categories: caméra python
---

Il a été difficile de trouver la solution mais voilà, c'est — *presque* — bon pour afficher le retour vidéo en temps réel, 
avec une *mire* par dessus, en `overlay`.

<video src="https://mastodon.social/media/iUDUM5ep-vKxdvjT6rI" type="video/mp4" poster="images/mire-video-pi-camera.png" controls autoplay loop>
[![voir la vidéo](images/mire-video-pi-camera.png)](https://mastodon.social/media/iUDUM5ep-vKxdvjT6rI)
</video>

Le mécanisme était en fait intégré à la librairie python *picamera*, avec la méthode `camera.add_overlay`

```python

import picamera
from PIL import Image
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()

    # Load the arbitrarily sized image
    img = Image.open('overlay-400-240.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    width = ((img.size[0] + 31) // 32) * 32
    height = ((img.size[1] + 15) // 16) * 16
    print("pad size",width,height)
    pad = Image.new('RGBA', (width,height))
    # Paste the original image into the padded one
    pad.paste(img, (0, 0))
    print("img size",img.size)
    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    #b = img.tobytes('rgba')    
    b = pad.tobytes()
    o = camera.add_overlay(b, size=img.size)
    print(camera)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    #o.alpha = 128
    o.layer = 3

    # Wait indefinitely until the user terminates the script
    while True:
        sleep(1)
```

Bref, j'ai pas mal galéré à essayé de passer par d'autres solutions (OpenCV, Pygame, ...) avec lesquels je n'ai pas réussi à m'en sortir