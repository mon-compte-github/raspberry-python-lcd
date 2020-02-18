#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from time import sleep
from datetime import datetime

class FirstScreen:

    def __init__(self):
        # nop

    def run(self, lcd):

        newYear = datetime(2020, 12, 31, 23, 59, 59)
        delta = newYear - datetime.now()
        dizaines = ((delta.seconds // 60) % 60) // 10
        
        while (delta.seconds//3600) > 0:

            minutes = (delta.seconds // 60) % 60
            hour = delta.seconds // 3600
            dizaines = minutes // 10
            
            # remplissage de l'écran
            lcd.message("".rjust(20), 0)
            lcd.message("   nouvelle année dans ...    ", 1)
            lcd.message("      " + str(hour).rjust(2, " ") + " h " + str(minutes).rjust(2, "0") + "      ", 2)
            lcd.message("".rjust(20), 3)


            delta = newYear - datetime.now()
            sleep(self.sleepingTime)
    

