from cgitb import text
import random
import pandas
from tkinter import Tk, Canvas, Button, PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv(r"data\french_words.csv")

to_learn = data.to_dict(orient="records")

def next_card():
    entry = random.choice(to_learn)
    french_word = entry["French"]
    english_word = entry["English"]

    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(word_text, text=french_word)

#--------------UI

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas= Canvas(height=526, width=800)
card_front_image = PhotoImage(file=r"images\card_front.png")
card_back_image = PhotoImage(file=r"images\card_back.png")
canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

image_right = PhotoImage(file=r"images\right.png")
button_right = Button(image=image_right, highlightthickness=0, command=next_card)
button_right.grid(column=0, row=1)

image_wrong = PhotoImage(file=r"images\wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(column=1, row=1)

next_card()

window.mainloop()