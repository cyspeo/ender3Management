# Gestion du blocage de filament 
Le but est d'ajouter un capteur de filament tendu pour mettre en pause l'imprimante afin de défaire les noeuds.

## Links 
Installation rasbian sans écran ni clavier:
https://raspberry-pi.fr/raspberry-pi-sans-ecran-sans-clavier/

Camera esp32 :
http://electroniqueamateur.blogspot.com/2020/01/esp32-cam-premiere-utilisation-avec.html

Utisation d'une camera usb standard sur le raspberry:
https://www.raspberrypi.org/documentation/usage/webcams/

## Materiel
- un raspberry
- un capteur bouton poussoir
- du cable
## Os (raspbian)
Install pip
sudo apt-get install python-pip
Install lib pyserial
python -m pip install pyserial

## Code source
### Gestion du bouton poussoir

### Envoi des commandes à l'imprimante
python ./sendgcode.py -p'/dev/ttyUSB0' -c'G1 X0.1 Y200.0 Z0.3 F1500.0 E15'

