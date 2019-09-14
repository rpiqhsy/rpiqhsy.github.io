from gpiozero import AngularServo
from time import sleep
import Adafruit_DHT

servo_pin = 4 #pin of servo
dht_pin = 16 #pin of dht sensor
delay = 5 # second,must more than 2. 

servo = AngularServo(servo_pin, min_angle=-90, max_angle=90)
servo.angle = 0

while True:
    humi, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,dht_pin)
    print("humi = %f ,temp = %f"%(humi,temp))
    if humi > 80:
        servo.angle = 90
        print("servo 90")
    elif humi < 75:
        servo angle = 0
        print("servo 0")
    else :
        print("servo err")
    sleep(delay)
