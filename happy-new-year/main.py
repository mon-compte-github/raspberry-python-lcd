#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from first_screen import FirstScreen
from count_down import CountDown
from final_screen import FinalScreen

# on initialise le lcd
lcd = lcddriver.lcd()

FirstScreen().run(lcd)
# plus que 59 secondes avant minuit ;-)
CountDown(59).run(lcd)
FinalScreen().run(lcd)
