import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:

    # Constructor for MusicPlayer class
    # Creates GUI
    def __init__(self, title, size):
        # Creates instance of the Tk class
        # Needed to use Tkinter
        self.window = tk.Tk()

        # Title of our application window
        self.window.title(title)

        # The size of our application GUI
        self.window.geometry(str(size[0]) + 'x' + str(size[1]))

        # Makes sure that our GUI can't be made smaller
        # than this
        self.window.minsize(size[0], size[1])

        # Set the background color of the main window
        self.window.configure(bg='#000000')  # Black background

        # playlist is an array containing the songs
        # that were added to the personal playlist
        self.playlist = []
        self.library = []

        # Index of the song in the playlist
        # used when moving back and forth in the playlist
        self.current_song = 0

        self.paused = False

        # Call the method to set up the user interface
        self.initialize_ui()

        # Initialize Pygame for music playback
        pygame.init()

        # Start the Tkinter event loop
        self.window.mainloop()

    def initialize_ui(self):

        #############################################################
        #   Playlist GUI Frame
        #############################################################

        # This will be the frame used to create the
        # right side of the playlist side
        self.playlist_frame = tk.Frame(self.window)


        self.playlist_frame.place(relx=0.55,
                                  rely=0.10,
                                  relwidth=0.40,
                                  relheight=0.10)

        ############################
        #   Playlist Widgets
        ############################

        # Keep in mind that this Label is not located in the
        # Playlist Frame, but instead is just in the general
        # window
        self.playlist_title = tk.Label(self.window,
                                       text="Personal Playlist",
                                       font=('Arial', 25))

        # Buttons for controlling music playback
        self.play_button = tk.Button(self.playlist_frame,
                                     text="Play",
                                     command=self.play_music)

        self.pause_button = tk.Button(self.playlist_frame,
                                      text="Pause",
                                      command=self.pause_music)

        self.next_button = tk.Button(self.playlist_frame,
                                     text="Next",
                                     command=self.next_song)

        self.prev_button = tk.Button(self.playlist_frame,
                                     text="Previous",
                                     command=self.prev_song)

        # Labels for displaying currently playing song
        # and the playlist
        self.currently_playing = tk.Label(self.window,
                                          text="Currently Playing: ",
                                          font=("Arial", 20))

        self.song_label = tk.Label(self.window,
                                   text="None",
                                   font=("Arial", 15))

        ############################
        #   Playlist Widgets layout
        ############################

        self.playlist_title.place(relx=0.55,
                                  y=0,
                                  relwidth=0.40,
                                  relheight=0.10)

        self.playlist_frame.columnconfigure((0, 1, 2, 3), weight=1)

        self.playlist_frame.rowconfigure((0), weight=0)

        self.play_button.grid(row=0, column=0, sticky='we')
        self.pause_button.grid(row=0, column=1, sticky='we')
        self.next_button.grid(row=0, column=2, sticky='we')
        self.prev_button.grid(row=0, column=3, sticky='we')

        self.currently_playing.place(relx=0.55,
                                     rely=0.20,
                                     relwidth=0.40,
                                     relheight=0.10)

        self.song_label.place(relx=0.55,
                              rely=0.30,
                              relwidth=0.40,
                              relheight=0.10)

        #############################################################
        #   Homepage GUI Frame
        #############################################################

        # This will be the frame used to create the
        # left side of the homepage side
        self.homepage_frame = tk.Frame(self.window)

        # homepage layout
        # x is set to 0 so it starts on the left side
        # relwidth ensures it takes up half the screen's width
        # rel height ensures it takes up the left side vertically
        self.homepage_frame.place(relx=0.14,
                                  rely=0.30,
                                  relwidth=0.40,
                                  relheight=0.10)

        ############################
        #   Homepage Widgets
        ############################

        self.homepage_title = tk.Label(self.window,
                                       text="Welcome to a Better Spotify",
                                       font=('Arial', 20))

        self.library_title = tk.Label(self.window,
                                      text="Library",
                                      font=('Arial', 25))

        self.add_button = tk.Button(self.window,
                                    text="Add Music",
                                    command=self.add_music)

        # This is the variable name used to store whatever
        # The user types into the Entry widget defined below
        searched_song = tk.StringVar()

        self.user_search = tk.Entry(self.homepage_frame,
                                    textvariable=searched_song,
                                    font=('calibre', 10))

        self.searched_results_var = tk.StringVar()

        self.search_button = tk.Button(self.homepage_frame,
                                       text="Search",
                                       command=self.search_music
                                       )

        self.search_result = tk.Listbox(self.window,
                                        height=100,
                                        width=100,
                                        listvariable=self.searched_results_var
                                        )
        self.search_result.bind("<<ListboxSelect>>", self.searched_results_var)

        # Like button, used to add songs from the library to the playlist
        # Add like button functionality to this

        self.like_button = tk.Button(self.window,
                                     text="Like", command=self.like_song)

        ############################
        #   Homepage Widgets layout
        ############################

        self.homepage_title.place(relx=.05,
                                  y=0,
                                  relwidth=0.40,
                                  relheight=0.10)

        self.library_title.place(relx=.05,
                                 rely=.10,
                                 relwidth=0.40,
                                 relheight=0.10)

        self.add_button.place(relx=.20,
                              rely=.20,
                              relwidth=.10,
                              relheight=.05)

        self.user_search.grid(row=0,
                              column=0)

        self.search_button.grid(row=0,
                                column=1)

        self.search_result.place(relx=.05,
                                 rely=.35,
                                 relwidth=0.40,
                                 relheight=0.30)

        self.like_button.place(relx=0.20,
                               rely=0.80,
                               relwidth=0.10,
                               relheight=0.10)

        self.playlist_frame.configure(bg='#b3b3b3')
        self.playlist_title.configure(bg='#b3b3b3', fg='blue')

        button_color = '#4caf50'  # Green color
        self.play_button.configure(bg=button_color)
        self.pause_button.configure(bg=button_color)
        self.next_button.configure(bg=button_color)
        self.prev_button.configure(bg=button_color)
        self.add_button.configure(bg=button_color)

        self.homepage_frame.configure(bg='#b3b3b3')
        self.homepage_title.configure(bg='#b3b3b3', fg='blue')
        self.library_title.configure(bg='#b3b3b3', fg='blue')

        # Set background color for Search Button
        self.search_button.configure(bg='#2196f3')  # Blue color

        # Set background color for Like Button
        self.like_button.configure(bg='#4caf50')  # Green color

        #############################################################
    #   Button Functionality
    #############################################################

    def add_music(self):
        # Ask user to select a directory
        directory_path = filedialog.askdirectory()
        if directory_path:
            # Loop through files in the selected directory
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    # Check if the file has a valid music extension
                    if file.lower().endswith((".mp3", ".wav")):
                        file_path = os.path.join(root, file)
                        # Add the file path to the library
                        self.library.append(file_path)

    def play_music(self):
        # Check if there's a song in the playlist and no song is currently playing
        if not pygame.mixer.music.get_busy() and self.playlist:
            # Load and play the current song in the playlist
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            # Update the song label to display the currently playing song
            self.update_song_label()

    def pause_music(self):
        # Check if music is not paused, then pause it; if it is paused, then unpause
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def next_song(self):
        # Check if there are more songs in the playlist
        if self.current_song < len(self.playlist) - 1:
            # Move to the next song in the playlist
            self.current_song += 1
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            # Update the song label to display the currently playing song
            self.update_song_label()

    def prev_song(self):
        # Check if there are previous songs in the playlist
        if self.current_song > 0:
            # Move to the previous song in the playlist
            self.current_song -= 1
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()
            # Update the song label to display the currently playing song
            self.update_song_label()

    def update_song_label(self):
        # Pull the name of the currently playing song from the file path
        song_name = self.playlist[self.current_song].split("/")[-1]
        # Update the song label with the currently playing song
        self.song_label["text"] = "Now Playing: " + song_name

    def search_music(self):
        # Get the searched term from the user input
        searched_term = self.user_search.get().lower()
        # Filter the library based on the searched term
        results = [song for song in self.library if searched_term in song.lower()]
        # Set the search results variable to update the Listbox
        self.searched_results_var.set((results))

    def like_song(self):
        # Get the selected song from the listbox
        selected_song = self.search_result.get(tk.ACTIVE)
        # Add the selected song to the playlist
        self.playlist.append(selected_song)
        # Clear and update the playlist listbox
        self.playlist.delete(0, tk.END)
        for song in self.playlist:
            self.playlist.insert(tk.END, song)
