from PIL import Image, ImageTk
import tkinter as tk
import random
import time
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
    def create_grid(self, parent):
        """
        Function creates the grid and put the pos in a dirt positions
        parent: the parent widget (frame) where the grid will be created
        """
        for i in range(self.__n):
            parent.grid_rowconfigure(i, weight=1)
            parent.grid_columnconfigure(i, weight=1)
            for j in range(self.__n):
                button = tk.Button(parent, width=5, height=5, padx=10, pady=10)
                button.grid(row=i, column=j, sticky="nsew")
                self.__button_positions[(i, j)] = button
   
    def populate_grid(self, degree):
        """
        Fuction populates the grid with the degree or extent
        degree : float
        """
        num_dirt = round(degree * (self.__n **2)) # talk about access of variebles in classes
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

    def place_image(self, position, img_object):
        """
        Fuction places the image in a button at position
        position : tuple of position(x, y)
        img_object: either dirt obj or agent obj
        """
        button = self.__button_positions[position]
        if img_object.get_img() is not None:
            button.config(image=img_object.get_img())
    def remove_image(self, position):
        """
        Function removes an image at position leaving nothing
        position: (int, int)
        """
        button = self.__button_positions[position]
        if button.cget('image'):
            button.config(image='')
            self.__button_positions[position] = button

    def remove_dirt_obj(self, position):
        """
        Function removes dirt in position 
        position: tuple
        """
        if position in self.__dirt_positions:
            self.__dirt_positions.pop(position)
        




class Agent:
    def __init__(self):
        self.__strategy= []
        image_path = "./img/vaccum_cleaner.jpeg"
        self.__start_position = (0,0)
        self.__current_position = self.__start_position
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
    def get_img(self):
        return self.__img
    def get_current_position(self):
        return self.__current_position
    def set_current_position(self, position):
        """
        Function sets the current position of the agent
        position: tuples (int, int)
        """
        self.__current_position = position

    def start(self, grid_object):
        """
        Fuction puts the agent object at the starting object
        grid_object: the actual grid object
        """
        print("power")
        if self.__img:
            print("seen")
            self.move_agent(grid_object=grid_object, position= self.__start_position)
        else:
            print("No img")
    def strategy_one(self):
        """
        Function mimicks
        """
    
    def move_agent(self, position, grid_object):
        """
        Function removes the dirt object from dict and removes img
        grid_object: actual grid object
        """
        if position in grid_object.get_dirt_positions():
            print("hit")
            grid_object.place_image(position, self)
            grid_object.remove_image(self.__current_position)
            self.set_current_position(position)
            print("hitaable")
            grid_object.remove_dirt_obj(position)
        else:
            print("hitaable")
            grid_object.place_image(position, self)
            grid_object.remove_image(self.__current_position)
            self.set_current_position(position)
   # Create a class to handle the animation state
class StrategyOne:
    def __init__(self):
        self.current_i = 0
        self.current_j = 0
        
    def operate_agent(self):
        if self.current_i < n:
            agent.move_agent((self.current_i, self.current_j), grid)
            
            # Update position
            self.current_j += 1
            if self.current_j >= n:
                self.current_j = 0
                self.current_i += 1
            
            if self.current_i < n:
                root.after(500, self.operate_agent)  # 500ms = 0.5 second delay

    
    

    #strategy functions here
    # they would mostly focus on movement and how they move




                
        
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid Simulation")
    
    n = int(input("Enter grid size (N): ")) 
    grid = Grid(n)
    agent = Agent()
    window_width = grid.get_width()
    window_height = grid.get_height()
    # Setting the size of the window
    root.geometry(f"{window_width}x{window_height}")
    #Creating a frame to pack our buttons
    frame = tk.Frame(root)
    #using the grid packing manager
    frame.grid(row=0, column=0, sticky="nsew")
    
    # Configure root grid weights
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    grid.create_grid(frame) 
    #populating grid with dirt 
    grid.populate_grid(0.2)
    agent.start(grid)

    
    controller = StrategyOne()
    controller.operate_agent()
    
    root.mainloop()

    

    


    
