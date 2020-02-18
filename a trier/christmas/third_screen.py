#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from time import sleep
from datetime import datetime

class ThirdScreen:

    def run(self, lcd):

        lcd.load_custom_char(0, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b11111])
        lcd.load_custom_char(1, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b11111,0b11111])
        lcd.load_custom_char(2, [0b00000,0b00000,0b00000,0b00000,0b11111,0b11111,0b11111,0b11111])
        lcd.load_custom_char(3, [0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111])

        # reset
        lcd.load_custom_char(4, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
        lcd.load_custom_char(5, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
        lcd.load_custom_char(6, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
        lcd.load_custom_char(7, [0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000,0b00000])
        
        xmas = datetime(2019, 12, 24, 23, 59, 59)
        delta = xmas - datetime.now()
        dizaines = ((delta.seconds // 60) % 60) // 10

        # idem pour la vitesse qui sera de 0.3 au plus rapide
        self.sleepingTime = 0.3  ##+ (0.15 * dizaines)

        self.pos = 3 # -------v
        self.heights = [0,1,2,3,2,1,0]
        for k in range(20 - len(self.heights)):
            self.heights.append(0)

        self.right = True

        while (delta.seconds//3600) > 0:

            minutes = (delta.seconds // 60) % 60
            hour = delta.seconds // 3600
            dizaines = minutes // 10
            
            # remplissage de l'écran
            lcd.message("   ouverture des    ", 0)
            lcd.message("    cadeaux dans    ", 1)
            lcd.message("      " + str(hour).rjust(2, " ") + " h " + str(minutes).rjust(2, "0") + "      ", 2)
            
            # animation
            if(self.right):

                for k in range(1, 4):
                    if(self.pos <= 16 and self.heights[self.pos + k] < 4):
                        self.heights[self.pos + k] += 1
                    
                for k in range(0, 4):
                    if(self.pos >= 3 and self.heights[self.pos - k] > 0):
                        self.heights[self.pos - k] -= 1

                if(self.pos <= 16):
                    self.pos += 1
                else:
                    self.right = not self.right

            else:

                for k in range(1, 4):
                    if(self.pos >= 3 and self.heights[self.pos - k] < 4):
                        self.heights[self.pos - k] += 1
                    
                for k in range(0, 4):
                    if(self.pos <= 16 and self.heights[self.pos + k] > 0):
                        self.heights[self.pos + k] -= 1

                if(self.pos >= 3):
                    self.pos -= 1
                else:
                    self.right = not self.right

            print self.heights

            lcd.message("".join(map(lambda x: chr(x), self.heights)), 3)
            
            delta = xmas - datetime.now()
            sleep(self.sleepingTime)
            
    
