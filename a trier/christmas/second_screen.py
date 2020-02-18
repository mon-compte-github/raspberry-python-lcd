#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from time import sleep, time
from datetime import datetime

class SecondScreen:

    def __init__(self):
        self.count = 0

    def run(self, lcd):

        xmas = datetime(2019, 12, 24, 23, 59, 59)
        delta = xmas - datetime.now()

        while delta.days > 0:

            t = time()

            # remplissage de l'écran
            lcd.message(" NOEL c'est dans ...", 0)
            lcd.message("  " + str(delta.days) + " jours           ", 1)
            lcd.message("   " + str(delta.seconds//3600).rjust(2, " ") + " heures        ", 2)
            lcd.message("     " + str((delta.seconds//60)%60).rjust(2, " ") + " minutes     ", 3)

            # petite animation tranquille
            lcd.set_cursor(18, 2)
            lcd.write(chr(0xdb) if self.count != 1 else chr(0x20))
            lcd.write(chr(0xdb) if self.count != 0 else chr(0x20))
            lcd.set_cursor(18, 3)
            lcd.write(chr(0xdb) if self.count != 2 else chr(0x20))
            lcd.write(chr(0xdb) if self.count != 3 else chr(0x20))
            self.count = (self.count + 1) % 4

            delta = xmas - datetime.now()
            t = (t + 1 - time())

            if(t < 1):
                sleep(t)
