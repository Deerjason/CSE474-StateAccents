import os
import tkinter as tk
from pydub import AudioSegment
from tkinter import filedialog
from tkinter import *
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT


root = tk.Tk()
lableOne = Label(root, text="Waiting for test sample")

def UploadAction(event=None):
    lableOne.config(text="Processing request")
    source = filedialog.askopenfilename()
    [Result, P, classNames] = aT.file_classification(source, "model", "randomforest")
    if classNames == -1:
        lableOne.config(text="Error with test sample")
    else:
        lableOne.config(text= classNames[np.argmax(P)])
    

button = tk.Button(root,text ="insert pack", fg = "Black", command=UploadAction)
button.pack()
lableOne.pack()
root.mainloop()


       
