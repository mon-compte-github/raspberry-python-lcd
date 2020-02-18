#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe le pilote
import lcddriver

from first_screen import FirstScreen

from count_down import CountDown
from final_screen import FinalScreen
from second_screen import SecondScreen
from third_screen import ThirdScreen
from fourth_screen import FourthScreen

# on initialise le lcd
lcd = lcddriver.lcd()
FirstScreen().run(lcd)
SecondScreen().run(lcd)
ThirdScreen().run(lcd)
FourthScreen().run(lcd)
CountDown(59).run(lcd)
FinalScreen().run(lcd)
