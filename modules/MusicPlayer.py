# Module to Play Musics
from vlc import MediaPlayer
import os
import random
import time

current_this_file_location = os.path.dirname(__file__)
musics_txt_file_location = os.path.join(current_this_file_location, '..\\Data')
# Collecting Data
def generateMusicDirectory(**kargs):
    userprofile = os.environ.get('USERPROFILE')
    directoryMusic = os.path.join(userprofile, "Music")
    data_location = kargs.get('path', directoryMusic)
    try:
        file = open(f"{musics_txt_file_location}\\musics.txt", "w")
        walkedDir = os.walk(data_location)
        for root, _, contents in walkedDir:
            for item in contents:
                if item.endswith('.mp3') or item.endswith('.m4a'):
                    file.write(root+"\\"+item+"\n")
        file.close()
        return True
    except FileNotFoundError:
        return False
# Getting MediaURL
def chooseMusics(args):
    try:
        file = open(f'{musics_txt_file_location}\\musics.txt', 'r')
        lines = file.readlines()
        randomInteger = random.randint(0, len(lines) - 1)
        selected = str(lines[randomInteger]).replace('\n', '')
        if args == 'name':
            return selected
        elif args == 'number':
            return randomInteger
        elif args == 'list':
            return lines
        else:
            return "{}*{}".format(selected, randomInteger)
    except FileNotFoundError:
        return 'file-not-found'

# Creating Main Module
class MusicPlayer():
    def __init__(self):
        self.data_list = str(chooseMusics('')).split('*')
        self.music = self.data_list[0]
        self.part_music = str(self.music).split('\\')[-1]
        self.data = MediaPlayer(self.music)
        self.constant = 0
    def running(self):
        "This will Returns Boolen True if Audio is being Played else returns False"
        if self.data.is_playing() == 0:
            return False
        else:
            return True
    def play(self):
        "This will Play Loaded Audio"
        self.data.play()
        time.sleep(1)
        return f"{self.part_music} is being played"
    def pause(self):
        "This will Paused the currently Playing Audio"
        self.data.pause()
        return "Music Has been Paused"
    def stop(self):
        self.data.stop()
        return "Music is Stopped"
    def change(self):
        data = "Changing From {}".format(self.music)
        self.music = str(chooseMusics('')).split('*')[0]
        data += " to {}".format(self.music)
        self.data.stop()
        self.data = MediaPlayer(self.music)
        self.data.play()
        time.sleep(0.5)
        return data
    def next(self):
        list_music = chooseMusics('list')
        if int(self.constant) + 1 >= len(list_music)-1:
            self.constant = len(list_music) - 1
        else:
            self.constant += 1
        self.music = str(list_music[self.constant]).replace('\n', '')
        self.data.stop()
        self.data = MediaPlayer(self.music)
        self.data.play()
        time.sleep(0.5)
        return "Changed to {}".format(self.music)
    def prev(self):
        list_music = chooseMusics('list')
        if int(self.constant) - 1 <= 0:
            self.constant = 0
        else:
            self.constant = self.constant - 1
        self.music = str(list_music[self.constant]).replace('\n', '')
        self.data.stop()
        self.data = MediaPlayer(self.music)
        self.data.play()
        time.sleep(0.5)
        return "Changed to {}".format(self.music)
    def volume(self, arg):
        if str(arg) == 'max':
            self.data.audio_set_volume(100)
            return "Volume is set to 0"
        elif str(arg) == 'min':
            self.data.audio_set_volume(0)
            return 'Volume is set to 0'
        else:
            vol = self.data.audio_get_volume()
            if int(arg) < 0 or int(arg) > 100:
                return 'input-error'
            else:
                self.data.audio_set_volume(int(arg))
                return "Changing Volume from {} to {}".format(vol, arg)
    def up_volume(self):
        vol = int(self.data.audio_get_volume()) + 3
        if vol > 100:
            vol = 100
        else:
            vol = vol
        self.data.audio_set_volume(vol)
        return "Increasing Volume by 3"
    def down_volume(self):
        vol = int(self.data.audio_get_volume()) - 3
        if vol < 0:
            vol = 0
        else:
            vol = vol
        self.data.audio_set_volume(vol)
        return "Decreasing Volume by 3"
    def muteUnmute(self):
        status = self.data.audio_get_mute()
        self.data.audio_toggle_mute()
        if status == 0:
            return "Muting the Audio"
        else:
            return "UnMuting Audio"

generateMusicDirectory()
