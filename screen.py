from tkinter import Tk, Frame, Canvas, ALL
import numpy as np
class screen(Canvas):
    def __init__(self, x, y):
       super().__init__(width=x, height=y, background="white")
       self.items=[]
       self.viewingMatrix=np.array([[1,0,0],[0,0,1]])
       self.pack()
    def reloadGraphics(self):
        self.delete(ALL)
        for shape in self.items:
            shape.draw(self)
    def addshape(self, shape):
        shape.init()
        self.items.append(shape)
        self.reloadGraphics()

