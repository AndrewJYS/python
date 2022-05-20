import pygame

class Music():

    def __init__(self):
        self.music = 'music/001.mp3'

    def play_music(self):
        """Play the music"""
        pygame.mixer.init()
        self.track = pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(loops=-1)
