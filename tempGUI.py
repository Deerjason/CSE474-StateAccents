import os
import tkinter as tk
from pydub import AudioSegment
from tkinter import filedialog
from tkinter import *
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT


root = tk.Tk()
root.geometry("300x100+300+300")
root.title("Accent Detector")
lableOne = Label(root, text="",font = "Times 13",anchor = S,width = 20)

def UploadAction(event=None):
    lableOne.config(text="Processing request",font = "Times 13",anchor = S,width = 20)
    source = filedialog.askopenfilename()
    [Result, P, classNames] = aT.file_classification(source, "model", "randomforest")
    if classNames == -1:
        lableOne.config(text="Error with test sample",font = "Times 13",anchor = S,width = 20)
    else:
        lableOne.config(text= classNames[np.argmax(P)],font = "Times 13",anchor = S,width = 20)
    

button = tk.Button(root,text ="Insert Audio File", fg = "Black",font = "Times 12", command=UploadAction,width = 20)
button.place(x=55, y=10)
lableOne.place(x=55, y=70)
root.mainloop()


       
