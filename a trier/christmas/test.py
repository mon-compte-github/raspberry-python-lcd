# on importe le pilote
import lcddriver

from time import sleep 

# on initialise le lcd
lcd = lcddriver.lcd()

lcd.load_custom_char(0, [0xe,0x1b,0x1b,0x1f,0x1b,0x1b,0x1b,0x0])
lcd.load_custom_char(1, [0x1e,0x1b,0x1b,0x1e,0x1b,0x1b,0x1e,0x0])
lcd.load_custom_char(2, [0xe,0x1b,0x18,0x18,0x18,0x1b,0xe,0x0])
lcd.load_custom_char(3, [0x1e,0x1b,0x1b,0x1b,0x1b,0x1b,0x1e,0x0])
lcd.load_custom_char(4, [0x1f,0x18,0x18,0x1e,0x18,0x18,0x1f,0x0])
lcd.load_custom_char(5, [0x1f,0x18,0x18,0x1e,0x18,0x18,0x18,0x0])
lcd.load_custom_char(6, [0xe,0x1b,0x18,0x1b,0x1b,0x19,0xf,0x0])
lcd.load_custom_char(7, [0x1b,0x1b,0x1b,0x1f,0x1b,0x1b,0x1b,0x0])
lcd.load_custom_char(8, [0x0,0x0,0xe,0x3,0xf,0x1b,0xf,0x0])
lcd.load_custom_char(9, [0xe,0x1b,0x1b,0x1b,0x1b,0x1b,0xe,0x0])
lcd.load_custom_char(10, [0x2,0x6,0xe,0x6,0x6,0x6,0x6,0x0])
lcd.load_custom_char(11, [0xe,0x1b,0x3,0x6,0xc,0x18,0x1f,0x0])


for k in range(4):
	lcd.message("".rjust(20, " "), k)

str = ''
for k in range(8):
	str = str + chr(k)

lcd.message(str, 0)

