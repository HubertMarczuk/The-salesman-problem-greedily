from numpy import sqrt
from random import randint
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)

class Salesman(object):

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x800")
        self.window.title("Problem komiwojażera")
        self.BuildWindow()
        self.window.mainloop()

    def BuildWindow(self):
        field_width = 5

        self.etykietaBokuA = Label(self.window)
        self.etykietaBokuA["text"] = "Podaj liczbę punktów (4-20): "
        self.etykietaBokuA.grid(row=0, column=0, sticky=W)

        self.poleBokuA = Entry(self.window, width=field_width)
        self.poleBokuA.grid(row=0, column=1, sticky=W)

        self.tytul = Label(self.window)
        self.tytul["text"] = ""
        self.tytul.grid(row=1, column=0, sticky=W)

        self.tytul = Label(self.window)
        self.tytul["text"] = "Wprowadź współrzędne punktów:"
        self.tytul.grid(row=2, column=0, sticky=W)

        self.etykietaPunktu = []
        self.etykietaPunktuX = []
        self.polePunktuX = []
        self.etykietaPunktuY = []
        self.polePunktuY = []


        for i in range(20):
            self.etykieta = Label(self.window)
            self.etykieta["text"] = "Współrzędne punktu nr " + str(i+1) +"    "
            self.etykieta.grid(row=i+3, column=0, sticky=W)
            self.etykietaPunktu.append(self.etykieta)

            self.X = Label(self.window)
            self.X["text"] = "X:"
            self.X.grid(row=i+3, column=1, sticky=W)
            self.etykietaPunktuX.append(self.X)

            self.poleX = Entry(self.window, width=field_width)
            self.poleX.grid(row=i+3, column=2, sticky=W)
            self.polePunktuX.append(self.poleX)

            self.Y = Label(self.window)
            self.Y["text"] = "   Y:      "
            self.Y.grid(row=i+3, column=3, sticky=W)
            self.etykietaPunktuY.append(self.Y)

            self.poleY = Entry(self.window, width=field_width)
            self.poleY.grid(row=i+3, column=4, sticky=W)
            self.polePunktuY.append(self.poleY)


def RandomPoints(n):
    x = []
    y = []
    for i in range(n):
        x.append(randint(0, 100))
        y.append(randint(0, 100))
    return x, y

def Sort(edges, x, y):
    for i in range(len(edges)):
        for j in range(len(edges)-1):
            if Distance(x[edges[j][0]], y[edges[j][0]], x[edges[j][1]], y[edges[j][1]]) > Distance(x[edges[j+1][0]], y[edges[j+1][0]], x[edges[j+1][1]], y[edges[j+1][1]]):
                tmp = edges[j]
                edges[j] = edges[j+1]
                edges[j+1] = tmp
    return edges

def Distance(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))

def Condition1(edge, path):
    counter1 = 0
    counter2 = 0
    for i in range(len(path)):
        if path[i][0] == edge[0] or path[i][1] == edge[0]:
            counter1 += 1
        if path[i][0] == edge[1] or path[i][1] == edge[1]:
            counter2 += 1
        if counter1 > 1 or counter2 > 1:
            return False
    return True

def Condition2(edge, path, x):
    visited = [False for i in range(len(x))]
    point = edge[0]
    visited[point] = True
    next = True
    while next:
        next = False
        for i in range(len(path)):
            if path[i][0] == point and visited[path[i][1]] == False:
                if path[i][1] == edge[1] and len(path) < len(x)-1:
                    return False
                point = path[i][1]
                visited[point] = True
                next = True
                break
            if path[i][1] == point and visited[path[i][0]] == False:
                if path[i][0] == edge[1] and len(path) < len(x)-1:
                    return False
                point = path[i][0]
                visited[point] = True
                next = True
                break
    return True

def FindPath(x, y):
    edges = []
    for i in range(len(x)):
        for j in range(i):
            edges.append([j, i])
    print(edges)
    edges = Sort(edges, x, y)
    print(edges)
    path = []
    for i in range(len(edges)):
        if len(path) == len(x):
            break
        if Condition1(edges[i], path) and Condition2(edges[i], path, x):
            path.append(edges[i])
    return path

k = Salesman()
#x, y = RandomPoints(6)
#print(FindPath(x, y))
