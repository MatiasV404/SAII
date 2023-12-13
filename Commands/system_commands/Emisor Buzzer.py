# importamos libreria GPIO
import RPi.GPIO as GPIO
import time
# desactivamos mensajes de error
GPIO.setwarnings(False)
# guardamos en una variable el pin de salida
pin=18
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# indicamos que el GPIO18 es de salida de corriente
GPIO.setup(pin,GPIO.OUT)
tiempo=0
# bucle que se repite de forma indefinida
while (tiempo<1):
    # input para introducir el PWM
    PWM="3"
    # input para introducir los Herzios
    HZ="50"
    # pasamos los valores a integer
    pwm=int(PWM)
    hz=int(HZ)
    # enviamos el sonido
    pwm_led=GPIO.PWM(pin,hz)
    pwm_led.start(pwm)
    time.sleep(2)
    tiempo=tiempo+1
    pwm_led.stop(pwm)