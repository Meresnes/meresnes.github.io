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



def Draw(x,y,z):

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





root = Tk()
root.geometry("1200x900")
root.title('График')


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
but = Button(root, text='Отрисовать',command = Draw)
but.pack()

root.mainloop()
