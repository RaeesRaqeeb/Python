
import tkinter as Mano
import time

timestamp = int(time.strftime("%H"))

# Define the popup_message function
def popup_message(message):
    popup = Mano.Tk()
    popup.geometry("300x100") 
    label = Mano.Label(popup, text=message)
    label.pack(pady=10)

    button = Mano.Button(popup, text="OK", command=popup.destroy)
    button.pack()

    popup.mainloop()

# Call the popup_message function based on the time conditions
if 6 <= timestamp < 12:
    popup_message("Good Morning Sir!")
elif 12 <= timestamp <= 17:
    popup_message("Good Afternoon Sir!")
elif 17 <= timestamp < 20:
    popup_message("Good Evening Sir!")
elif 20 <= timestamp <= 23 or 0 <= timestamp < 6:
    popup_message("Good Night Sir!")
