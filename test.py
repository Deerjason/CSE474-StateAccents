"""
 Testing audio samples should be placed in the "test" directory as such:
 > test
   > Midwest
       > Illinois
           Illinois 1.wav
           Illinois 2.wav
       > Indiana
           Indiana 1.wav
   > Northeast
       > Connecticut
           Connecticut 1.wav
"""
import os
import shutil
import glob
import numpy as np
from pyAudioAnalysis import audioTrainTest as aT
from os import listdir
from os.path import isfile, join

pathtemp = "tempTest"
pathOfTest = "test"
# Moves all files to temporary directory
os.mkdir(pathtemp)
regions = [f.name for f in os.scandir(pathOfTest) if f.is_dir()]
for region in regions:
    tempregion = pathOfTest +"/" + region
    states = [f.name for f in os.scandir(tempregion) if f.is_dir()]
    os.mkdir(pathtemp + "/" +region)
    for state in states:
        tempstate = join(pathOfTest,region,state)
        paths = os.listdir(tempstate)
        for path in paths:    
            try:             
                source = join(pathOfTest,region,state,path)
                destination = join(pathtemp,region)
                shutil.move(source, destination)    
            except Exception:
                pass
          

# Classifies all testing data and gets accuracy rate
correct = 0
totalTested = 0
regions =  [f.name for f in os.scandir(pathtemp) if f.is_dir()]
for region in regions:
    tempstate = join(pathtemp,region)
    paths = os.listdir(tempstate)
    for path in paths:
        source = join(pathtemp,region,path)       
        [Result, P, classNames] = aT.file_classification(source, "model", "randomforest")
        if classNames == -1:
            print(path)
        elif classNames[np.argmax(P)] == region:
            correct = correct + 1
        totalTested = totalTested + 1

# Moves all files back to original directory


# Removes temporary directory

# Prints resulting accuracy rate
print("Accuracy: " + str(correct/totalTested * 100) + "%")