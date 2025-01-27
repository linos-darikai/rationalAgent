import tkinter as tk

root = tk.Tk()
button = tk.Button(root, text="A", width=1, height=1)  # Use a single character for better estimation
button.pack()

button_width = button.winfo_width()
button_height = button.winfo_height()
print(f"Button width: {button_width} pixels")
print(f"Button height: {button_height} pixels")

root.mainloop()