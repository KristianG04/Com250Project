import tkinter as tk
from tkinter import filedialog
import pygame


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.playlist = []
        self.current_song = 0
        self.paused = False

        self.initialize_ui()
        pygame.init()

    def initialize_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.play_button = tk.Button(self.frame, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.frame, text="Pause", command=self.pause_music)
        self.next_button = tk.Button(self.frame, text="Next", command=self.next_song)
        self.prev_button = tk.Button(self.frame, text="Previous", command=self.prev_song)
        self.add_button = tk.Button(self.frame, text="Add Music", command=self.add_music)

        self.play_button.grid(row=0, column=0)
        self.pause_button.grid(row=0, column=1)
        self.next_button.grid(row=0, column=2)
        self.prev_button.grid(row=0, column=3)
        self.add_button.grid(row=0, column=4)

        self.song_label = tk.Label(self.root, text="")
        self.song_label.pack()

    def add_music(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)

    def play_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.update_song_label()

    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def next_song(self):
        if self.current_song < len(self.playlist) - 1:
            self.current_song += 1
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.update_song_label()

    def prev_song(self):
        if self.current_song > 0:
            self.current_song -= 1
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            self.update_song_label()

    def update_song_label(self):
        song_name = self.playlist[self.current_song].split("/")[-1]
        self.song_label["text"] = "Now Playing: " + song_name

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
