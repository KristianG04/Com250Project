import tkinter as tk
        from tkinter import ttk

        class MusicApp:
            def __init__(self, root):
                self.root = root
                self.root.title("Music App")

                # Create tabs
                self.tabControl = ttk.Notebook(self.root)
                self.tab1 = ttk.Frame(self.tabControl)
                self.tab2 = ttk.Frame(self.tabControl)

                self.tabControl.add(self.tab1, text="Songs")
                self.tabControl.add(self.tab2, text="Playlist")

                self.tabControl.pack(expand=1, fill="both")

                # Song list in Tab 1
                self.song_listbox = tk.Listbox(self.tab1, selectmode=tk.SINGLE)
                self.song_listbox.pack(pady=10)

                # Add some example songs
                self.populate_song_list()

                # Like button in Tab 1
                self.like_button = tk.Button(self.tab1, text="Like Song", command=self.like_song)
                self.like_button.pack(pady=5)

                # Playlist list in Tab 2
                self.playlist_listbox = tk.Listbox(self.tab2)
                self.playlist_listbox.pack(pady=10)

                # Like songs will be added to this list
                self.playlist = []

            def populate_song_list(self):
                # Add some example songs to the listbox
                songs = ["MELTDOWN","Search&Rescue"]
                for song in songs:
                    self.song_listbox.insert(tk.END, song)

            def like_song(self):
                # Get the selected song from the listbox
                selected_song = self.song_listbox.get(tk.ACTIVE)

                # Add the selected song to the playlist
                self.playlist.append(selected_song)

                # Clear and update the playlist listbox
                self.playlist_listbox.delete(0, tk.END)
                for song in self.playlist:
                    self.playlist_listbox.insert(tk.END, song)

        if __name__ == "__main__":
            root = tk.Tk()
            app = MusicApp(root)
            root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()


