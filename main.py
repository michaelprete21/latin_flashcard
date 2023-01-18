from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
english_word = ""
dict_index = ""


def known_word():
    global latin_dict
    global dict_index
    latin_dict.pop(dict_index)
    latin_dict = latin_dict
    latin_word()


def flip_card():
    myCanvas.itemconfig(background_canvas, image=card_back)
    myCanvas.itemconfig(word_canvas, text=f"{english_word}", fill="white")
    myCanvas.itemconfig(title_canvas, text="English", fill="white")
    Button(image=red_button, command=latin_word).grid(column=2, row=2)


def latin_word():
    global english_word
    global dict_index
    dict_index = random.randint(0, len(latin_dict))
    translation = latin_dict[dict_index]
    myCanvas.itemconfig(word_canvas, text=f"{(translation['Latin'])}", fill="black")
    myCanvas.itemconfig(background_canvas, image=card_front)
    myCanvas.itemconfig(title_canvas, text="Latin", fill="black")
    english_word = translation['English']
    Button(image=flip_button, command=flip_card).grid(column=2, row=2)
    Button(image=green_button, command=known_word).grid(column=0, row=2)


# Create dataframe
try:
    latin_df = pd.read_csv('unknown words.csv')
except:
    latin_df = pd.read_csv('1000_latin_vocab.csv')
finally:
    latin_dict = latin_df.to_dict(orient='records')

# Set-up Window
window = Tk()
window.title("Vocabulary")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image imports
green_button = PhotoImage(file='images/right.png')
red_button = PhotoImage(file='images/wrong.png')
flip_button = PhotoImage(file='images/refresh.png')
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

# Set canvas and text
myCanvas = Canvas(width=800, height=526)
background_canvas = myCanvas.create_image(400, 263, image=card_front)
title_canvas = myCanvas.create_text(400, 150, text="Latin", font=("Ariel", 60, "italic"))
word_canvas = myCanvas.create_text(400, 250, text="word", font=("Ariel", 30, "bold"))
myCanvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
myCanvas.grid(column=0, row=0, columnspan=3)

# Create buttons
Button(image=green_button, command=latin_word).grid(column=0, row=2)
Button(image=flip_button, command=flip_card).grid(column=2, row=2)

window.mainloop()

known_latin = pd.DataFrame(latin_dict)
known_latin.to_csv('unknown words.csv', index=False)
