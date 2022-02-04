from gtts import gTTS
import os

#myText = "You are using text To Speech Engine in English using python"
read_file = open("SampleText.txt", "r")
myText = read_file.read().replace("\n"," ")
language = 'en'

output = gTTS(text = myText, lang = language, slow = False)

output.save("output.mp3")
read_file.close()

os.system("start output.mp3")

