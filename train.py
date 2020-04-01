from pyAudioAnalysis import audioTrainTest as aT

# Replace ["Arizona", "Alaska"] with a list of state directories to be trained
aT.extract_features_and_train(["Arizona","Alaska"], 1.0, 1.0, 0.1, 0.1, "randomforest", "model", False)
