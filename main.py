from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import vlc_player_lib
from str_to_num import str_to_num
import math_module
import os

model = Model(r"/home/abraham/Documents/scripts/Lauros/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

#creating speech engine
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", rate-0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
for voice in voices:
    if voice.name == "english":
        engine.setProperty("voice", voice.id)
#for voice in voices:
#    if 'female' in voice.gender.lower():
#        engine.setProperty('voice', voice.id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def loop():
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text = text[14:-3]
        print(text)
        if text.split(" ")[0] + " " + text.split(" ")[1] == "system command" if len(text.split(" ")) > 2 else None:
            text = text.replace("system command ", "")
            #start of if/elif command blocks
            if 'who is ' in text:
                person = text.replace('who is ', '')
                info = wikipedia.summary(person, 1)
                return info
            elif "what is " in text:
                person = text.replace('who is ', '')
                info = wikipedia.summary(person, 1)
                return info
            elif 'play on you tube ' in text:
                song = text.replace('play on you tube ', '')
                return 'playing ' + song
                pywhatkit.playonyt(song)
            if 'time ' in text:
                time = datetime.datetime.now().strftime('%I:%M %p')
                return 'Current time is ' + time
            elif 'date' in text:
                talk('sorry, I have a headache')
            elif 'are you single' in text:
                return 'I am in a relationship with wifi'
            elif 'joke' in text:
                return pyjokes.get_joke()
            #code for VLC player
            for each_key in vlc_player_lib.action_dict.keys():
                if each_key in text:
                    player_command = str_to_num(text)
                    output = vlc_player_lib.vlc_player(player_command)
                    return output
            #code for the math module
            for each_key in math_module.operators.keys():
                if each_key in text:
                    equation = str_to_num(text)
                    answer = math_module.math_module(equation)
                    return answer
            if "abort process " in text:
                text = text.replace('abort process ', '')
                if "exit level one" in text:
                    quit()
                elif "exit level two" in text:
                    os.system("sudo reboot")
                elif "exit level three" in text:
                    os.system("sudo shutdown now")
            else:
                return 'Please say the command again'
                

                
if __name__ == '__main__':
    while True:
        try:
            output = loop()
            if output:
                print(output)
                talk(output)
        except Exception as e:
            print(f"\033[31m--ERROR--\n{e}\033[0m")
#end
