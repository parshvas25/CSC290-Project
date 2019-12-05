# Sokoban
A classic arcade game built using Python and Pygame

## Getting started
The instructions listed will help you get a copy of the game running on your local machine.

### Prerequisites
Before starting, you require Python version 3.0 or later. Available here https://www.python.org/downloads/<br />
Along with Python you need Pygame. To download, follow https://www.pygame.org/wiki/GettingStarted
### For ```Windows```
Pygame can easily be installed through command line using either
```
pip install pygame
py -m pip install -U pygame --user
```
### For ```Linux```
Pygame can easily be installed through terminal using
```
sudo apt-get install python3-pygame
```

## Installation
Git clone or download the zip file of the project repository: CSC290-Project 

Link: https://github.com/parshvas25/CSC290-Project.git

### For ```Windows```

If the download was saved to the default Downloads folder...

#### Option 1

Open up the folder in file explorer under

```Downloads\CSC290-Project\Sokoban```

Double click on it to run the game

#### Option 2

Open up the command prompt through Windows search 

Go into the file where the project is located by using 

```cd Downloads\CSC290-Project\Sokoban```

Run the sokoban.py file through the command line:

```python sokoban.py```

### For ```Linux```

If the download was saved to the default Downloads folder

Open up the terminal 

Go into the file where the project is located by using 

```cd Downloads/CSC290-Project/Sokoban```

Run the sokoban.py file by either double clicking on it or through command line:

```python sokoban.py```

## Game Features
* Level selector to play any available level
* Few levels with varying difficulty
* Custom player character sprite

## How to Play
### Controls: 
![Controls - Visual](https://github.com/kchiem198/random_resources/blob/master/controls.png)

| Command | Result |
| --- | --- |
| Arrows keys | Movement |
| Space bar | Reset level |
| Escape key | Return to main menu |
### Gameplay:
* Select any level in the main menu to start
* Player must move into the crate to push it, if nothing blocks it 
* Move all crates into the storage to complete the level
* Advance and complete all levels
		
## Documentation
### Repository Structure: 
The project is split into two main folders

1. Resources
   - The game resources folder contains the fonts, sprites, and sound that the game uses to function. 
   - The main program relies on this folder for the visuals and sounds that the user will hear and see
   
2. Sokoban
   - The Sokoban folder contains the game mechanics and all the logic for the program to function. 
   - Contains the game objects, the menus, the levels, and the main application to run the game, Sokoban.py

### Class and Method Structure:
| Files | Classes | Methods |
| --- | --- | --- |
| sokoban.py | class Sokoban | set_game_object(self, levels)<br />play(self, curr_level) |
| game_object.py | class Player<br />class Crate<br />class Wall<br />class Storage|change_sprite(self)<br />update(walls, crates, storages)<br />move(self, x, y)<br />draw(self, screen) |
| level.py | class Levels | set_level(self, start_level)<br />advance(self)<br />level_n(self) |
| main_menu.py | class Button | on_click(self, event)<br />get_level(self)<br />draw(self, screen)<br />|


### Main Methods:
#### Sokoban.py
- play(self, curr_level):
  * Is where the main game is ran, initializing the pygame variables and settings
  * Takes in user input, such as the arrow key controls to move
  * Updates the screen accordingly to the current state the level is on
  * Allows the user to advance to the next level


#### game_objects.py: 
* Contains all game objects (wall, player, crate, storage) class: 
- move(self, dir_x, dir_y, walls, crates, storages): 
  * Check for object collisions and move each object correspondingly. 
- draw(self, screen): 
  * Drawing functionality to display sprites 

#### level.py: 
* Reads a level layout to make the grid for the current level
* Contains every level the user can play

- advance(self):
  * Allows the game to advance to the next level from 1 to 10
  * Resets the grid and then calls the next level in line

#### main_menu.py:
* Creates the main menu where the user can select a level to play

- on_click(self, event): 
  * Checks pygame rectangle collision with the rectangle boundaries and the mouse position to determine what level was selected

## Contributing
Everyone is welcome to make edits and customize the game to your liking. If you want everyone to enjoy any edits you made, feel free to make a pull request!

Some challenges that may interest you:
* Leaderboard: Compare times for clearing levels!
* Challenges: Time and move limits
* More Levels: Currently, there are only 5 levels in the game.
* Level Creator: Create your own levels!

## Our Contributions
#### Ajay: 
My contributions to the project included writing the logic for the game objects; Player, Crate, and Wall. I also wrote the template for the Pygame application to run, and the ability for Pygame to accept input and translate that into player movement. As for the main menu, I created the ability to select any of the available levels to play, starting and continuing from the level selected.

My contributions to the readme include creating the template for the overall document, and translating the document into the md format for the readme. I wrote the Game features and Contributing sections alone. I also contributed to the Installation and Documentation sections. For the installation, I wrote the Windows guide to installing the game. As for the documentation, I wrote the Repository Structure, and contributed to Main methods. Finally, I looked over the document to ensure that all information was correct and in a readable format.


#### Bingbing: 
My contributions to the project includes organizing and combining team members' code. I organized the classes Player, Crate, Wall, and Storage into one file, game_object.py. Level advancement and layout into the file level.py. I combined the game mechanics together (menu, levels, and player movement) into sokoban.py so we have a fully functional game. My contributions to the README includes creating the rough outline. I added the information in How To Play, Documentation, and the list of ways to contribute in Contributing.


#### Parshva:
For this project my role was to create the menu and level select page of the game. For this my role was to create an appealing menu page that any user will see when first opening the application. To do this I browsed through various fonts and backgrounds that would make the title stand out as well. When beginning the project, I was also responsible for creating a sample level which we then built all the levels of the game.

	As per the Readme, my contributions consisted of adding the installation instructions on Mac, as well as making grammatical checks to ensure the documents contains as few grammatical and spelling errors as possible.



#### Shion:
My main contribution to the project was layout design for each level. I 
organized the layout of wall, crate, storage and player, and stored all the arrangement
information into the nested lists. My role in creating README was to read over the 
document multiple times to fix any minor error and confusion. Also, I modified the 
"how to install" section to clarify some terminology for people who don't have CS
background.


#### Kester:
My contributions to the project encompassed anything related to sound: finding background music and sound effects, as well as writing code for the sound and music during the gameplay.
For this Readme file, I made visuals placed throughout the file (for example, the controls image) as well as proofread and fix any grammatical or flow errors in the text.


## License

Built under MIT License

Game walls and crates taken from https://www.svgrepo.com/svg/53378/brick

