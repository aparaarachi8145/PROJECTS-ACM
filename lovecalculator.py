# Import tkinter and random modules
from tkinter import *
import random

# Creating the GUI window
root = Tk()
# Setting the size of the window
root.geometry('400x240')
# Setting the title of the window
root.title('Love Calculator')

# Function to calculate love percentage
def calculate_love():
    # Randomly generate a percentage between 0 and 100
    love_percentage = random.randint(0, 100)
    # Update the result label with the calculated percentage
    result.config(text=f"Love Percentage: {love_percentage}%")

# Heading at the top
heading = Label(root, text='Love Calculator - How much is he/she into you?', font=('Helvetica', 14))
heading.pack(pady=10)

# Input for the user's name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack(pady=5)

# Input for the partner's name
slot2 = Label(root, text="Enter Your Partner's Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack(pady=5)

# Button to calculate love percentage
bt = Button(root, text="Calculate", height=1, width=10, command=calculate_love)
bt.pack(pady=10)

# Label to display the result
result = Label(root, text='Love Percentage between both of You will appear here.', font=('Helvetica', 12))
result.pack(pady=10)

# Run the main loop to keep the window open
root.mainloop()

