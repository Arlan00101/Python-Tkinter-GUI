# Importing tkinter as tk
import tkinter as tk

# Creating the root windows
# IMPORTANT all the tkinter code must be inside this root and the root.mainloop()
root = tk.Tk()

# Setting the title of the window
root.title("Windows Title")

# Setting the dimentions and position ("[width]x[height]+[Xposition]+[Yposition]")
root.geometry("800x600+500+250")

# Creating the mainloop
root.mainloop()
