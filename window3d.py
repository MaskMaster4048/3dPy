import numpy as np
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, CENTER
class shape:
    def __init__(self, points):
        self.points = np.array(points)
        self.modelPoints = np.flip(np.rot90(self.points), 0)
        self.updatexy(np.array([[1,0,0],[0,0,1]]),np.array([[0,0]]))
    def updatexy(self, sm, tm):
        self.xy = np.rot90(np.flip(sm.dot(self.modelPoints)+np.flip(np.rot90(tm),0),0),3)
        self.lastSM = sm
        self.lastTM = tm
    def draw(self, canvas):
        pass
    def translate(self, t):
        for point in self.points:
            point = point+t
        self.modelPoints = np.flip(np.rot90(self.points), 0)
        self.updatexy(self.lastSM, self.lastTM)
    def init(self):
        pass
class point(shape):
    def __init__(self, point):
        super().__init__([point])
    def draw(self, canvas):
        canvas.create_image(self.xy[0][0], self.xy[0][1], image=self.img,
                anchor=CENTER)
    def getPoint(self):
        return self.points[0]
    def init(self):
        self.img = ImageTk.PhotoImage(Image.open("dot.jpg"))
class line(shape):
    def draw(self, canvas):
        canvas.create_line(self.xy[0][0], self.xy[0][1], self.xy[1][0], self.xy[1][1])

class screen(Canvas):
    def __init__(self, x, y):
       super().__init__(width=x, height=y, background="white")
       self.items=[]
       self.scaleMatrix=np.array([[1,0,0],[0,0,-1]])
       self.transformMatrix=np.array([[x/2,y/2]])
       self.pack()
    def reloadGraphics(self):
        self.delete(ALL)
        for shape in self.items:
            shape.updatexy(self.scaleMatrix, self.transformMatrix)
            shape.draw(self)
    def addshape(self, shape):
        shape.init()
        self.items.append(shape)
#depreciated
class window(Frame):
    def __init__(self,canvas):
        super().__init__()
        self.master.title('3d window')
        self.board = canvas
        self.pack()
def createWindow(canvas):
    root = Tk()
    #nib = window(canvas)
    root.mainloop()
