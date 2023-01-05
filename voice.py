import pyttsx3
import subprocess
import os
from datetime import datetime

path = 'data' # path to mp3, ogg files
file_age = 30
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-80) # voice rate
engine.setProperty('voice', voices[1].id) #chose voice by id, voice_sound = "TTS_MS_EN-US_ZIRA_11.0"

def text_to_file(text): # text to .mp3 then convert to .ogg, delete files older 30 sec
    now = int(datetime.now().strftime("%Y%m%d%H%M%S%f"))
    mp3_file_name = f'{path}/mp3_{now}.mp3'
    ogg_file_name = f'{path}/ogg_{now}.ogg'
    engine.save_to_file(text , mp3_file_name)
    engine.runAndWait()
    subprocess.run(["ffmpeg", '-i', mp3_file_name, '-acodec', 'libopus', ogg_file_name, '-y'])
    #delete files older then filename_age in millisec
    for filename in os.listdir(path):
        filename_age = int(datetime.fromtimestamp(os.stat(os.path.join(path, filename)).st_mtime).strftime("%Y%m%d%H%M%S%f"))
        if filename_age < now - file_age * 1000000: # file_age * 1000000 convert second to microsecond (%f in time presentation) 
            if os.path.isfile(os.path.join(path, filename)):
                print(f'file deleted - {filename} age in seconds {(now-filename_age)/1000000} ')
                os.remove(os.path.join(path, filename))
    return ogg_file_name