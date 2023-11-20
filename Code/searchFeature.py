class MusicPlayer:
    def __init__(self, library):
        self.library = library
        self.current_playlist = library

    def search_songs(self, query):
        results = [song for song in self.library if query.lower() in song.lower()]
        return results

    def display_playlist(self):
        print("Current Playlist:")
        for i, song in enumerate(self.current_playlist, 1):
            print(f"{i}. {song}")

    def autocomplete(self, text, state):
        options = [song for song in self.library if song.lower().startswith(text.lower())]
        return options[state] if state < len(options) else None

    def run_music_player(self):
        while True:
            user_input = input("Enter song name (or part of it): ")
            search_results = self.search_songs(user_input)
            if len(search_results) == 1:
               print(f"Autofilling: {search_results[0]}")
               user_input = search_results[0]

            elif len(search_results) >= 1:
                print(f"{search_results[0]}")
                user_input = search_results[0]
            else:
                print(f"No result for \""+user_input+"\" \n")
                continue
            print("\nSearch Results:")
            for i, result in enumerate(search_results, 1):
                print(f"{i}. {result}")

            choice = input("Enter the index of the song to play (0 to cancel): ")
            if choice == "0":
                continue

            try:
                song_index = int(choice)
                if 1 <= song_index <= len(search_results):
                    print(f"Now playing: {search_results[song_index-1]}")
                else:
                    print("Invalid song index.")

                
            except ValueError:
                print("Invalid input. Please enter a number or '0' to cancel.")

songs_library = ["Hello - Adele", "Kill Bill - SZA", "Billie Jean - Michael Jackson", "Stairway to Heaven - Led Zepplin", "Bohemian Rhapsody - Queen", "Across the Universe - The Beatles", "Time in a Bottle - Jim Croce", "No Woman No Cry - Bob Marley", "All Along the Watchtower - Jimi Hendrix", "Like a Rolling Stone - Bob Dylan", "Is it over now - Taylor Swift", "Now that we don't talk - Taylor Swift", "Paint the Town Red - Doja Cat", 'Let it Be - The Beatles', "Cruel Summer - Taylor Swift", "Snooze - SZA", "Style - Taylor Swift", "Style(Taylor's Version) - Taylor Swift","The Times they are a changing - Bob Dylan", "Highway 61 Revisited - Bob Dylan", "Knocking on Heaven's Door - Bob Dylan", "My Back Pages - Bob Dylan", "Rolling in the Deep - Adele", "Someone like you - Adele"  ]
music_player = MusicPlayer(songs_library)
music_player.run_music_player()