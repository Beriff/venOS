import os

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
    "MAGENTA": "\u001b[35m"

    }



class renderObject:
    def __init__(self, symb, col=COLORS["WHITE"]):
        self.col = col
        self.symb = symb

        self.symb = self.col + self.symb + COLORS["RESET"]

BUFFER_1 = []
BUFFER_2 = []
INIT_STATE = []

_TEST_STATE = []

DEF_WHITE = renderObject("▓", COLORS["WHITE"])
DEF_BLUE = renderObject("▓", COLORS["BLUE"])

def _DEF_FILL(state, def_col=DEF_WHITE):
    for i in range(0, HEIGHT):
        state.append([])
        for k in range(0, WIDTH):
            state[i].append(def_col)

def format_list(list_):
    """formats list to 2d list used as state pattern"""
    """can format existing lists or define new 2d list using var = format_list([])"""
    for i in range(0, HEIGHT):
        list_.append([])

    return list_

NEW_RENDER = format_list([])



_DEF_FILL(INIT_STATE)
_DEF_FILL(_TEST_STATE, DEF_BLUE)



def new_state_render(state):
    """render new state using double buffering"""
    global BUFFER_1
    global BUFFER_2
    global INIT_STATE
    global NEW_RENDER

    BUFFER_1 = state
    if not BUFFER_2:
        BUFFER_2 = INIT_STATE
    
    for x in range(0, len(BUFFER_1)):
        for y in range(0, len(BUFFER_1[0])):
            if BUFFER_1[x][y] != BUFFER_2[x][y]:
                NEW_RENDER[x].append(BUFFER_1[x][y])
            else:
                NEW_RENDER[x].append(False)

    for x in range(0, len(NEW_RENDER)):
        for y in range(0, len(NEW_RENDER[0])):
            if NEW_RENDER[x][y]:
                print(NEW_RENDER[x][y].symb, end="")
            else:
                print(BUFFER_2[x][y].symb, end="")

    BUFFER_2 = BUFFER_1
    BUFFER_1 = []
