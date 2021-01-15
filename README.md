[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=312532&assignment_repo_type=GroupAssignmentRepo)
# Diabolical: Starter Edition | BCIT CST COMP1510 Midterm Hackathon
Developers: Michael Yu & Aaron Tansley
Date: October 2020

This single-user dungeon was developed during the 6-hour midterm hackathon for COMP 1510 at BCIT, supervised by Chris Thompson.

# Game design:
In the early days of internet and computing, gamers used to dial into things called multi-user dungeons (MUDs). MUDs were text-based real-timerole-playing adventure games that let users read descriptions about rooms, objects, other players, non-player characters, etc., and perform actions and interact with the virtual world. We have not learned how to use python for networking yet, so this project is a single-user dungeon (SUD) readily playable in CLI.

The game is played on a square 5 x 5 board.  
Player location is stored using (x, y) coordinates.  
The game maps squares from north to south (0 -> 4)  
The game maps squares from west to east (0 -> 4)  
i.e.: The square in the top-left of the board has the coordinates (0, 0)

# Gameplay - General:
The player must find and defeat 3 enemies without dying to beat the game.  
Player begins the game with 10 health. All enemies have 5 health.
Damage inflicted during combat is random (between 1 and 6 damage).

# Gameplay - Movement:
Player always moves 1 square north, south, east, or west.  
Player cannot move outside the bounds of the 5 x 5 dungeon.  
Every time the player moves, there is a 25% chance that a monster encounter will occur.
Every time the player moves and does not enounter a monster, they heal for 2 health.

# List of functions:  
game   
make_board    
make_character   
get_user_direction  
move_character  
validate_move  
roll_d4  
roll_d6  
roll_d10  
roll_d20  
player_combat_turn   
enemy_combat_turn   
flee_success_calculator  
encounter  
initiative_calculator  
combat_round  
