from pydub import AudioSegment
from pydub.playback import play
import multiprocessing

class MusicUtil:
    def __init__(self, music_path):
        self.music_path = music_path
        self.music_process = None

    def __play_music__(self):
        song = AudioSegment.from_mp3(self.music_path)
        
        # Minus 12 dB
        song = song - 12
        
        play(song)

    def start_playback(self):
        self.music_process = multiprocessing.Process(target = self.__play_music__)
        self.music_process.start()

    def stop_playback(self):
        self.music_process.kill()