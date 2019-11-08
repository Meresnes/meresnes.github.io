import matplotlib.pyplot as plt
import numpy as np


def draw_graph(A,B,C,xmin,xmax,ymin, ymax):
    x = 3
    y = A*x^2 + B*x + C
    print(y)
    fig, ax = plt.subplots()
    plt.plot(x, y)
    plt.show()
    ax.plot(x, y, color="blue", label="голубая линия")

    plt.plot(x, y, 'r--')
    plt.xlim((xmin, xmax))
    plt.ylim((ymin, ymax))
    plt.show()
draw_graph(2,2,2,1,5,1,5)



