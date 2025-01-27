from PIL import Image, ImageTk
import tkinter as tk
class Dirt:
    def __init__(self):
        image_path = "./img/dirt.jpeg"
        try:
            img = Image.open(image_path)
            img = img.resize((100, 100))

            self.__img = ImageTk.PhotoImage(img)
            self.__cleaned = False
           
        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found. Using a default image.")
            self.__img = None
            self.__cleaned = False

    def get_img(self):
        return self.__img
    def get_clean_state(self):
        return self.__cleaned
    def clean(self):
        self.__cleaned = True

class Grid:
    def __init__(self, n):
        self.__button_positions = {}
        self.__dirt_positions = {}
        self.__n = n
        self.__window_width = n * 200
        self.__window_height= n * 200

    def get_button_pos(self):
        return self.__button_positions
    def get_dirt_positions(self):
        return self.__dirt_positions
    def get_width(self):
        return self.__window_width
    def get_height(self):
        return self.__window_height
    def create_grid(self, root):
        for i in range(self.__n):
            for j in range(self.__n):
                button = tk.Button(root, width=5, height=5, padx=10, pady=10)
                button.grid(row=i, column=j, sticky="nsew")
                self.__button_positions[(i, j)] = button
                
        
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid Simulation")

    # Get grid size from user input
    n = int(input("Enter grid size (N): ")) 
    grid = Grid(n)
    window_width = grid.get_width()
    window_height = grid.get_height()
    root.geometry(f"{window_width}x{window_height}") 

    grid.create_grid(root)

    root.mainloop()


    


    
