from tkinter import Tk, mainloop, Button
import Canvas3d as c3d
import numpy as np
import time

root = Tk()
root.title('3d Window')
c = c3d.screen(200,200, root)
c.addshape(c3d.rect([[-50,-50,-50],[50,50,50]]))
c.reloadGraphics()

def xn():
    c.rotX(-1)
    c.reloadGraphics()
def xp():
    c.rotX(1)
    c.reloadGraphics()
def yn():
    c.rotY(-1)
    c.reloadGraphics()
def yp():
    c.rotY(1)
    c.reloadGraphics()
def zn():
    c.rotZ(-1)
    c.reloadGraphics()
def zp():
    c.rotZ(1)
    c.reloadGraphics()
def animate():
    def turn():
        c.rotZ(-1)
    c.startAnimate(45, turn, 360)
def keyPress(e):
    key = e.keysym
    if key == 'Up':
        xn()
    if key == 'Down':
        xp()
    if key == 'Prior':
        yp()
    if key == 'Next':
        yn()
    if key == 'Left':
        zn()
    if key == 'Right':
        zp()

b1 = Button(root, text='Stop Animation', width=25, command=c.stopAnimate)
b1.pack()
b2 = Button(root, text='Start Animation', width=25, command=animate)
b2.pack()
root.bind_all('<Key>', keyPress)
root.mainloop()
