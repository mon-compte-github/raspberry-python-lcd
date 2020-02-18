#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from time import sleep
from random import random, randint

class FinalScreen:

    def __init__(self):
        # empty characters positions
        # (row, begin, end)
        self.emptyPlaces = [(0,0,5), (0,14,19), (1,0,2), (1,17,19), (2,0,2), (2,17,19), (3,0,5), (3,14,19)]
        
    def run(self, lcd):
 
        lcd.load_custom_char(0, [0b11111,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
        lcd.load_custom_char(1, [0b00000,0b10000,0b01000,0b00100,0b00010,0b00001,0b00000,0b00000])

        lcd.load_custom_char(2, [0b00000,0b00000,0b00000,0b00100,0b01110,0b00100,0b00000,0b00000])
        lcd.load_custom_char(3, [0b00000,0b00000,0b00100,0b00100,0b11111,0b00100,0b00100,0b00000])
        lcd.load_custom_char(4, [0b00000,0b00000,0b00000,0b01010,0b00100,0b01010,0b00000,0b00000])
        lcd.load_custom_char(5, [0b00000,0b00000,0b10001,0b01010,0b00100,0b01010,0b10001,0b00000])
        lcd.load_custom_char(6, [0b00000,0b00000,0b01010,0b11011,0b00100,0b11011,0b01010,0b00000])

        while True:
            # remplissage de l'écran
            lcd.message("      ________      ", 0)
            lcd.message("   |" + chr(1) + "/ JOYEUX " + chr(1) + "/|   ", 1)
            lcd.message("   |/" + chr(1) + "  NOEL  /" + chr(1) + "|   ", 2)
            lcd.message("      " + chr(0) * 8  + "      ", 3)

            # étoiles
            for place in self.emptyPlaces:
                # pour chaque case de l'intervalle
                for k in range(place[1], place[2]+1):
                    if(random() < 0.33):
                        lcd.set_cursor(k, place[0])
                        lcd.write(chr(randint(2, 6)))
            
            sleep(2)
