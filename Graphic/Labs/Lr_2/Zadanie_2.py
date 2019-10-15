import turtle
import time
from tkinter import *

def draw_triangle_1(ttl,color,size,x,y):

    ttl.color(str(color))

    ttl.penup()
    ttl.setpos(x, y)
    ttl.pendown()

    ttl.goto(x + size/2, y+size)


def draw_triangle_2(ttl,color,size,x,y):

    ttl.color(str(color))

    ttl.penup()
    ttl.setpos(x+size/2, y+size)
    ttl.pendown()

    ttl.goto(x + size, y)

def draw_triangle_3(ttl,color,size,x,y):

    ttl.color(str(color))

    ttl.penup()
    ttl.setpos(x, y)
    ttl.pendown()

    ttl.goto(x + size, y)



def drawing(x,y,z):

    turtle.tracer(0, 0)
    turtle.hideturtle()

    ttl = turtle.Turtle()
    ttl.hideturtle()
    while True:
        time.sleep(0.2)
        ttl.clear()

        draw_triangle_1(ttl, 'black', z, x, y)
        draw_triangle_2(ttl, 'red', z, x, y)
        draw_triangle_3(ttl, 'blue', z, x, y)

        turtle.update()


def Enter_coords():

    x = EntryX.get()
    x = float(x)

    y = EntryY.get()
    y = float(y)

    z = EntryZ.get()
    z = float(z)

    drawing(x,y,z)


root = Tk()
root.geometry("900x900")
root.title('Треугольник')


Label(root, text='Enter X:').pack()
EntryX = Entry(root, width=10, font='Arial 16')
EntryX.pack()

Label(root, text='Enter Y:').pack()
EntryY = Entry(root, width=10, font='Arial 16')
EntryY.pack()

Label(root, text='Enter Lenth:').pack()
EntryZ = Entry(root, width=10, font='Arial 16')
EntryZ.pack()

but = Button(root, text='Отрисовать')
but = Button(root, text='Отрисовать',command = Enter_coords)
but.pack()

root.mainloop()
