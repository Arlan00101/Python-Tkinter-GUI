# Importing tkinter as tk
import tkinter as tk

# Creating the root windows
# IMPORTANT all the tkinter code must be inside this root and the root.mainloop()
root = tk.Tk()

# Setting the title of the window
root.title("Windows Title")

# Setting the dimentions and position ("[width]x[height]+[Xposition]+[Yposition]")
root.geometry("800x600+500+250")

# Setting a green background on the root
root.config(background="green")

# Setting the cursor inside the root to a pointing hand
root.config(cursor="hand2")

# Setting a border relief here we add a bd(border)
root.config(bd=40, relief="groove")

# Creating the mainloop
root.mainloop()
