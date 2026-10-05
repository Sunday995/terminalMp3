import pygame
import os
import time

#start pygame
pygame.mixer.init()

#Ask user for the MP3 location
mp3_location = input("Enter the location of the MP3 file: ")

#Check if the file exists
if not os.path.isfile(mp3_location):
    print("File does not exist. Please check the path and try again.")
    exit()

#Load the MP3 file
pygame.mixer.music.load(mp3_location)

#Play the MP3 file
pygame.mixer.music.play()

print("\nPlaying...")
print("press Q to stop the music and exit.")

# Keep the program running
while True:
    key = input("Press 'Q' to stop the music and exit: ")

    if key.lower() == 'q':
        pygame.mixer.music.stop()
        print("Music stopped. Exiting...")
        break