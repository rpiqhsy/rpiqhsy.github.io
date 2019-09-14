from gpiozero import AngularServo
from time import sleep
import Adafruit_DHT

servo = AngularServo(servo_pin, min_angle=-90, max_angle=90)
servo.angle = 0
while True:
