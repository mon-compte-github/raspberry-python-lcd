#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from time import sleep
from datetime import datetime

class FourthScreen:

    def __init__(self):
        # positions
        self.leftward = True

        # l'écart entre le pacman et le fantome
        # vaut les dizaines des minutes + 1
        self.pacman = 19
        self.ghost = 25

    def run(self, lcd):

        # diamond
        lcd.load_custom_char(0, [0b00000,0b00100,0b01110,0b11111,0b11111,0b01110,0b00100,0b00000])
        
        # ghost (normal)
        lcd.load_custom_char(1, [0b01110,0b11111,0b10101,0b11111,0b11111,0b11111,0b10101,0b10101])

        # ghost (afraid)
        lcd.load_custom_char(2, [0b01110,0b11111,0b10101,0b10101,0b11111,0b10101,0b10101,0b01010])

        # pacman (normal, left)
        lcd.load_custom_char(3, [0b01110,0b10111,0b11111,0b11111,0b00011,0b11111,0b01111,0b01110])

        # pacman (opened mouth, right)
        lcd.load_custom_char(4, [0b01110,0b11101,0b11111,0b11100,0b11000,0b11100,0b01111,0b01110])

        xmas = datetime(2019, 12, 24, 23, 59, 59)
        delta = xmas - datetime.now()
        dizaines = ((delta.seconds // 60) % 60) // 10
        
        # l'écart entre le pacman et le fantôme dépend du temps qu'il reste
        # on le détermine avec la dizaine des minutes (1 dizaine = 1 case)
        # avec toujours au moins une case d'écart
        self.ghost = self.pacman + dizaines + 1

        # idem pour la vitesse qui sera de 0.3 au plus rapide
        self.sleepingTime = 0.3 + (0.15 * dizaines)

        while (delta.seconds//3600) > 0:

            minutes = (delta.seconds // 60) % 60
            hour = delta.seconds // 3600
            dizaines = minutes // 10
            
            # remplissage de l'écran
            lcd.message("   ouverture des    ", 0)
            lcd.message("    cadeaux dans    ", 1)
            lcd.message("      " + str(hour).rjust(2, " ") + " h " + str(minutes).rjust(2, "0") + "      ", 2)
            
            # animation
            if(self.leftward):
                # le diamant est en toute première case
                # le pacman se sauve vers la gauche
                # pour le manger avant de se faire
                # rattraper par le fantôme
                if(self.pacman > 0):
                    
                    lcd.message(chr(0) + "".rjust(self.pacman - 1, chr(0xa5)) + \
                        chr(3) + "".rjust(self.ghost - self.pacman, " ") + chr(1) + "".rjust(20, " "), 3)
                    
                    self.pacman -= 1
                    self.ghost -= 1

                else:
                    # le pacman mange le diamant, il change de sens
                    # et se met à courir après le fantôme qui s'enfuit
                    lcd.message(chr(4) + "".rjust(self.ghost - self.pacman, " ") + chr(2) + "".rjust(20, " "), 3)
                    
                    self.leftward = False
                    self.pacman += 1
                    self.ghost += 1
            else:
                if(self.pacman < 20):
                    # le pacman coure après le fantôme pour le manger
                    lcd.message("".rjust(self.pacman, chr(0xa5)) + chr(4) + "".rjust(self.ghost - self.pacman, " ") + chr(2) + "".rjust(20, " "), 3)
                    self.pacman += 1
                    self.ghost += 1
                else:
                    # reset
                    self.pacman = 19
                    self.ghost = self.pacman + dizaines + 1
                    self.sleepingTime = 0.3 + (0.20 * dizaines)
                    self.leftward = True

            delta = xmas - datetime.now()
            sleep(self.sleepingTime)
    

