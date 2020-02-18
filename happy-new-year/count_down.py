#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver
import time

from time import sleep
from datetime import datetime

# get current time millis
milliseconds = lambda: int(round(time.time() * 1000))

# digits will be printed
# on screen with this layout
#   0 1  2 3
#   4 5  6 7

# translate digit into function's name (see below)
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# glyphs for numbers

def zero(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00111,0b01111,0b11100,0b11000,0b11000,0b11000,0b11000,0b11000])
    lcd.load_custom_char(1+shift, [0b11100,0b11110,0b00111,0b00011,0b00011,0b00011,0b00011,0b00011])
    lcd.load_custom_char(4+shift, [0b11000,0b11000,0b11000,0b11000,0b11000,0b11100,0b01111,0b00111])
    lcd.load_custom_char(5+shift, [0b00011,0b00011,0b00011,0b00011,0b00011,0b00111,0b11110,0b11100])

def one(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00000,0b00000,0b00000,0b00001,0b00011,0b00110,0b01100,0b00000])
    lcd.load_custom_char(1+shift, [0b00100,0b01100,0b11100,0b11100,0b11100,0b11100,0b11100,0b11100])
    lcd.load_custom_char(4+shift, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
    lcd.load_custom_char(5+shift, [0b11100,0b11100,0b11100,0b11100,0b11100,0b11100,0b11100,0b11100])

def two(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00111,0b01111,0b11100,0b11000,0b00000,0b00000,0b00000,0b00000])
    lcd.load_custom_char(1+shift, [0b11100,0b11110,0b00111,0b00011,0b00011,0b00011,0b00110,0b01100])
    lcd.load_custom_char(4+shift, [0b00000,0b00001,0b00011,0b00110,0b01100,0b11000,0b11111,0b11111])
    lcd.load_custom_char(5+shift, [0b11000,0b10000,0b00000,0b00000,0b00000,0b00000,0b11111,0b11111])

def three(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00111,0b01111,0b11100,0b11000,0b00000,0b00000,0b00000,0b00111])
    lcd.load_custom_char(1+shift, [0b11100,0b11110,0b00111,0b00011,0b00011,0b00011,0b00110,0b11100])
    lcd.load_custom_char(4+shift, [0b00111,0b00000,0b00000,0b00000,0b11000,0b11100,0b01111,0b00111])
    lcd.load_custom_char(5+shift, [0b11100,0b00110,0b00011,0b00011,0b00011,0b00111,0b11110,0b11100])

def four(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00000,0b00000,0b00000,0b00000,0b00001,0b00011,0b00111,0b01110])
    lcd.load_custom_char(1+shift, [0b00011,0b00111,0b01111,0b11111,0b11011,0b10011,0b00011,0b00011])
    lcd.load_custom_char(4+shift, [0b11100,0b11111,0b11111,0b00000,0b00000,0b00000,0b00000,0b00000])
    lcd.load_custom_char(5+shift, [0b00011,0b11111,0b11111,0b00011,0b00011,0b00011,0b00011,0b00011])

def five(lcd, shift):
    lcd.load_custom_char(0+shift, [0b11111,0b11111,0b11000,0b11000,0b11000,0b11000,0b11111,0b01111])
    lcd.load_custom_char(1+shift, [0b11111,0b11111,0b00000,0b00000,0b00000,0b00000,0b11000,0b11100])
    lcd.load_custom_char(4+shift, [0b00111,0b00000,0b00000,0b00000,0b00000,0b11000,0b11111,0b01111])
    lcd.load_custom_char(5+shift, [0b11110,0b00111,0b00011,0b00011,0b00011,0b00110,0b11100,0b11000])

def six(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00111,0b01111,0b11100,0b11000,0b11000,0b11000,0b11000,0b11111])
    lcd.load_custom_char(1+shift, [0b11100,0b11110,0b00111,0b00000,0b00000,0b00000,0b00000,0b11100])
    lcd.load_custom_char(4+shift, [0b11111,0b11100,0b11000,0b11000,0b11000,0b11100,0b01111,0b00111])
    lcd.load_custom_char(5+shift, [0b11110,0b00111,0b00011,0b00011,0b00011,0b00111,0b11110,0b11100])

def seven(lcd, shift):
    lcd.load_custom_char(0+shift, [0b11111,0b11111,0b00000,0b00000,0b00000,0b00000,0b00000,0b00001])
    lcd.load_custom_char(1+shift, [0b11111,0b11111,0b00011,0b00011,0b00111,0b01110,0b11100,0b11000])
    lcd.load_custom_char(4+shift, [0b00001,0b00001,0b00001,0b00001,0b00001,0b00001,0b00001,0b00001])
    lcd.load_custom_char(5+shift, [0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b10000,0b10000])

def eight(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00111,0b01111,0b11100,0b11000,0b11000,0b11000,0b01100,0b00111])
    lcd.load_custom_char(1+shift, [0b11100,0b11110,0b00111,0b00011,0b00011,0b00011,0b00110,0b11100])
    lcd.load_custom_char(4+shift, [0b01111,0b11100,0b11000,0b11000,0b11000,0b11100,0b01111,0b00111])
    lcd.load_custom_char(5+shift, [0b11110,0b00111,0b00011,0b00011,0b00011,0b00111,0b11110,0b11100])

def nine(lcd, shift):
    lcd.load_custom_char(0+shift, [0b00111,0b01111,0b11100,0b11000,0b11000,0b11000,0b11100,0b01111])
    lcd.load_custom_char(1+shift, [0b11100,0b11110,0b00111,0b00011,0b00011,0b00011,0b00111,0b11111])
    lcd.load_custom_char(4+shift, [0b00111,0b00000,0b00000,0b00000,0b00000,0b11100,0b01111,0b00111])
    lcd.load_custom_char(5+shift, [0b11111,0b00011,0b00011,0b00011,0b00011,0b00111,0b11110,0b11100])

class CountDown:

    def __init__(self, count):
        self.count = count
    
    def __print_digit(self, lcd, digit, shift):
        funcName = globals()[digits[digit]]
        funcName(lcd, (2 if shift else 0))
        
    def run(self, lcd):

        # remplissage de l'écran
        lcd.message(" " * 20, 0)
        lcd.message(" " * 8 + chr(0) + chr(1) + chr(2) + chr(3) + " " * 8, 1)
        lcd.message(" " * 8 + chr(4) + chr(5) + chr(6) + chr(7) + " " * 8, 2)
        lcd.message(" " * 20, 3)

        while self.count > 0:
            millis = milliseconds()
            
            # split number into two digits
            d = (self.count / 10)
            u = (self.count % 10)

            # write on screen
            self.__print_digit(lcd, d, False)
            self.__print_digit(lcd, u, True)
            
            print str(d) + str(u)

            # compute remaining time until next second 
            delta = 1000 - (milliseconds() - millis)
            if(delta > 0):
                sleep(delta / float(1000))

            self.count -= 1

