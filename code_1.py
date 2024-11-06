from numpy import sqrt
import numpy as np
from random import randint
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
import matplotlib.patheffects as pe

class Salesman(object):

    def __init__(self):
        self.window = Tk()
        self.window.geometry("750x950")
        self.window.title("Problem komiwojażera")
        self.BuildWindow()
        self.window.mainloop()

    def BuildWindow(self):
        field_width = 5

        self.etiquette1 = Label(self.window)
        self.etiquette1["text"] = "Podaj liczbę punktów (4-20): "
        self.etiquette1.grid(row=0, column=0, sticky=W)

        self.point_number_field = Entry(self.window, width=field_width)
        self.point_number_field.grid(row=0, column=1, sticky=W)

        self.space1 = Label(self.window)
        self.space1["text"] = ""
        self.space1.grid(row=1, column=0, sticky=W)

        self.etiquette2 = Label(self.window)
        self.etiquette2["text"] = "Wprowadź współrzędne punktów (wartości całkowite 0-100):"
        self.etiquette2.grid(row=2, column=0, sticky=W)

        self.point_etiquettes = []
        self.point_etiquettes_x = []
        self.point_field_x = []
        self.point_etiquettes_y = []
        self.point_field_y = []


        for i in range(20):
            self.point_etiquette = Label(self.window)
            self.point_etiquette["text"] = "Współrzędne punktu nr " + str(i+1) +"    "
            self.point_etiquette.grid(row=i+3, column=0, sticky=W)
            self.point_etiquettes.append(self.point_etiquette)

            self.X = Label(self.window)
            self.X["text"] = "X:"
            self.X.grid(row=i+3, column=1, sticky=W)
            self.point_etiquettes_x.append(self.X)

            self.field_x = Entry(self.window, width=field_width)
            self.field_x.grid(row=i+3, column=2, sticky=W)
            self.point_field_x.append(self.field_x)

            self.Y = Label(self.window)
            self.Y["text"] = "   Y:      "
            self.Y.grid(row=i+3, column=3, sticky=W)
            self.point_etiquettes_y.append(self.Y)

            self.field_y = Entry(self.window, width=field_width)
            self.field_y.grid(row=i+3, column=4, sticky=W)
            self.point_field_y.append(self.field_y)

        self.space2 = Label(self.window)
        self.space2["text"] = ""
        self.space2.grid(row=23, column=0, sticky=W)

        self.random_button = Button(self.window, width=15)
        self.random_button["text"] = "Losuj"
        self.random_button["command"] = self.Randomize
        self.random_button.grid(row=24, column=0, sticky=W)

        self.space3 = Label(self.window)
        self.space3["text"] = ""
        self.space3.grid(row=25, column=0, sticky=W)

        self.find_button = Button(self.window, width=15)
        self.find_button["text"] = "Szukaj trasy"
        self.find_button["command"] = self.Find
        self.find_button.grid(row=26, column=0, sticky=W)

        self.space4 = Label(self.window)
        self.space4["text"] = ""
        self.space4.grid(row=27, column=0, sticky=W)

        self.summary = Label(self.window)
        self.summary["text"] = ""
        self.summary.grid(row=28, column=0, sticky=W)

    def Randomize(self):
        x, y = self.RandomPoints(int(float(self.point_number_field.get())))
        for i in range(20):
            self.point_field_x[i].delete(0, END)
            self.point_field_y[i].delete(0, END)
            if i<int(float(self.point_number_field.get())):
                self.point_field_x[i].insert(0, x[i])
                self.point_field_y[i].insert(0, y[i])

    def RandomPoints(self,n):
        x = []
        y = []
        for i in range(n):
            x.append(randint(0, 100))
            y.append(randint(0, 100))
        return x, y
    
    def Find(self):
        x = []
        y = []
        for i in range(int(float(self.point_number_field.get()))):
            x.append(int(float(self.point_field_x[i].get())))
            y.append(int(float(self.point_field_y[i].get())))
        path = self.FindPath(x,y)
        self.summary["text"] = self.CreateText(path, x, y)
        self.Draw(path, x, y)


    def FindPath(self, x, y):
        edges = []
        for i in range(len(x)):
            for j in range(i):
                edges.append([j, i])
        edges = self.Sort(edges, x, y)
        path = []
        for i in range(len(edges)):
            if len(path) == len(x):
                break
            if self.Condition1(edges[i], path) and self.Condition2(edges[i], path, x):
                path.append(edges[i])
        return path

    def Sort(self, edges, x, y):
        for i in range(len(edges)):
            for j in range(len(edges)-1):
                if self.Distance(x[edges[j][0]], y[edges[j][0]], x[edges[j][1]], y[edges[j][1]]) > self.Distance(x[edges[j+1][0]], y[edges[j+1][0]], x[edges[j+1][1]], y[edges[j+1][1]]):
                    tmp = edges[j]
                    edges[j] = edges[j+1]
                    edges[j+1] = tmp
        return edges

    def Distance(self, x1, y1, x2, y2):
        return sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))

    def Condition1(self, edge, path):
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

    def Condition2(self, edge, path, x):
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
    
    def CreateText(self, path, x, y):
        distances = []
        full_distance=0
        for i in range(len(path)):
            tmp = self.Distance(x[path[i][0]], y[path[i][0]], x[path[i][1]], y[path[i][1]])
            full_distance += tmp
            tmp = round(tmp, 2)
            distances.append(tmp)
        full_distance = round(full_distance, 2)
        text = "Trasa wyznaczona. Całkowita długość: " + str(full_distance) +"\n\nWybrane krawędzie:\n"
        for i in range(len(distances)):
            text += "Między punktami " + str(path[i][0]) + " a " + str(path[i][1]) + ". Długość: " + str(distances[i]) + "\n"
        return text
    
    def Draw(self, path, x, y):
        plt.close()
        fig = plt.figure(figsize=(3, 3))
        ax = fig.add_subplot(111)
        ax.axis("square")
        plt.grid(axis='both', which='major',
                 color="black", linestyle=':', linewidth=0.5)
        
        for i in range(len(path)):
            array_x = np.array([x[path[i][0]], x[path[i][1]]])
            array_y = np.array([y[path[i][0]], y[path[i][1]]])
            plt.plot(array_x, array_y, color = "blue", linewidth=2)
        
        for i in range(int(float(self.point_number_field.get()))):
            plt.scatter(x[i], y[i], color = "red", s=20)
            ax.annotate(i+1, [x[i]+1, y[i]+1], color = "white", path_effects = [pe.withStroke(linewidth=2, foreground="black")])

        plt.xlim(-1, 101)
        plt.ylim(-1, 101)

        plot_window = FigureCanvasTkAgg(fig, self.window)
        plot_window.draw()
        plot_window.get_tk_widget().grid(row=28, column=4, sticky=W)


k = Salesman()

