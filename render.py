import os
import enum

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
NEW_RENDER = []

_TEST_STATE = []

DEF_WHITE = renderObject("▓", COLORS["WHITE"])
DEF_BLUE = renderObject("▓", COLORS["BLUE"])

def _DEF_FILL(state, def_col=DEF_WHITE):
    for i in range(0, WIDTH * HEIGHT):
        state.append(def_col)

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
    
    for i in range(0, len(BUFFER_1)):
        if BUFFER_1[i] != BUFFER_2[i]:
            NEW_RENDER.append(BUFFER_1[i])
        else:
            NEW_RENDER.append(False)

    for i in range(0, len(NEW_RENDER)):
        if NEW_RENDER[i]:
            print(NEW_RENDER[i].symb, end="")
        else:
            print(BUFFER_2[i].symb, end="")

    BUFFER_2 = BUFFER_1
    BUFFER_1 = []





