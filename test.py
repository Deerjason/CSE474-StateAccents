from pyAudioAnalysis import audioTrainTest as aT

# Replace "testing.wav" with the path of the testing .wav file
Result, P, classNames = aT.file_classification("testing.wav", "model", "randomforest")

# Prints all states with a probability >= 0.2
states = []

for index in range(len(classNames)):
    if P[index] >= 0.2:
        states.append(index)

for state in states:
    print(classNames[state] + ": " + str(P[state]))
