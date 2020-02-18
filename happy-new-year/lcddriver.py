
import smbus
from time import sleep

# Joined existing 'i2c_lib.py' and 'lcddriver.py' into a single library
# Original post at https://www.recantha.co.uk/blog/?p=4849

# some const

# default LCD Address
LCD_ADDRESS = 0x27

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# ddram offsets for up to 4 rows
# first row wraps on the third one
# and second row wraps on the fourth one
LCD_ROW_OFFSET = (0x80, 0xC0, 0x94, 0xD4)

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100  # Enable bit
Rw = 0b00000010  # Read/Write bit
Rs = 0b00000001  # Register select bit

# internal class
class i2c: 
    def __init__(self, i2c_addr=LCD_ADDRESS, port=1):
        # i2c stuff
        self._addr = i2c_addr
        self._bus = smbus.SMBus(port)

    # Write a single byte
    def write_byte(self, byte):
        self._bus.write_byte(self._addr, byte)
        sleep(0.0001)

    def write_bytes(self, cmd, data):
        self._bus.write_block_data(self.addr, cmd, data)
        sleep(0.0001)

# lcd driver
class lcd:
    def __init__(self, i2c_addr=LCD_ADDRESS, port=1):
        """
        Init LCD class and panel
        :param i2c_addr: i2c address
        :type i2c_addr: int
        """
        self._bus = i2c(i2c_addr, port)

        # backlight state
        self._back_light = True

        # init display
        self.__write_cmd(0x03)
        self.__write_cmd(0x03)
        self.__write_cmd(0x03)
        self.__write_cmd(0x02)
        # 4bits mode - seems the only way to go with i2c
        # use 2 lines mode even for 20x4 lines display
        self.__write_cmd(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.__write_cmd(LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF)
        self.__write_cmd(LCD_CLEARDISPLAY)
        self.__write_cmd(LCD_ENTRYMODESET | LCD_ENTRYLEFT)

        sleep(.2)

    # internal command
    def __strobe(self, data):
        """
        Clocks En pin to latch current command
        :param data:
        :return:
        """
        # (re)set back light
        data |= LCD_BACKLIGHT if self._back_light else LCD_NOBACKLIGHT
        # clock data with a pulse on En pin
        self._bus.write_byte(data | En)
        sleep(.0005)
        self._bus.write_byte(data & ~En)
        sleep(.0001)

    # internal command
    def __write_cmd(self, cmd):
        """
        Write a command to LCD panel
        :param cmd: value of command byte
        :type cmd: int
        """
        self.__strobe(cmd & 0xF0)
        self.__strobe((cmd << 4) & 0xF0)

    # internal command
    def __write_char(self, char_value):
        """
        Write a char to LCD panel or character ROM
        :param char_value: value of char
        :type char_value: int
        """
        self.__strobe(Rs | (char_value & 0xF0))
        self.__strobe(Rs | ((char_value << 4) & 0xF0))

    ##
    ## PUBLIC API
    ##

    def message(self, string, row = 0):
        """
        Send string to LCD panel to display it
        :param string: string to display
        :type string: str
        :param row: row id (default is 0) 
        :type row: int
        """
        # set max row
        if row > 3:
            row = 3

        addr = LCD_ROW_OFFSET[row]
        self.__write_cmd(addr)

        for char in string:
            self.__write_char(ord(char))

    def home(self):
        """
        Home the cursor
        """
        self.__write_cmd(LCD_RETURNHOME)

    def clear(self):
        """
        Clear LCD and home cursor
        """
        self.__write_cmd(LCD_CLEARDISPLAY)
        self.__write_cmd(LCD_RETURNHOME)

    def set_cursor(self, col=0, row=0):
        """
        Move cursor to col, row
        :param col: column id (default is 0)
        :type col: int
        :param row: row id (default is 0)
        :type row: int
        """
        # set max row
        if row > 3:
            row = 3
        # set location
        self.__write_cmd(LCD_SETDDRAMADDR | (col + LCD_ROW_OFFSET[row]))

    def write(self, string):
        """
        Send string to LCD panel to display it
        at current cursor position (set_cursor)
        :param string: string to display
        :type string: str
        """
        for char in string:
            self.__write_char(ord(char))

    def set_backlight(self, state):
        """
        Define back light state
        :param state: back light status to set
        :type state: bool
        """
        self._back_light = bool(state)
        self._bus.write_byte(LCD_BACKLIGHT if self._back_light else LCD_NOBACKLIGHT)

    def load_custom_char(self, number, font_data):
        """
        Add custom chars (8 max)
        :param font_data:
        :type font_data: array
        """
        # set CGRAM mode
        self.__write_cmd(LCD_SETCGRAMADDR + (8 * number))
        # transfer data to CGRAM
        for char in font_data:
            self.__write_char(char)

# EOF