import tkinter as tk

#imports the MusicPlayer class from the homepageGUI
#File so we can use the constructor from that class
#To start up the Homepage GUI
from homepageGui import MusicPlayer

#############################################################

def main():

    #Calls the constructor for the MusicPlayer class
    #The constructor will automatically start up the GUI
    app = MusicPlayer("A Better Spotify", (900,600))

#############################################################

#Calls our main function, starting our application
main()
