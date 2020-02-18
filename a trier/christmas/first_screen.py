#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from time import sleep
from datetime import datetime

class FirstScreen:

    def run(self, lcd):

        xmas = datetime(2019, 12, 24, 23, 59, 59)
        delta = xmas - datetime.now()

        while delta.days > 7:
            # remplissage de l'écran
            lcd.message(">                  <", 0)
            lcd.message(">  encore " + str(delta.days).rjust(2, " ") + " jours <", 1)
            lcd.message(">   avant NOEL !!  <", 2)
            lcd.message(">                  <", 3)

            delta = xmas - datetime.now()

            # refresh ttes les minutes
            sleep(60)
