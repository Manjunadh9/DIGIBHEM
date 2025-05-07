import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize pygame mixer
pygame.mixer.init()

# Main App Window
root = tk.Tk()
root.title("Digital Bhem - Music Player")
root.geometry("400x200")
root.resizable(False, False)

current_song = ""

def open_file():
    global current_song
    current_song = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if current_song:
        pygame.mixer.music.load(current_song)

def play_music():
    if current_song:
        pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

tk.Label(root, text="Simple Music Player", font=("Helvetica", 16)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Open", width=10, command=open_file).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Play", width=10, command=play_music).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Pause", width=10, command=pause_music).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Resume", width=10, command=resume_music).grid(row=1, column=0, padx=5, pady=10)
tk.Button(frame, text="Stop", width=10, command=stop_music).grid(row=1, column=1, padx=5, pady=10)

root.mainloop()
