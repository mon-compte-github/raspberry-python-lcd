#!/usr/bin/env python2
# -*-coding:Latin-1 -*

# on importe la lib de pilotage
# du lcd (puce hd44780)
import lcddriver

# import(s)
from time import sleep

# dessine le bonhomme en position
# (pos, pos+1 et pos+2)
# sur les lignes 1 et 2
def draw_man(lcd, pos):
    lcd.set_cursor(pos, 1)  
    lcd.write(chr(0)+chr(1)+chr(2))
    lcd.set_cursor(pos, 2)
    lcd.write(chr(4)+chr(5)+chr(6))

# efface un bonhomme précédemment
# précédemment dessiné avec draw_man
def erase_man(lcd, pos):
    lcd.set_cursor(pos, 1)  
    lcd.write("   ")
    lcd.set_cursor(pos, 2)
    lcd.write("   ")

# toute première image
# le bonhomme attend
def define_waiting_man(lcd):
    lcd.load_custom_char(0, [0b00001,0b00001,0b00011,0b00011,0b00011,0b00001,0b00000,0b00001])
    lcd.load_custom_char(1, [0b11111,0b11111,0b11101,0b11101,0b11111,0b11111,0b11111,0b11111])
    lcd.load_custom_char(2, [0b00000,0b10000,0b11000,0b00000,0b11000,0b11100,0b11000,0b10000])
    lcd.load_custom_char(4, [0b00011,0b00111,0b00111,0b00111,0b00111,0b00001,0b00011,0b00111])
    lcd.load_custom_char(5, [0b11111,0b11111,0b11111,0b11111,0b11111,0b11011,0b10001,0b10001])
    lcd.load_custom_char(6, [0b11000,0b11100,0b11100,0b11100,0b11100,0b10000,0b11000,0b11100])

# animation du bonhomme qui 
# marche vers la droite
# frames de 0 à 3, en boucle

def define_man0(lcd):
    lcd.load_custom_char(0, [0b00000,0b00001,0b00001,0b00011,0b00011,0b00011,0b00000,0b00001])
    lcd.load_custom_char(1, [0b11111,0b11111,0b11101,0b11101,0b11111,0b11111,0b11111,0b11111])
    lcd.load_custom_char(2, [0b00000,0b11000,0b00000,0b11000,0b11100,0b11000,0b10000,0b00000])
    lcd.load_custom_char(4, [0b00011,0b00011,0b00011,0b00011,0b00011,0b00001,0b00000,0b00000])
    lcd.load_custom_char(5, [0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111])
    lcd.load_custom_char(6, [0b00000,0b00000,0b10000,0b10000,0b10000,0b00000,0b10000,0b00000])

def define_man1(lcd):
    lcd.load_custom_char(0, [0b00000,0b00001,0b00001,0b00011,0b00011,0b00011,0b00000,0b01111])
    lcd.load_custom_char(1, [0b11111,0b11111,0b11101,0b11101,0b11111,0b11111,0b11111,0b11111])
    lcd.load_custom_char(2, [0b00000,0b11000,0b00000,0b11000,0b11100,0b11000,0b10000,0b00000])
    lcd.load_custom_char(4, [0b11111,0b11111,0b11101,0b00011,0b00111,0b01111,0b01111,0b00111])
    lcd.load_custom_char(5, [0b11111,0b11111,0b11111,0b11111,0b10011,0b00000,0b00000,0b00000])
    lcd.load_custom_char(6, [0b11110,0b01100,0b11100,0b11100,0b11100,0b00000,0b00000,0b00000])

# alias
def define_man2(lcd):
    define_man0(lcd)

def define_man3(lcd):
    lcd.load_custom_char(0, [0b00000,0b00001,0b00001,0b00011,0b00011,0b00011,0b00011,0b00000])
    lcd.load_custom_char(1, [0b00000,0b11111,0b11111,0b11101,0b11101,0b11111,0b11111,0b11111])
    lcd.load_custom_char(2, [0b00000,0b00000,0b11000,0b00000,0b11000,0b11100,0b11000,0b10000])
    lcd.load_custom_char(4, [0b00001,0b00011,0b00111,0b00111,0b00111,0b01111,0b01100,0b00000])
    lcd.load_custom_char(5, [0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11110,0b11111])
    lcd.load_custom_char(6, [0b10000,0b11000,0b10000,0b00000,0b00000,0b00000,0b00000,0b00000])

#
# début 
#


# TODO essayer d'améliorer les perfs en écrivant les caractères une fois pour toute,
# en les redéfinissant au fur et à mesure et en les décalant vers la droite (shift)

if __name__ == "__main__":

    # on initialise le lcd
    lcd = lcddriver.lcd()

    # position initiale
    position = 0

    # standing still
    define_waiting_man(lcd)
    draw_man(lcd, position)
    sleep(2)
    erase_man(lcd, position)
    position += 1

    # run baby run
    while position < 17:

        locals()["define_man" + str((position -1) % 4)](lcd)
        draw_man(lcd, position)
        sleep(0.55)
        erase_man(lcd, position)

        position += 1
    
    # TODO tourner et repartir dans l'autre sens
    # (nécessite d'inverser les bitmaps)

    define_waiting_man(lcd)
    draw_man(lcd, position)

# EOF