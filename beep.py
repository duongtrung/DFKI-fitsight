import pygame
import threading
import time

def beep():
    while True:  # Play the sound 5 times
        pygame.mixer.music.play()
        time.sleep(3)  # Wait for 3 seconds between beeps

# Set the audio driver to "dummy" to avoid the audio device issue
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(8)

# Load the audio file outside of the beep function
pygame.mixer.music.load("lets_go.mp3")  # Replace with your audio file path

time.sleep(60)

beep()

