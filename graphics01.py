from tkinter import Tk, Frame, Canvas
import numpy as np
import shapes as sh
import screen as s
#w = s.screen(100,100)
#w.addshape(sh.point(np.array([[50,10,80]])))
def getw():
    return w
class window(Frame):
    def __init__(self):
        super().__init__()
        self.master.title('3d window')
        self.board = s.screen(100,100)
        self.pack()
def main():
    root = Tk()
#    root.withdraw()
    nib = window()
    root.mainloop()
if __name__ == '__main__':
    main()
