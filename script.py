from tkinter import Tk, mainloop
import window3d as w3d
import numpy as np
master = Tk()
w = w3d.screen(100,100)
w.addshape(w3d.point(np.array([[30,40,80]])))
mainloop()
