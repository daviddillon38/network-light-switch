import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

def turnOn():
  GPIO.output(21, GPIO.HIGH)
  print('Relay 1 On')

def turnOff():
  GPIO.output(21, GPIO.LOW)
  print('Relay 1 Off')
