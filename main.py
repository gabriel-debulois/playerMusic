from tkinter import *
# from tkinter import filedialog
import pygame.mixer as mixer
import os

music_player = Tk()
music_player.geometry("312x515")
music_player.resizable(width=False, height=False)
music_player.title("musicPlayer")
mixer.init()

os.chdir("./dir_player")


def load():
    for file in os.listdir():
        filename = os.fsdecode(file)
        mixer.music.load(filename)
        playlist.insert(END, filename)


def play():
    current_song = playlist.get(ACTIVE)
    mixer.music.load(current_song)
    mixer.music.play()


def stop():
    mixer.music.stop()


def pause():
    mixer.music.pause()


def unpause():
    mixer.music.unpause()


def loop():
    mixer.music.play(loops=-1)


# function to increase or decrease the volume
def volume(number):
    # if the up button is triggered, increase the volume by 0.1
    if number == 1:
        mixer.music.set_volume(mixer.music.get_volume() + 0.1)
        print(mixer.music.get_volume())
    # else if the down button is triggered, decrease the volume by 0.1
    elif number == 0:
        mixer.music.set_volume(mixer.music.get_volume() - 0.1)
        print(mixer.music.get_volume())


def delete():
    playlist.delete(ANCHOR)


playlist = Listbox(music_player, font=('Helvetica', 11), selectbackground='Gold')
playlist.pack(fill=BOTH, padx=50, pady=200)

btn_load = Button(music_player, text='Load', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: load())
btn_load.place(y=80)

play_btn = Button(music_player, text='Play', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: play())
play_btn.place(x=195, y=10)

stop_btn = Button(music_player, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: stop())
stop_btn.place(x=105, y=10)
pause_btn = Button(music_player, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,
                   command=lambda: pause())
pause_btn.place(x=105, y=80)
unpause_btn = Button(music_player, text='Unpause', bg='Aqua', font=("Georgia", 13), width=7,
                     command=lambda: unpause())
unpause_btn.place(x=195, y=80)
up_btn = Button(music_player, text='Up', bg='Aqua', font=("Georgia", 13), width=7,
                command=lambda: volume(1))
up_btn.place(x=195, y=160)
down_btn = Button(music_player, text='Down', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: volume(0))
down_btn.place(x=105, y=160)
btn_loop = Button(music_player, text='Loop', bg='Aqua', font=("Georgia", 13), width=7,
                  command=lambda: loop())
btn_loop.place(y=160)
btn_delete = Button(music_player, text='Delete', bg='Aqua', font=("Georgia", 13), width=7,
                    command=lambda: delete())
btn_delete.place(y=10)

music_player.mainloop()
