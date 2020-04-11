import os
from pydub import AudioSegment

path = "C:/Users/IIO20160229/Desktop/Buffalo/CSE475/CSE474-StateAccents-develop/raw_data"

outpath = "C:/Users/IIO20160229/Desktop/Buffalo/CSE475/CSE474-StateAccents-develop/processed_data/"

#Change working directory
os.chdir(path)

audio_files = os.listdir()

startSec = 6

# Time to miliseconds
startTime = startSec*1000

# Opening file and extracting segment

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       extract = mp3_sound[startTime:]
       #rename them using the old name + ".wav"
       extract.export(outpath + "{0}.wav".format(name), format="wav", )