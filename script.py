from tkinter import Tk, mainloop
import window3d as w3d
import numpy as np
import time
master = Tk()
master.title('3d window')
w = w3d.screen(200,200)
p1=w3d.point([-35, -40, -25])
p2=w3d.point([25,10,25])
#w.addshape(p1)
#w.addshape(p2)
w.addshape(w3d.rect([p1.getPoint(), p2.getPoint()]))
w.addshape(w3d.point([0,0,0]))
w.addshape(w3d.point([50,0,0]))
w.addshape(w3d.point([0,0,50]))
w.addshape(w3d.point([50,50,50]))
#w.rotX(30)
def turn():
    w.rotZ(1)
    w.rotX(1)
    w.rotY(1)
w.startAnimate(30, turn, 360)
w.reloadGraphics()
mainloop()
