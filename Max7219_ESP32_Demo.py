#
# Demo Program using the MicroPython Max7219 driver on a NodeMCU-32S
# (ESP-32) MCU board. This demo works with 4 Max7219 8x8 LED Matrix 
# Modules.
#
# On my NodeMCU-32S (ESP32) MCU board, for SPI I'm using
# the following pins to interface the 4 Max7219 8x8 LED
# matrix modules:
#
#    MOSI = 13
#    MISO = 12 (nc)
#    CLK  = 14
#    CS (SS) = 15
#
# I used GPIO13, GPIO14 and GPIO15 Along with +5V, and GND
# and was successful in using this program with four Max7219
# 8x8 LED matrix displays daisy chained together.
#
# Aitionally, I added a "clear()" method to the "Matrix8x8" class
# (part of the max7219.py library module) to make it easy to
# clear the display (rather than accumulate lit LEDs as was
# happening without the use of a clear() method. This modified
# module library is called "max7219a.py".
#
# Filename: "Max7219_ESP32_Demo.py"
#

# Function to reverse a string 
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

from machine import Pin, SPI
import time
import max7219a

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13))
ss = Pin(15, Pin.OUT)
display = max7219.Matrix8x8(spi, ss, 4)

# Display the message "THIS IS A TEST OKAY":
delay = 1

while True:
    display.clear()
    
    # This displays "THIS" left-to-right across the 4-char display.
    message1 = "SIHT"
    display.text(message1,0,0,1)
    display.show()
    time.sleep(delay)
    display.clear()

    # This displays "IS A" left-to-right across the 4-char display.
    message2 = "A SI"
    display.text(message2,0,0,1)
    display.show()
    time.sleep(delay)
    display.clear()

    # This displays "TEST" left-to-right across the 4-char display.
    message3 = "TSET"
    display.text(message3,0,0,1)
    display.show()
    time.sleep(delay)
    display.clear()
    
    # Display a string in proper order. String length must be a multiple of 4.
    # Seems you may need to add 10 spaces to end of string to avoid the error
    # message "string index out of range"
    message4 = "    The quick brown fox jumps over the lazy dog.          "

    print("String length = " + str(len(message4)) + " characters.")
    
    # Process message4 string 4 characters at a timje and reverse
    # the order of these 4 characters just before displaying them.
    for i in range(0,55):
        message=""
        for j in range(0,4):       
            message = message + message4[i+j]
        message = reverse(message)
        display.text(message,0,0,1)
        display.show()
        time.sleep(delay/2)
        display.clear()

    # This displays "OKAY" left-to-right across the 4-char display.
    message5 = "YAKO"
    display.text(message5,0,0,1)
    display.show()
    time.sleep(delay)
    display.clear()        # Last time need to do an extra "display.show()"
    display.show()
    time.sleep(delay)
    
# EOF
