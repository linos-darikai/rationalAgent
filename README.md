# 🤖 Vacuum Cleaner Simulation

## 🌟 Overview
This project simulates an autonomous vacuum cleaner that navigates through a grid-based environment to clean dirt. The simulation features a graphical interface built with tkinter, multiple cleaning strategies, and a customizable grid size.

## 🏗️ Core Components

### 🧹 Dirt Class
- 🖼️ Represents dirt objects on the grid
- 📏 Uses 100x100 pixel images
- ✨ Tracks cleaning state
- 🔒 Private attributes for encapsulation

```python
class Dirt:
    def __init__(self):
        # Loads and resizes dirt image
        # Tracks if the dirt has been cleaned
```

### 📊 Grid Class
- 🎯 Manages the main simulation environment
- 🔲 Creates an NxN button grid
- 🎨 Handles image placement and removal
- 📍 Tracks button and dirt positions

```python
class Grid:
    def __init__(self, n):
        # n: grid size (n x n)
        # Manages button and dirt positions
        # Calculates window dimensions
```

### 🤖 Agent Class
- 🚗 Represents the vacuum cleaner
- 📍 Tracks current position
- 🎮 Handles movement logic
- 🖼️ Displays vacuum cleaner image

```python
class Agent:
    def __init__(self):
        # Loads vacuum cleaner image
        # Sets starting position (0,0)
        # Tracks current position
```

## 🎯 Cleaning Strategies

### 📈 Strategy One
- 🔄 Systematic row-by-row cleaning
- ⏱️ Automated movement with delays
- 📊 Complete coverage pattern

```python
class StrategyOne:
    def __init__(self):
        # Tracks current position
        # Moves systematically through grid
```

### 🎮 Strategy Two
- ⌨️ Manual control (WASD keys)
- 🎯 Direction-based movement
- 🛑 Boundary checking

```python
class StrategyTwo:
    def move(self, direction):
        # Handles WASD movement
        # Checks grid boundaries
```

## 🚀 Getting Started

1. 📁 Ensure required images are in `./img/` directory:
   - `dirt.jpeg`
   - `vacuum_cleaner.jpeg`

2. 🏃‍♂️ Run the simulation:
```python
python vacuum_simulation.py
```

3. 🔢 Enter desired grid size when prompted

4. 🎮 Watch the automated cleaning or use manual controls

## 🎛️ Configuration Options

- 🔲 Grid Size: Customizable via user input
- 🎯 Dirt Density: Adjustable via `populate_grid()` (default 0.2 or 20%)
- ⏱️ Movement Speed: Adjustable via `root.after()` delay (default 500ms)

## 🛠️ Features

1. 📊 **Dynamic Grid Creation**
   - Custom-sized grid based on user input
   - Responsive button layout

2. 🎯 **Random Dirt Generation**
   - Configurable dirt density
   - Random placement algorithm

3. 🤖 **Intelligent Agent**
   - Automatic dirt detection
   - Position tracking
   - Image-based representation

4. 🎮 **Multiple Control Strategies**
   - Automated systematic cleaning
   - Manual control option

## 💡 Implementation Details

### 🔄 Movement Logic
```python
def move_agent(self, position, grid_object):
    # Checks for dirt at new position
    # Updates agent position
    # Updates visual representation
```

### 🎯 Grid Population
```python
def populate_grid(self, degree):
    # Calculates number of dirt spots
    # Randomly distributes dirt
    # Places dirt images
```

## 🤝 Contributing

Feel free to contribute to this project! Some areas for improvement:
- 🎯 Additional cleaning strategies
- 📊 Performance metrics
- 🎨 Enhanced visualization
- 🎮 More user controls

## ⭐ Star the Project!
If you find this simulation helpful, please give it a star! It helps others discover this educational tool.

## 📜 License
This project is open source and available under the MIT License.

## 🐛 Troubleshooting

Common issues:
- 🖼️ Missing image files
- 🎯 Grid size limitations
- 🎮 Control responsiveness

Contact us or open an issue for support!
