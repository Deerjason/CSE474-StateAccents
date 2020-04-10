import os
from pyAudioAnalysis import audioTrainTest as aT

# Training audio samples should be placed in the "train" directory as such:
# > train
#   > Arizona
#       Arizona 1.wav
#       Arizona 2.wav
#   > Arkansas
#       Arkansas 1.wav
dirs = ["train/" + directory for directory in os.listdir("train")]

# Trains model using randomforest
aT.extract_features_and_train(dirs, 1.0, 1.0, 0.1, 0.1, "randomforest", "model", False)
