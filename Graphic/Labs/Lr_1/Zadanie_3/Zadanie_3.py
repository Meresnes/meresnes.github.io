import turtle
import time
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.geometry("1200x900")
root.title('График')

def draw_graph(A,B,C,xmin,xmax,ymin, ymax):
    x = 3
    y = A*x^2 + B*x + C
    fig, ax = plt.subplots()

    ax.plot(x, y, color="blue", label="голубая линия")

    plt.plot(x, y, 'r--')
    plt.xlim((xmin, xmax))
    plt.ylim((ymin, ymax))
    plt.show()



def Enter_coords():

    a = EntryA.get()
    a = float(a)

    b = EntryB.get()
    b = float(a)

    c = EntryC.get()
    c = float(c)

    x_min = Entry_x_min.get()
    x_min = float(x_min)

    y_min = Entry_y_min.get()
    y_min = float(y_min)

    x_max = Entry_x_max.get()
    x_max = float(x_max)

    y_max = Entry_y_max.get()
    y_max = float(y_max)

    draw_graph(a,b,c,xmin,xmax,ymin, ymax)

Label(root, text='Enter A:').pack()
EntryA = Entry(root, width=10, font='Arial 16')
EntryA.pack()

Label(root, text='Enter B:').pack()
EntryB = Entry(root, width=10, font='Arial 16')
EntryB.pack()

Label(root, text='Enter C:').pack()
EntryC = Entry(root, width=10, font='Arial 16')
EntryC.pack()

Label(root, text='Enter x min:').pack()
Entry_x_min = Entry(root, width=10, font='Arial 16')
Entry_x_min.pack()

Label(root, text='Enter y min:').pack()
Entry_y_min = Entry(root, width=10, font='Arial 16')
Entry_y_min.pack()

Label(root, text='Enter x max:').pack()
Entry_x_max = Entry(root, width=10, font='Arial 16')
Entry_x_max.pack()

Label(root, text='Enter y max:').pack()
Entry_y_max = Entry(root, width=10, font='Arial 16')
Entry_y_max.pack()

but = Button(root, text='Отрисовать')
but = Button(root, text='Отрисовать',command = Enter_coords)
but.pack()

root.mainloop()
