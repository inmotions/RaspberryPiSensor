#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
 
trigger_pin = 16    ##使用16号引脚
echo_pin = 18       ##使用18号引脚
 
GPIO.setmode(GPIO.BOARD)     ##使用BCM引脚编号，此外还有GPIO.BCM
GPIO.setup(trigger_pin,GPIO.OUT)   ##设置引脚输出
GPIO.setup(echo_pin,GPIO.IN)        ##设置引脚输入
 
def send_trigger_pulse():
    GPIO.output(trigger_pin,True)
    time.sleep(0.00015)
    GPIO.output(trigger_pin,False)
 
def wait_for_echo(value,timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count>0:
        count = count-1
 
def get_distance():
    send_trigger_pulse()
    wait_for_echo(True,10000)
    start = time.time()
    wait_for_echo(False,10000)
    finish = time.time()
    pulse_len = finish-start
    distance_cm = pulse_len/0.000058
    return distance_cm
 
while True:
    print("距离 = %f cm"%get_distance())
    time.sleep(1)
GPIO.cleanup()
