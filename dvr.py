"""
Nisarg Shah

10015513132

"""

from tkinter import Tk
import tkinter as tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import time
import tkinter.messagebox as tkmb

FONT = ("Times New Roman", 12)

"""
This fucntion provides an intial frame for our GUI

"""
class window(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = HomePage(container,self)
        self.frames[HomePage] = frame
        frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

"""
This class has our button windows

"""
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Welcome", font=FONT)

        label.pack(pady=10,padx=50)

        button = tk.Button(self, text="Step-by-step output",
                            command=lambda: file_content("input.txt", 1))
        button.pack(pady=10,padx=10)
        button2 = tk.Button(self, text="Without intervention",
                            command=lambda: file_content("input.txt", 0))
        button2.pack(pady=10,padx=10)


"""
This is where we read in the file and
pass the coreect arguments for bellman-ford

"""
def file_content(filename, choice):

    start = time.time()

    f = open(filename, 'r')
    Lines = f.readlines()

    data = [lines.split() for lines in Lines]
    #print(data)
    g = Graph(6)
    for d in data:
        g.addEdge(int(d[0]),int(d[1]),int(d[2]))
    for i in range(len(data)-1):
        g.BellmanFord(i+1, choice)
    end = time.time()
    # print all distance
    info_message = "The total run time for algorithm is "+str(end-start)+" seconds"
    tkmb.showinfo("Output", info_message)


"""

Class for our graph and all the edges.

"""
class Graph:

    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.graph.append([v, u, w])

    # utility function used to print the solution
    def printArr(self, dist,src):
        print("Vertex Distance from node (Final result) "+str(src))
        for i in range(1,self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def BellmanFord(self, src, choice):
        if choice == 1:
            print("Step-by-Step values till it reaches stable state are :")
        dist = [16] * self.V
        dist[src] = 0
        for _ in range(1,self.V):
            dist_copy = dist[:]
            for u, v, w in self.graph:
                if dist[u] != 16 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    if choice == 1:
                        print("{0}\t\t{1}".format(src,dist[1:]))
                        time.sleep(2)

            if dist == dist_copy:
                break

        self.printArr(dist,src)

#Tk.draw()
app = window()
app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
app.mainloop()






"""
References :

https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter

https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

https://www.programiz.com/dsa/bellman-ford-algorithm

https://algotree.org/algorithms/single_source_shortest_path/bellman_ford_shortest_path/

"""
