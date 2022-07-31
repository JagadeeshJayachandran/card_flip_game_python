from tkinter import *
from tkinter.ttk import Button

import pandas
import pandas as pd
import random
current_card = {}
try:
    data_frame = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    words = original_data.to_dict(orient="records")
else:
    words = data_frame.to_dict(orient="records")

def next_card():
    """Read excel file"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=my_image)
    flip_timer = window.after(3000, func=flip_card)
    print(current_card['French'])
#     return words['French']
#
# print(next_card())
def is_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/Words_to_learn.csv", index=False)
    next_card()

BACKGROUND_COLOR = "#B1DDC6"

def flip_card():
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

window = Tk()

window.title("Flashy")


window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
my_image = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=my_image)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# button = Button(image=my_image)
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,  command=next_card)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)
next_card()

window.mainloop()