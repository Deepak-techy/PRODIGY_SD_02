from tkinter import *
from tkinter import messagebox
import random

# Initialize game variables
random_number = int(random.randrange(1,101))
total_attempts = 0

# Function to check the user's guess
def checknumber():
    global total_attempts
    try:
        user_number = int(numvalue.get())
        total_attempts+=1
        if user_number > random_number:
            display_text="Too high! Try again."
            display_title="Try Again"
        elif user_number < random_number:
            display_text="Too low! Try again."
            display_title="Try Again"
        elif user_number == random_number:
            display_text=f"Correct! You guessed the number in {total_attempts} attempts."
            display_title="Congratulations!"
            reset_game()
        messagebox.showinfo(display_title, display_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to reset the game
def reset_game():
    global random_number, total_attempts
    random_number = random.randint(1, 101)
    total_attempts = 0
    numvalue.set("")

# Initialize the main window
root = Tk()
root.geometry("350x150")
root.title("Number Guessing Game")

# Create and place widgets in the main window
Label(text="Guess a number between 1 and 100 ", font="lucida 14 bold").pack(pady=10)

numvalue = StringVar()
numvalue.set("")
numentry = Entry(root, textvariable=numvalue).pack(pady=10)

Button(root, text="Guess", font="lucida 12 bold", command=checknumber, relief=RIDGE).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()