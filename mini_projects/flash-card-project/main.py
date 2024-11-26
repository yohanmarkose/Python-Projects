import tkinter as tk
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
FLIP_TIMER = None
CURRENT_CARD = {}
# Reading csv and creating the question and answer dictionary
quest_ans_filename = 'french_words.csv'
words_to_learn_filename = 'words_to_learn.csv'
to_learn = {}
try:
    df_quest_ans = pd.read_csv(f'data/{words_to_learn_filename}')
except FileNotFoundError:
    df_quest_ans = pd.read_csv(f'data/{quest_ans_filename}')
    to_learn = df_quest_ans.to_dict(orient='records')
else:
    to_learn = df_quest_ans.to_dict(orient='records')


#-------------Generate random questions on flashcard----------------#
def show_answer(ans):
    canvas.itemconfig(front_card, image=back_card_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_question, text=ans, fill='white')

def next_card(status):
    global FLIP_TIMER, CURRENT_CARD
    window.after_cancel(FLIP_TIMER)
    canvas.itemconfig(front_card, image=front_card_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    CURRENT_CARD = random.choice(to_learn)
    canvas.itemconfig(card_question, text=current_card['French'], fill='black')

    answer = CURRENT_CARD['English']
    FLIP_TIMER = window.after(3000, show_answer, answer)  # passing the fn and the argument

def is_known():  # if user clicked the tick button
    to_learn.remove(CURRENT_CARD)
    next_card()

#-------------------------------UI----------------------------------#
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

question = "Quetion?"
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = tk.PhotoImage(file='images/card_front.png')
back_card_img = tk.PhotoImage(file='images/card_back.png')

front_card = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 120, text=f"title", font=("Ariel", 30, "italic"))
card_question = canvas.create_text(400, 220, text=question, font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = tk.PhotoImage(file='images/wrong.png')
wrong_button = tk.Button(image=wrong_image, width=90, height=90, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = tk.PhotoImage(file='images/right.png')
right_button = tk.Button(image=right_image, width=90, height=90, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

FLIP_TIMER = window.after(3000, show_answer)
next_card()  # To show the next card before clicking a button

window.mainloop()

df_to_learn = pd.DataFrame(to_learn)
df_to_learn.to_csv('data/words_to_learn.csv', index=False)