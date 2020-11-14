#This is a placeholder
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
f = open(filename, 'r')
Lines = f.readlines()

data = [lines.split() for lines in Lines]










"""
References :

https://stackoverflow.com/questions/3579568/choosing-a-file-in-python-with-simple-dialog

"""
