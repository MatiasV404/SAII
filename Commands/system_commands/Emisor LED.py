#Link 1: https://parzibyte.me/blog/2020/02/09/raspberry-python-encender-apagar-led/
#Link 2: https://aprendiendoarduino.wordpress.com/2020/03/04/manejar-gpio-raspberry-pi/

# import RPi.GPIO as GPIO

# Instalar biblioteca Rpi.GPIO
# sudo apt-get update ó pip install RPi.GPIO

# Instalar ó actualizar Raspbian y Python
# sudo apt-get update
# sudo apt-get upgrade
# sudo apt-get install python3-dev
# sudo apt-get install pyton3-rpi.gpio

# Código link 1
import time
ESPERA = 0.5
PIN = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(ESPERA)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(ESPERA)
    
# Código link 2
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(12, gpio.OUT)

for  x in range ( 0, 10):

    gpio.output(12, True)
    time.sleep(0.5)
    gpio.output(12, False)
    time.sleep(0.5)

print("Ejecución finalizada")