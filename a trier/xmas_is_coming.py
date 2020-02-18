#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from datetime import *
from time import *

# on initialise le lcd
lcd = lcddriver.lcd()

# xmas time
xmas = datetime(2019, 12, 25, 23, 59, 59)

while True:

    delta = xmas - datetime.now()
    
    lcd.message("xmas is coming ...", 0)
    lcd.message(" " + str(delta.days) + " jours", 1)
    lcd.message("  " + str(delta.seconds//3600) + " heures", 2)
    lcd.message("   " + str((delta.seconds//60)%60) + " minutes", 3)
    
    sleep(5)

