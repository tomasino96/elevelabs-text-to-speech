import elevenlabs
from elevenlabs import set_api_key
import os

set_api_key("YourAPIKeyHere")

input_text = input("Enter text here: ")

audio = elevenlabs.generate(text = input_text, voice = "Adam", model="eleven_multilingual_v2") #Define your voice parameters

elevenlabs.save(audio, "speech.mp3") #Save your text to speech as mp3 file

os.system('start speech.mp3') #Starts your audio file