from tkinter import Tk, mainloop
import Canvas3d as c3d
import numpy as np
import time
master = Tk()
master.title('3d Canvas')
c = c3d.screen(200,200, master)
p1=c3d.point([-35, -40, -25])
p2=c3d.point([25,10,25])
#c.addshape(p1)
#c.addshape(p2)
c.addshape(c3d.rect([p1.getPoint(), p2.getPoint()]))
c.addshape(c3d.point([0,0,0]))
c.addshape(c3d.point([50,0,0]))
c.addshape(c3d.point([0,0,50]))
c.addshape(c3d.point([50,50,50]))
#c.rotX(30)
def turn():
    c.rotZ(1)
    c.rotX(1)
    c.rotY(1)
c.startAnimate(30, turn, 360)
c.reloadGraphics()
mainloop()
