"""
 Training audio samples should be placed in the "train" directory as such:
 > train
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
from os import listdir
from os.path import isfile, join
from pyAudioAnalysis import audioTrainTest as aT

pathtemp = "tempTrain"
pathOfTrain = "train"
# Moves all files to temporary directory
os.mkdir(pathtemp)
regions = [f.name for f in os.scandir(pathOfTrain) if f.is_dir()]
for region in regions:
    tempregion = pathOfTrain +"/" + region
    states = [f.name for f in os.scandir(tempregion) if f.is_dir()]
    os.mkdir(pathtemp + "/" +region)
    for state in states:
        tempstate = join(pathOfTrain,region,state)
        paths = os.listdir(tempstate)
        for path in paths:    
            try:             
                source = join(pathOfTrain,region,state,path)
                destination = join(pathtemp,region)
                shutil.move(source, destination)    
            except Exception:
                pass
          
            
# Gets list of directories to be trained on
dirs = [f.path for f in os.scandir(pathtemp) if f.is_dir()]

print(dirs)

# Trains model using randomforest
aT.extract_features_and_train(dirs, 2.0, 0.2, 0.50, 0.25, "randomforest", "model", False)

# Moves all files back to original directory

# Removes temporary directory
