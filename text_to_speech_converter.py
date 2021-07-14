'''
    File name: text_to_speech_converter.py
    Author: Software Samsaaram
    Date created: 15/07/2021
    Date last modified: 15/07/2021
    Python Version: 3.9.0
    Description: This python program converts given input text into Audio
'''
from gtts import gTTS
from playsound import playsound

def main():
    output = 'output_audio.mp3' #Output Audio File Name. You can change the name and location if you want
    language = 'en' #Speech language: English
    text_to_convert = "30 Thousand.Ante nalabhai velu" #This is the text you want to convert to Audio
    sp = gTTS(text_to_convert,
              lang=language,
              slow=False)
    sp.save(output) #Save the Output Audio as File
    playsound(output) #Play the Audio file

if __name__ == "__main__":
    main()
