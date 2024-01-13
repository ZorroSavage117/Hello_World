import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("Hello World")

# Create a label widget with the text "Hello World"
label = tk.Label(window, text="Hello World")

# Pack the label widget to display it in the window
label.pack()

# Start the main event loop
window.mainloop()
