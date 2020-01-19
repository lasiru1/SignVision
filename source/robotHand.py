import RPi.GPIO as GPIO
import time


servoPIN_thumb = 17
servoPIN_index = 21
servoPIN_middle = 22
servoPIN_ring = 18
servoPIN_pinky = 16
servoPIN_yaw = 24
servoPIN_pitch = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN_thumb, GPIO.OUT)
GPIO.setup(servoPIN_index, GPIO.OUT)
GPIO.setup(servoPIN_middle, GPIO.OUT)
GPIO.setup(servoPIN_ring, GPIO.OUT)
GPIO.setup(servoPIN_pinky, GPIO.OUT)
GPIO.setup(servoPIN_yaw, GPIO.OUT)
GPIO.setup(servoPIN_pitch, GPIO.OUT)

# motors
thumb = GPIO.PWM(servoPIN_thumb, 50) 
index = GPIO.PWM(servoPIN_index, 50) 
middle = GPIO.PWM(servoPIN_middle, 50) 
ring = GPIO.PWM(servoPIN_ring, 50) 
pinky = GPIO.PWM(servoPIN_pinky, 50) 
yaw = GPIO.PWM(servoPIN_yaw, 50) 
pitch = GPIO.PWM(servoPIN_pitch, 50)
thumb.start(2.5)
index.start(2.5)
middle.start(2.5)
ring.start(2.5)
pinky.start(2.5)
yaw.start(2.5)
pitch.start(2.5)
try:
  while True:
    thumb.ChangeDutyCycle(11)
    index.ChangeDutyCycle(11)
    middle.ChangeDutyCycle(11)
    ring.ChangeDutyCycle(11)
    pinky.ChangeDutyCycle(11)
    yaw.ChangeDutyCycle(11)
    pitch.ChangeDutyCycle(11)

    time.sleep(0.5)
except KeyboardInterrupt:
  thumb.stop()
  index.stop()
  middle.stop()
  ring.stop()
  pinky.stop()
  yaw.stop()
  pitch.stop()
  GPIO.cleanup()