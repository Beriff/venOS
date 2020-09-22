![GitHub commit activity](https://img.shields.io/github/commit-activity/w/Beriff/venOS?style=flat-square)
![Lines of code](https://img.shields.io/tokei/lines/github/Beriff/venOS?style=flat-square)
![GitHub](https://img.shields.io/github/license/Beriff/venOS?style=flat-square)

# venOS
**venOS** is a graphic shell for own generated filesystem named venFS. For convenience and simplicity it was called an OS. venOS means **v**irtual **en**vironment operating system.

It is planned for venOS to support custom executable files, written in python, as well as opportunity to deploy them to the local store where anyone can download them. venOS should support
multithreading for several windows to run.

One of the main aspects of venOS is a simple API for custom applications, for example:
```python
import windowAPI as wa
import venos_graphic as vg

master = wa.newWindow(600, 800) #initializing new window with given size
master.newTitle("example") #giving title to new window
#newWidget() takes widget name, widget object, x coord, y coord and z-order.
#windowAPI transforms venos_graphic canvas object to window-drawable canvas.
master.newWidget("myCanvas", wa.Canvas(vg.newCanvas(600, 800)), 0, 0, 0) 

def test(): #creating function to put it in the button
  canv = vg.newCanvas(600, 800) #creating new canvas
  canv.drawLine(50, 30, 70, 80, vg.colors["yellow"]) #drawLine() takes x1, y1, x2, y2, color
  
  master.findWidget("myCanvas") = wa.Canvas(canv) #finding widget and assigning new canvas to it


master.newWidget("myButton", wa.Button("click me", test), 50, 50, 1) #creating button widget

#As result, it will draw blank canvas, then a button over it. On button click, it will draw a yellow line.
```

The point of the project is to develop a community of people who are helping with this project by creating new apps / improving source code / creating new libraries and see how far
we can push this and how similar the final project will look to any existing operating systems.

To use the project, head up to the latest release and download the project. venOS is intended to be used in a "raw" form of just a bunch of python files. This way gives more flexible interacting
with venOS.

## Helping the project
I would gladly accept any help, feel free to pull request or fork.
