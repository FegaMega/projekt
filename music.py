import pygame, sys
from pygame.locals import *
class music:
    def __init__(self, music_library):
        pygame.mixer.init()
        self.mixer = pygame.mixer.music
        self.music_Library = music_library
        self.CurrentIndex = 0
        self.SONG_END = 100
        self.volume = 1
        self.mixer.set_volume(self.volume)
        self.mixer.load(self.music_Library[self.CurrentIndex])
        self.mixer.play()
    def RunMusic(self):
        if self.mixer.get_endevent() != pygame.NOEVENT:
            self.mixer.unload()
            self.CurrentIndex += 1
            if self.CurrentIndex <= len(self.music_Library) -1:
                self.CurrentIndex = 0
            self.mixer.load(self.music_Library[self.CurrentIndex])
            self.mixer.play()
    def PauseMusic(self):
        self.mixer.pause()
    def UnpauseMusic(self):
        self.mixer.unpause()
    def SkipMusic(self):
        self.mixer.stop()
        self.mixer.unload()
        self.CurrentIndex += 1
        self.mixer.load(self.music_Library[self.CurrentIndex])
        self.mixer.play()
    def SetVolume(self, Volume):
        self.volume = Volume
        self.mixer.set_volume(self.volume)
    def LowerVolume(self, increments):
        self.volume -= increments
        self.mixer.set_volume(self.volume)
    def IncreaseVolume(self, increments):
        self.volume += increments
        self.mixer.set_volume(self.volume)
    
    def PlaySound(self, fileORarrayIndex):
        if fileORarrayIndex.__class__ == str:
            self.mixer.load(fileORarrayIndex)
            self.mixer.play()
        if fileORarrayIndex.__class__ == int:
            self.mixer.load(self.music_Library[fileORarrayIndex])
            self.mixer.play()


def main():
    mixer = music(["Cipher_BGM.flac", "Aloft_BGM.flac", "lemmino-nocturnal.flac"])
    screen = pygame.display.set_mode((700, 700))
    r = True    
    while r == True:
        screen.fill((146, 244, 255))
        # Töm event kön
        for event in pygame.event.get():
            # Quit kod
            if event.type == QUIT:
                pygame.mixer.stop()
                r = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_s:
                    print("skip Music")
                    mixer.SkipMusic()
                if event.key == K_p:
                    print("Pause Music")
                    mixer.PauseMusic()
                if event.key == K_u:
                    print("Unpause Music")
                    mixer.UnpauseMusic()
                if event.key == K_DOWN:
                    mixer.LowerVolume(.1)
                if event.key == K_UP:
                    mixer.IncreaseVolume(.1)

        mixer.RunMusic()
if __name__ == '__main__':
    sys.exit(main())