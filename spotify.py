import os
import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize the pygame mixer
pygame.mixer.init()

# Define the Music Player class
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        
        self.current_song = ""
        self.paused = False
        
        # Create widgets
        self.label = tk.Label(root, text="No song loaded", width=40)
        self.label.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)
        
        self.load_button = tk.Button(root, text="Load", command=self.load_music)
        self.load_button.pack(pady=10)
    
    def load_music(self):
        self.current_song = filedialog.askopenfilename(initialdir=".", title="Select a Song",
                                                       filetypes=(("MP3 Files", "*.mp3"),))
        if self.current_song:
            self.label.config(text=os.path.basename(self.current_song))
            pygame.mixer.music.load(self.current_song)
            self.paused = False
    
    def play_music(self):
        if self.current_song:
            if self.paused:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.play()
            self.paused = False
    
    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.paused = False
        self.label.config(text="No song loaded")

# Create the main window
root = tk.Tk()

# Initialize the music player
app = MusicPlayer(root)

# Start the Tkinter main loop
root.mainloop()
