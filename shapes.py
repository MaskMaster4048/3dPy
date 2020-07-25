import numpy as np
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, CENTER
class shape:
    def __init__(self, points):
        self.points = points
        self.modelPoints = np.flip(np.rot90(self.points), 0)
        self.updatexy(np.array([[1,0,0],[0,0,1]]))
    def updatexy(self, matrix):
        self.xy = np.rot90(np.flip(matrix*self.points,0),3)
        self.lastMatrix = matrix
    def draw(self, canvas):
        pass
    def translate(self, t):
        for point in self.points:
            point = point+t
        self.modelPoints = np.flip(np.rot90(self.points), 0)
        self.updatexy(self.lastMatrix)
    def init(self):
        pass
class point(shape):
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
