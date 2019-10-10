import turtle
import time

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


def main():

    turtle.tracer(0, 0)
    turtle.hideturtle()

    ttl = turtle.Turtle()
    ttl.hideturtle()

    x = int(input("Введите X:"))
    y = int(input("Введите Y:"))

    while True:

        time.sleep(0.2)
        ttl.clear()

        draw_triangle_1(ttl,'black',x,x,y)
        draw_triangle_2(ttl,'red',x,x,y)
        draw_triangle_3(ttl,'blue',x,x,y)

        turtle.update()

if __name__ == '__main__':
    main()
