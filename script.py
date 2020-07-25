from tkinter import Tk, mainloop
import window3d as w3d
import numpy as np
master = Tk()
w = w3d.screen(100,100)
p1=w3d.point([30,40,80])
p2=w3d.point([60,10,30])
w.addshape(p1)
w.addshape(p2)
w.addshape(w3d.line([p1.getPoint(), p2.getPoint()]))
mainloop()
