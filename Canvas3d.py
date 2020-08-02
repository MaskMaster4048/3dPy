import numpy as np
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, CENTER
from collections import deque
import math
import time
import threading #TODO delete later
import time #TODO delete later
class shape:
    def __init__(self, points):
        self.subItems=[]
        self.points = np.array(points)
        self.modelPoints = np.flip(np.rot90(self.points), 0)
        self.updatexy(np.array([[1,0,0],[0,0,1]]),np.array([[0,0]]))
    def updatexy(self, sm, tm):
        self.xy = np.rot90(np.flip(sm.dot(self.modelPoints)+np.flip(np.rot90(tm),0),0),3)
        self.lastSM = sm
        self.lastTM = tm
        for i in self.subItems:
            i.updatexy(sm,tm)
    def draw(self, canvas):
        pass
    def translate(self, t):
        for point in self.points:
            point = point+t
        self.modelPoints = np.flip(np.rot90(self.points), 0)
        self.updatexy(self.lastSM, self.lastTM)
        for i in self.subItems:
            i.translate(t)
class point(shape):
    def __init__(self, point):
        super().__init__([point])
        self.img = ImageTk.PhotoImage(Image.open("dot.jpg"))
    def draw(self, canvas):
        canvas.create_image(self.xy[0][0], self.xy[0][1], image=self.img,
                anchor=CENTER)
    def getPoint(self):
        return self.points[0]
class line(shape):
    def draw(self, canvas):
        canvas.create_line(self.xy[0][0], self.xy[0][1], self.xy[1][0], self.xy[1][1])
class rect(shape):
    def __init__(self, points):
        super().__init__(points)
        for i in range(2):
            for j in range(2):
                self.subItems.append(line([
                    [points[i][0], points[j][1], points[0][2]],
                    [points[i][0], points[j][1], points[1][2]]]))
                self.subItems.append(line([
                    [points[i][0], points[0][1], points[j][2]],
                    [points[i][0], points[1][1], points[j][2]]]))
                self.subItems.append(line([
                    [points[0][0], points[i][1], points[j][2]],
                    [points[1][0], points[i][1], points[j][2]]]))
    def draw(self, canvas):
        for line in self.subItems:
            line.draw(canvas)

class screen(Canvas):
    def __init__(self, x, y):
       super().__init__(width=x, height=y, background="white")
       self.items=[]
       self.scaleMatrix=np.array([[1,0,0],[0,0,-1]])
       self.transformMatrix=np.array([[x/2,y/2]])
       self.degs=np.array([0,0,0])
       self.animationList=deque()
       self.pack()
    def reloadGraphics(self):
        self.delete(ALL)
        for shape in self.items:
            shape.updatexy(self.scaleMatrix, self.transformMatrix)
            shape.draw(self)
    def addshape(self, shape):
        self.items.append(shape)
    def rotX(self, deg):
        self.degs[0] = (self.degs[0]+deg)%360
        self.remakeMatrix()
    def rotY(self, deg):
        self.degs[1] = (self.degs[1]+deg)%360
        self.remakeMatrix()
    def rotZ(self, deg):
        self.degs[2] = (self.degs[2]+deg)%360
        self.remakeMatrix()
    def remakeMatrix(self):
        def sin(n):
            return math.sin(math.radians(self.degs[n]))
        def cos(n):
            return math.cos(math.radians(self.degs[n]))
        self.scaleMatrix=np.array([
            [ cos(1)*cos(2)-sin(0)*sin(1)*sin(2), -cos(1)*sin(2)-sin(0)*sin(1)*cos(2), -cos(0)*sin(1)],
            [-sin(1)*cos(2)-sin(0)*cos(1)*sin(2),  sin(1)*sin(2)-sin(0)*cos(1)*cos(2), -cos(0)*cos(1)]])
    def addAnimation(self, step, action, ticks):
        self.animationList.append([step, action, ticks])
    def startAnimation(self):
        alist = self.animationList.popleft()
        self.animateVar=True
        self.animateStep=alist[0]
        self.animateAction=alist[1]
        self.ticks=alist[2]
        self.prevDegs=self.degs.copy()
        self.animate()
    def animate(self):
        if self.ticks !=0 and self.animateVar==True:
            self.animateAction(self.ticks)
            self.remakeMatrix()
            self.reloadGraphics()
            self.after(round(1000.0/self.animateStep), self.animate)
            self.ticks -= 1
        else:
            if self.ticks==0 and self.animateVar==True and len(self.animationList)!=0:
                self.startAnimation()
    def stopAnimation(self):
        self.animateVar=False
    def resumeAnimation(self):
        self.animateVar=True
        self.animate()
    def clearAnimation(self):
        self.animationList = deque()
    def resetAnimation(self):
        self.degs=[0,0,0]
        self.remakeMatrix()
    def smoothMoveTo(self, degsN, seconds):
        for i in self.degs:
            if i < 0:
                i+=360
        def smoothMove(e):
            print(time.time())
            multiplier=(math.cos(math.radians(e))+1)*0.5
            for i in range(3):
                self.degs[i]=(
                    self.prevDegs[i]*(-multiplier+1) +
                    degsN[i]        *  multiplier )
        self.addAnimation(180.0/seconds, smoothMove, 180)
    def smoothReset(self, sec):
        self.clearAnimation()
        self.smoothMoveTo([0,0,0], sec)
        self.startAnimation()
