import speech_recognition as sr
import wave
import os
import contextlib
import sys
from os import path

def function():
    i = 0
    WAV_FILE = path.join(path.dirname(path.realpath(__file__)), sys.argv[1])
    extension = ""
    extension = WAV_FILE.split(".")[-1]
    text_file =("sample.txt","w")
    if (extension != "wav"):
        os.system("avconv -i " + WAV_FILE + "  -vn -f wav temp.wav")
        WAV_FILE  = "temp.wav"
    fname = WAV_FILE
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        end = duration
    r = sr.Recognizer()
    start = 0.0;
    end_time = 4.0;
    while(start != end):
        i+=1
        with sr.WavFile(WAV_FILE) as source:
            audio = r.record(source,end_time, start)
            start += 4.0
            end_time += 4.0
        try:
            print '\n', i,'\n',start," --> ",end_time , r.recognize_google(audio),
        except sr.UnknownValueError:
            print "",
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    os.remove("temp.wav")
    return 0
function()
