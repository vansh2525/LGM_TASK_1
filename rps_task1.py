import tkinter as tk
import random
from tkinter import font

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.config(bg="#EAECEE")  # Greyish Blue Background
root.geometry('700x300')

# Initialize scores
player_score = 0
computer_score = 0
options = [('Rock', 0), ('Paper', 1), ('Scissors', 2)]

# Game Title
title_label = tk.Label(root, text='Rock Paper Scissors', font=font.Font(size=20), bg="#EAECEE")
title_label.pack(pady=10)

# Functions
def player_choice(player_input):
    global player_score, computer_score
    computer_input = get_computer_choice()
    player_choice_label.config(text='You Selected: ' + player_input[0])
    computer_choice_label.config(text='Computer Selected: ' + computer_input[0])
    
    if player_input == computer_input:
        winner_label.config(text='It\'s a Tie!')
    elif (player_input[1] - computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text='You Won!')
        player_score_label.config(text='Your Score: ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text='Computer Won!')
        computer_score_label.config(text='Computer Score: ' + str(computer_score))

def get_computer_choice():
    return random.choice(options)

def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    player_choice_label.config(text='')
    computer_choice_label.config(text='')
    winner_label.config(text="Let's Start the Game...")
    player_score_label.config(text='Your Score: 0')
    computer_score_label.config(text='Computer Score: 0')

# Labels
winner_label = tk.Label(root, text="Let's Start the Game...", fg="#2C3E50", bg="#EAECEE", font=font.Font(size=14), pady=9)
winner_label.pack(pady=10)

player_choice_label = tk.Label(root, text='', fg="#2C3E50", bg="#EAECEE", font=font.Font(size=12))
player_choice_label.pack()

computer_choice_label = tk.Label(root, text='', fg="#2C3E50", bg="#EAECEE", font=font.Font(size=12))
computer_choice_label.pack()

# Scores
player_score_label = tk.Label(root, text='Your Score: 0', fg="#2C3E50", bg="#EAECEE", font=font.Font(size=12))
player_score_label.pack(side=tk.LEFT, padx=(20, 0))

computer_score_label = tk.Label(root, text='Computer Score: 0', fg="#2C3E50", bg="#EAECEE", font=font.Font(size=12))
computer_score_label.pack(side=tk.RIGHT, padx=(0, 20))

# Input Frame
input_frame = tk.Frame(root, bg="#EAECEE")
input_frame.pack(pady=20)

# Buttons
rock_button = tk.Button(input_frame, text="Rock", bg="#FF5733", fg="white", font=font.Font(size=14), command=lambda: player_choice(('Rock', 0)))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(input_frame, text="Paper", bg="#33FF57", fg="white", font=font.Font(size=14), command=lambda: player_choice(('Paper', 1)))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(input_frame, text="Scissors", bg="#3357FF", fg="white", font=font.Font(size=14), command=lambda: player_choice(('Scissors', 2)))
scissors_button.grid(row=0, column=2, padx=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", bg="#E74C3C", fg="white", font=font.Font(size=14), command=reset_game)
reset_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
