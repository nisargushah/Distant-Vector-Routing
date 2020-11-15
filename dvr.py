#This is a placeholder
from tkinter import Tk
import tkinter as tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

FONT = ("Times New Roman", 12)


class window(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame2 = FileSelect(container, self)
        self.frames [FileSelect] = frame2
        frame2.grid(row=0,column=0,sticky="nsew")

        frame = HomePage(container,self)
        self.frames[HomePage] = frame
        frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Welcome", font=FONT)

        label.pack(pady=10,padx=10)

        btn = tk.Button(self, text="Open input file here", command = lambda:controller.show_frame(FileSelect))

        btn.pack()


class FileSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Please Select an input file", font=FONT)
        label.pack(pady=10,padx=10)
        filename = askopenfilename()
        file_content(filename)

def file_content(filename):
    f = open(filename, 'r')
    Lines = f.readlines()

    data = [lines.split() for lines in Lines]
    print(data)
    g = Graph(len(data))

    g = Graph(len(data))
    for d in data:
        g.addEdge(int(d[0]),int(d[1]),int(d[2]))
    for i in range(len(data)-1):
        g.BellmanFord(i+1)

class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.graph.append([v, u, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(1,self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src):
        dist = [16] * self.V
        dist[src] = 0
        for _ in range(1,self.V):
            dist_copy = dist[:]
            for u, v, w in self.graph:
                if dist[u] != 16 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    print(dist[1:], src)
            if dist == dist_copy:
                break

        # print all distance
        self.printArr(dist)


app = window()
app.mainloop()



"""
References :

https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
"""
