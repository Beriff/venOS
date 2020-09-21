import filesystem as fs
import render
import time
import std_graphics as stdg

def loading_screen_render(progress, task):
    loading_screen = render._DEF_FILL(render.renderObject("▓", render.add_bg(render.COLORS["BLUE"], render.BG_COLORS["BLUE"])))
    loading_screen = render.draw_text(loading_screen, "loading venOS...", 85, 20, render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["BLUE"]))
    loading_screen = render.draw_progress_bar(loading_screen, 70, 25, 5, 50, render.renderObject("▓", render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["WHITE"])), render.renderObject("▓", render.add_bg(render.COLORS["GREEN"], render.BG_COLORS["GREEN"])), progress)
    loading_screen = render.draw_text(loading_screen, task, 85, 27, render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["BLUE"]))
    render.new_state_render(loading_screen)


#loading files

loading_screen_render(1, "loading files")

venos_root = fs.create_folder("venos", 0)
desktop = fs.create_folder("desktop", venos_root)
launch_log = fs.create_file("launch", "log", "launched", desktop)
system = fs.create_folder("system", venos_root)

data = fs.create_folder("sysdata", system)

if True:

    layout = fs.create_file("layout", "sys", "ENG", data)


# loading interface

loading_screen_render(10, "loading interface")
wallpaper = render.add_bg(render.COLORS["BLUE"], render.BG_COLORS["BLUE"])

main_screen = render._DEF_FILL(render.renderObject("▓", wallpaper))
main_screen = render.draw_rectangle(main_screen, render.HEIGHT - 5, 0, render.HEIGHT, render.WIDTH, render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["WHITE"]), True, render.add_bg(render.COLORS["WHITE"], render.BG_COLORS["WHITE"]))

main_screen = stdg.draw_folder(main_screen, 5, 5, "ur mom")
main_screen = stdg.draw_file(main_screen, 5, 30, "polytoria database")

render.new_state_render(main_screen)
#loading nav tables


input()