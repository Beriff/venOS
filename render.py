  
import os
import time

os.system("mode con: cols=200 lines=50")
WIDTH = 200
HEIGHT = 50

COLORS = {
    "RESET": "\u001b[0m",
    "RED": "\u001b[31m",
    "BLUE": "\u001b[34m",
    "CYAN": "\u001b[36m",
    "WHITE": "\u001b[37m",
    "YELLOW": "\u001b[33m",
    "GREEN": "\u001b[32m",
    "MAGENTA": "\u001b[35m",
    "BRIGHT_YELLOW": "\u001b[33;1m",
    "BRIGHT_GREEN": "\u001b[32;1m",
    "BRIGHT_BLUE": "\u001b[34;1m",
    "BRIGHT_MAGENTA": "\u001b[35;1m",
    "BRIGHT_CYAN": "\u001b[36;1m",
    "BRIGHT_RED": "\u001b[31;1m",
    "BRIGHT_WHITE": "\u001b[37;1m" #the snow is snowier than before
    }
    
BG_COLORS = {
    "BLACK": "\u001b[40m",
    "RED": "\u001b[41m",
    "GREEN": "\u001b[42m",
    "YELLOW": "\u001b[43m",
    "BLUE": "\u001b[44m",
    "MAGENTA": "\u001b[45m",
    "CYAN": "\u001b[46m",
    "WHITE": "\u001b[47m"
}


class renderObject:
    def __init__(self, symb, col=COLORS["WHITE"]):
        self.col = col
        self.symb = symb

        self.symb = self.col + self.symb + COLORS["RESET"]

_TEST_STATE = []

RO_DEFAULT_WHITE = renderObject("▓", COLORS["WHITE"])
RO_DEFAULT_BLUE = renderObject("▓", COLORS["BLUE"])
RO_DEFAULT_GREEN = renderObject("▓", COLORS["GREEN"])
RO_DEFAULT_RED = renderObject("▓", COLORS["RED"])
RO_DEFAULT_CYAN = renderObject("▓", COLORS["CYAN"])
RO_DEFAULT_YELLOW = renderObject("▓", COLORS["YELLOW"])
RO_DEFAULT_MAGENTA = renderObject("▓", COLORS["MAGENTA"])


def format_list(list_):
    """formats list to 2d list used as state pattern"""
    """can format existing lists or define new 2d list using var = format_list([])"""
    for i in range(0, HEIGHT):
        list_.append([])

    return list_
    
def _DEF_FILL(def_col=RO_DEFAULT_WHITE):
    state = format_list([])
    for i in range(0, len(state)):
        for k in range(0, WIDTH):
            state[i].append(def_col)

    return state

def add_bg(color, bg_col):
    return bg_col + color

NEW_RENDER = format_list([])

_TEST_STATE = _DEF_FILL(RO_DEFAULT_BLUE)



def new_state_render(state):
    """render new state using double buffering"""

    os.system("cls")

    for x in range(0, HEIGHT):
        
        for y in range(0, WIDTH - 1):
            print(state[x][y].symb, end="")

        print("\n", end="")
       

def draw_rectangle(state, y_1, x_1, y_2, x_2, outline_color=COLORS["WHITE"], fill=False, fill_color=COLORS["YELLOW"], outline_symb="▓", fill_symb="▓"):
    """returns a state with a drawn rectangle"""

    y_2 -= 1
    x_2 -= 1

    for i in range(x_1, x_2 + 1):
        state[y_1][i] = renderObject(outline_symb, outline_color)
        state[y_2][i] = renderObject(outline_symb, outline_color)

    for i in range(y_1, y_2):
        state[i][x_1] = renderObject(outline_symb, outline_color)
        state[i][x_2] = renderObject(outline_symb, outline_color)

    if fill:
        for i in range(y_1 + 1, y_2):
            for k in range(x_1 + 1, x_2):
                state[i][k] = renderObject(fill_symb, fill_color)

    return state

def draw_point(state, x, y, col=COLORS["WHITE"], symb="▓"):
    """returns a state with a placed point"""

    state[y][x] = renderObject(symb, col)

    return state

def draw_line(state, x1, y1, x2, y2, col=COLORS["WHITE"]):
    """uses bresenham algorithm to draw line"""


    m_new = 2 * (y2 - y1)  
    slope_error_new = m_new - (x2 - x1) 
  
    y = y1 
    for x in range(x1, x2 + 1):  
      
        draw_point(state, x, y, col)
 
        slope_error_new =slope_error_new + m_new  
  
        if (slope_error_new >= 0):  
            y= y + 1
            slope_error_new = slope_error_new - 2 * (x2 - x1)  

    return state

def draw_text(state, text, x, y, col=COLORS["WHITE"]):
    for i in range(0, len(text)):
        state[y][x + i] = renderObject(text[i], col) 

    return state

def draw_progress_bar(state, x, y, fractions, width, empty_cell, fill_cell, progress):
    for i in range(0, width):
        state[y][x + i] = empty_cell

    for i in range(0, progress):
        for k in range(0, fractions):
            state[y][x + i + k] = fill_cell

    return state
