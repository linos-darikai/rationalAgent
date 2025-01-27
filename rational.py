from PIL import Image, ImageTk
import tkinter as tk
import random
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
    def populate_grid(self, degree):
        num_dirt = round(degree * (n **2))
        counter = 0
        for i in self.__button_positions:
            if counter == num_dirt:
                break
            random_num = random.random()
            if random_num > 0.5:
                dirt = Dirt()
                self.__dirt_positions[i] = dirt
                self.place_image(i, dirt)
                counter += 1

    def place_image(self, position, dirt_object):
        button = self.__button_positions[position]
        if dirt_object.get_img() is not None:
            button.config(image=dirt_object.get_img())


class Agent:
    def __init__(self):
        self.__strategy= []
        image_path = "./img/vaccum_cleaner.jpeg"
        self.__start_position = (0,0)
        try:
            img = Image.open(image_path)
            img = img.resize((100, 100))

            self.__img = ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found. Using a default image.")
            self.__img = None

    
    def get_strategy(self):
        return self.__strategy
    def get_start_pos(self):
        return self.__start_position
    def start(self, grid_object):
        if self.__start_position in grid_object.get_dirt_positions():
            grid_object.place
        #check if starting position has dirt
            #if it does remove it replace with the agent image
        
    
    def move(self, direction):
        #can move left right and up and down
        # we can use the tuple to move up x and left and right with y
    
    def remove_dirt(self, grid_object):
        # remove the image from the button replace with 

    
    

    #strategy functions here
    # they would mostly focus on movement and how they move




                
        
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid Simulation")

    n = int(input("Enter grid size (N): ")) 
    grid = Grid(n)
    window_width = grid.get_width()
    window_height = grid.get_height()
    root.geometry(f"{window_width}x{window_height}") 

    grid.create_grid(root)
    grid.populate_grid(0.3)

    root.mainloop()


    


    
