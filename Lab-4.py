import tkinter as tk
from tkinter import Label

import pygame
import random as rn
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Astroneer OST — Cave 1.mp3")


def key():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = rn.randint(0, 25)
    b = rn.randint(0, 25)
    work_letters = letters[min(a, b):max(a, b)]
    if min(a, b) == max(a, b):
        seq = ''
        seq = letters[a] * 7
    else:
        seq = ''
        for i in range(7):
            seq += work_letters[rn.randint(0, len(work_letters) - 1)]
    temp_key = str(min(a, b)) + ' ' + seq + ' ' + str(max(a, b))
    return temp_key


def animation():
    for i in range(10):
        window.update_idletasks()

        frame = tk.Frame(window)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        label_bg: Label = tk.Label(frame, image=bg)
        label_bg.grid()

        label_animation = tk.Label(frame, text=key(), font=("Arial", 30), bg='#999900')
        label_animation.grid(column=0, row=0, padx=10, pady=20)

        time.sleep(0.5)


window = tk.Tk()
window.title("Astroneer key generator")
window.geometry('804x504')
bg = tk.PhotoImage(file='yd.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

label_bg = tk.Label(frame, image=bg)
label_bg.grid()

button_key = tk.Button(frame, text='Сгенерировать уникальный код', font=("Arial", 15), command=animation)
button_key.grid(column=0, row=0, padx=10, pady=20)

pygame.mixer.music.play(-1)
window.mainloop()
