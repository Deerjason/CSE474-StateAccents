import numpy as np
from pyAudioAnalysis import audioTrainTest as aT

# Replace "testing/alaska.wav" with the path of the testing .wav file
Result, P, classNames = aT.file_classification("testing/alaska.wav", "model", "randomforest")
winner = np.argmax(P)

# 0.7 is the desired threshold for classifying an accent (change as desired)
if P[winner] > 0.7:
    print("State: " + classNames[winner] + ", with probability: " + str(P[winner]))
else :
    print("Can't classify accent: " + str(P))