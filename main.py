from cgitb import text
from email.mime import image
import random
from sys import exec_prefix
from textwrap import fill
from numpy import flip
import pandas
from tkinter import Tk, Canvas, Button, PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

to_learn ={}
current_card = {}

try:
    data = pandas.read_csv(r"data\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"data\french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    french_word = current_card["French"]

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_learn():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"data\words_to_learn.csv", index=False)
    next_card()



#--------------UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas= Canvas(height=526, width=800)
card_front_image = PhotoImage(file=r"images\card_front.png")
card_back_image = PhotoImage(file=r"images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

image_right = PhotoImage(file=r"images\right.png")
button_right = Button(image=image_right, highlightthickness=0, command=is_learn)
button_right.grid(column=0, row=1)

image_wrong = PhotoImage(file=r"images\wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(column=1, row=1)

next_card()

window.mainloop()