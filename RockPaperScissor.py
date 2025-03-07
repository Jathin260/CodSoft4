import tkinter as tk
import random

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    result_label.config(text=f"You chose {choice}\nComputer chose {computer_choice}\n{result}")

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

# Frame setup
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Input label
label = tk.Label(root, text="Your choice", font=("Arial", 10))
label.pack(pady=5)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
rock = tk.Button(button_frame, text="Rock", width=8, command=lambda: play("Rock"))
rock.grid(row=0, column=0, padx=5)

paper = tk.Button(button_frame, text="Paper", width=8, command=lambda: play("Paper"))
paper.grid(row=0, column=1, padx=5)

scissors = tk.Button(button_frame, text="Scissors", width=8, command=lambda: play("Scissors"))
scissors.grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 10))
result_label.pack(pady=20)

root.mainloop()