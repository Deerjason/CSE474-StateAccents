import os
from pyAudioAnalysis import audioTrainTest as aT

# The .wav file to be tested should be placed in the "test" directory as such:
# > test
#   Arizona.wav
data = [wav for wav in os.listdir("test")]

# Classifies .wav file using existing randomforest model
Result, P, classNames = aT.file_classification(data[0], "model", "randomforest")

# Prints all states with a probability >= 0.2
states = []

for index in range(len(classNames)):
    if P[index] >= 0.2:
        states.append(index)

for state in states:
    print(classNames[state] + ": " + str(P[state]))
