import tkinter as tk
from tkinter import filedialog
import pygame


class MusicPlayer:

    #Constructor for MusicPLayer class
    #Creates GUI
    def __init__(self, title, size):

        #Creates instance of the Tk class
        #Needed to use Tkinter
        self.window = tk.Tk()

        #Title of our application window
        self.window.title(title)

        #The size of our application GUI
        self.window.geometry(str(size[0]) + 'x' + str(size[1]))

        #Makes sure that our GUI can't be made smaller 
        # than this
        self.window.minsize(size[0],size[1])

        #playlist is an array containing the songs
        #that were added to the personal playlist
        self.playlist = []

        #Index of the song in the playlist
        #used when moves back and forth in the playlist
        self.current_song = 0

        
        self.paused = False

        self.initialize_ui()
        pygame.init()

        #This is function that creates an infinite loop
        #used to keep the GUI open while it is waiting
        #for the user to interact with it
        self.window.mainloop()

    def initialize_ui(self):
        
        #############################################################
        #   Playlist GUI Frame
        #############################################################

        #This will be the frame used to create the
        # right side of the UI, aka the playlist side
        self.playlist_frame = tk.Frame(self.window)

        #Places the playlist_frame starting 55% from the left
        # of the screen with relx = 0.55, the extra 0.05 creates 
        # a buffer on the left side of the frame.
        # relwidth is .40 so there is a .05 buffer zone on the
        # right side of the frame
        # rely is .10 so the playlist_title can go in that upper 
        # .10 percent
        self.playlist_frame.place(relx = 0.55, 
                                  rely = 0.10, 
                                  relwidth= 0.40,
                                  relheight= 0.10)

        ############################
        #   Playlist Widgets
        ############################

        #Keep in mind that this Label is not located in the
        # Playlist Frame, but instead is just in the general
        # window
        self.playlist_title = tk.Label(self.window,
                                       text = "Personal Playlist",
                                       font = ('Arial', 25))

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
        
        self.add_button = tk.Button(self.playlist_frame, 
                                    text="Add Music", 
                                    command=self.add_music)
        
        #Also located in the window and not playlist frame
        self.currently_playing = tk.Label(self.window,
                                          text = "Currently Playing",
                                          font = ("Arial", 20))
        
        #Also located in the window and not playlist frame
        self.song_label = tk.Label(self.window,
                                   text="None",
                                   font = ("Arial", 15))

        ############################
        #   Playlist Widgets layout
        ############################

        self.playlist_title.place(relx = 0.55,
                                  y = 0,
                                  relwidth = 0.40,
                                  relheight = 0.10)

        self.playlist_frame.columnconfigure((0,1,2,3,4), weight = 1)

        self.playlist_frame.rowconfigure((0), weight = 0)

        self.play_button.grid(row=0, column=0, sticky = 'we')
        self.pause_button.grid(row=0, column=1, sticky = 'we')
        self.next_button.grid(row=0, column=2, sticky = 'we')
        self.prev_button.grid(row=0, column=3, sticky = 'we')
        self.add_button.grid(row=0, column=4, sticky = 'we')

        self.currently_playing.place(relx = 0.55,
                                     rely = 0.20,
                                     relwidth = 0.40,
                                     relheight = 0.10)
        
        self.song_label.place(relx = 0.55,
                              rely = 0.30,
                              relwidth = 0.40,
                              relheight = 0.10)

        #############################################################
        #   Homepage GUI Frame
        #############################################################

        #This will be the frame used to create the
        # left side of the UI, aka the homepage side
        self.homepage_frame = tk.Frame(self.window)

        #homepage layout
        #x is set to 0 so it starts on the left side
        # relwidth ensures it takes up half the screen's width
        # rel height ensures it takes up the left side vertically
        self.homepage_frame.place(relx = 0.14, 
                                  rely = 0.20, 
                                  relwidth = 0.40, 
                                  relheight = 0.10)
        
        #Test code, DELETE IT LATER
        #tk.Label(self.homepage_frame, 
        #         background = 'red',).pack(expand = True,
        #                                   fill = 'both')
        
        ############################
        #   Homepage Widgets
        ############################

        self.homepage_title = tk.Label(self.window,
                                       text = "Welcome to a Better Spotify",
                                       font = ('Arial', 20))
        
        self.library_title = tk.Label(self.window,
                                       text = "Library",
                                       font = ('Arial', 25))
        
        #This is the variable name used to store whatever
        #The user types into the Entry widget defined below
        searched_song = tk.StringVar()

        self.user_search = tk.Entry(self.homepage_frame,
                                    textvariable = searched_song,
                                    font = ('calibre', 10))
        self.searched_results_var = tk.StringVar()
        #Search button here, integrate search bar code here
        self.search_button = tk.Button(
            self.homepage_frame,
            text="Search",
            command=self.search_music
        )
        
        self.search_result = tk.Listbox(
            self.homepage_frame,
            height=5,
            width=25,
            listvariable=self.searched_results_var
        )
        self.search_result.bind("<<ListboxSelect>>", self.play_selected_song)
        
        #This is the variable name used to store whether
        #The user selected the song they searched for or not
        #to add to thier playlist
        select_song = tk.IntVar()

        self.search_selection_checkbox = tk.Checkbutton(self.window,
                                                        text = "Select Searched Song",
                                                        variable = select_song,
                                                        onvalue = 1,
                                                        offvalue = 0,
                                                        height = 10,
                                                        width = 25)
        
        


        ############################
        #   Homepage Widgets layout
        ############################

        self.homepage_title.place(relx = .05,
                                  y = 0,
                                  relwidth = 0.40,
                                  relheight = 0.10)
        
        self.library_title.place(relx = .05,
                                 rely = .10,
                                 relwidth = 0.40,
                                 relheight = 0.10)
        
        self.user_search.grid(row = 0,
                              column = 0)
        
        self.search_button.grid(row = 0,
                                column = 1)
        
        self.search_result.grid(row = 1,
                                column = 0)

        #change code so the button goes below the search_result
        self.search_selection_checkbox.place(relx = .20,
                                             rely = .30,
                                             relwidth = .15,
                                             relheight = .10)


    #############################################################
    #   Button Functionality
    #############################################################


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
    def search_music(self):


        searched_term = self.user_search.get().lower()


        results = [song for song in self.playlist if searched_term in song.lower()]
        self.searched_results_var.set(tuple(results))
    def play_selected_song(self, event):
        
     
        selected_index = self.search_result.curselection()
        if selected_index:
            selected_song = self.search_result.get(selected_index[0])
            
            self.playlist.append(selected_song)
            
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
            self.update_song_label()