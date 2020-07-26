from tkinter import Tk, mainloop
import window3d as w3d
import numpy as np
master = Tk()
master.title('3d window')
w = w3d.screen(100,100)
p1=w3d.point([15,40,30])
p2=w3d.point([25,10,25])
w.addshape(p1)
w.addshape(p2)
w.addshape(w3d.line([p1.getPoint(), p2.getPoint()]))
w.reloadGraphics()
mainloop()
