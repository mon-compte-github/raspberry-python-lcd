
from curses import wrapper, curs_set

def main(stdscr):
    stdscr.clear()
    curs_set(False)

    stdscr.addstr(("+" + "".rjust(20, "-") + "+\n"))
    for k in range(1, 5):
        stdscr.addstr(("|" + "".rjust(20, " ") + "|\n"))
    stdscr.addstr(("+" + "".rjust(20, "-") + "+\n"))

    stdscr.move(1,1)
    stdscr.addstr("coucou")
    
    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)