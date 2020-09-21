import render
selection = render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["WHITE"])

def draw_folder(state, x, y, text, selected = False, bg_col = render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["BLUE"])):
    state = render.draw_point(state, x + 3, y, render.add_bg(render.COLORS["YELLOW"], render.BG_COLORS["YELLOW"]))
    state = render.draw_point(state, x + 4, y, render.add_bg(render.COLORS["YELLOW"], render.BG_COLORS["YELLOW"]))
    state = render.draw_point(state, x + 5, y, render.add_bg(render.COLORS["YELLOW"], render.BG_COLORS["YELLOW"]))
    state = render.draw_rectangle(state, y + 1, x, y + 4, x + 6, render.add_bg(render.COLORS["YELLOW"], render.BG_COLORS["YELLOW"]), True, render.add_bg(render.COLORS["YELLOW"], render.BG_COLORS["YELLOW"]))

    state = render.draw_text(state, text, x, y + 4, bg_col)

    if selected:
        state = render.draw_rectangle(state, x - 2, y - 2, x + 6, y + 8, selection)

    return state

def draw_file(state, x, y, text, selected = False, bg_col = render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["BLUE"])):
    if len(text) > 10:
        for i in range(8, 10):
            if i <= 10:
                text[i] = "."
            else:
                text[i] = ""
        



    state = render.draw_rectangle(state, x, y, x + 4, y + 6, render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["WHITE"]), True, render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["WHITE"]))

    state = render.draw_text(state, text, x, y - 6, bg_col)

    return state
