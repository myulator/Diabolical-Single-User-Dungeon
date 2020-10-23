"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.

Michael and Aaron
"""

import random


def game():
    board = make_board()
    character = make_character()
    achieved_goal = 0 # the number of souls freed; free 5 souls to win the game
    while achieved_goal < 5 and character[2] > 0:
        print(f'You are currently at', character[1],',', character[0])
        direction = get_user_direction()
        valid_move = validate_move(direction, character, board)
        if valid_move:
            move_character(direction, character,)
            encounter(character, achieved_goal)
        else:
            print('You cannot move that way!')
    if achieved_goal == 5:
        print('You have freed the souls of your clansmen! Congratulations!')
    elif character[2] <= 0:
        print('Despite your best efforts, you were slain in combat. Try again!')


def make_board():
    """
    Create 5 x 5 square game board.

    :postcondition: always create a 2-dimensional list representing all positions on the board
    :return: a list of length 5 that contains 5 lists of length 5
    """
    positions_list = []
    for row in range(5):
        positions_list.append([])
        for column in range(5):
            positions_list[row].append(column)
    return positions_list


def make_character():
    """
    Create a character.

    :postcondition: always create a new character that stores its current coordinates, their health (hp), and their name. 
    :return: a list of length 3 that contains the player coordinates, health, and name
    """
    name = input('Welcome to Diabolical: Starter Edition. Please enter your name: ')
    health = 10
    x = 2
    y = 2
    print(f'Welcome, brave', name)
    print('An evil presence has emerged in the small town of Wristrum!')
    print('Quickly now, enter the catacombs and free the tormented souls of your clansmen.')
    return [x, y, health, name]


def get_user_direction():
    """
    Calculate player movement based on user input.
    
    :param character_info: A list that contains the player's x and y position
    :board: A 2d list representing all positions on the board
    :return:
    """
    print('Movement:\n1 or N = North\n2 or S = South\n3 or E = East\n4 or W = West')
    choice = input('In which direction will you move?: ').lower().strip()
    return choice
    
    
def move_character(choice, character_info):
    """
    Change the x or y position of the player depending on user choice

    :param choice: a string or integer that represents player's desired direction
    :param character_info: a list that contains the player's x and y position
    :precondition: choice must be a valid movement input
    :postcondition: adjusts either the x or y position in character_info according to user choice
    :return: a list that contains the player's modified x and y position
    """
    if choice == 1 or 'n' or 'north':
        character_info[1] -= 1
    if choice == 2 or 's' or 'south':
        character_info[1] += 1
    if choice == 3 or 'e' or 'east':
        character_info[0] += 1
    if choice == 4 or 'w' or 'west':
        character_info[0] -= 1
    return character_info


def validate_move(choice, player_info, board):
  """
  Validate if player inputted movement is within boundaries of the board.
  
  :param choice: a string or integer that represents player's desired direction
  :param player_info: a list that contains the player's x and y position 
  :board: A 2d list representing all positions on the board
  :precondition: choice must be a valid movement input
  :postcondition: determines if player movement is possible
  :return: a boolean value
  """
  # Check if player x or y position after movement is a value contained in board.
  valid = False
  if choice == 1 or 'n' or 'north':
    if (player_info[1] - 1) in board[0]:
      valid = True
  if choice == 2 or 's' or 'south':
    if (player_info[1] + 1) in board[0]:
      valid = True
  if choice == 3 or 'e' or 'east':
    if (player_info[0] + 1) in board[0]:
      valid = True
  if choice == 4 or 'w' or 'west':
    if (player_info[0] - 1) in board[0]:
      valid = True
  return valid

def roll_d4():
  """
  Generate a random integer between 1 and 4, inclusively.

  :return: an integer between 1 and 4, both included
  """
  return random.randint(1, 4)
  

def roll_d6():
  """
  Generate a random integer between 1 and 6, inclusively.

  :return: an integer between 1 and 6, both included
  """
  return random.randint(1, 6)


def roll_d10():
  """
  Generate a random integer between 1 and 10, inclusively.

  :return: an integer between 1 and 10, both included
  """
  return random.randint(1, 10)


def roll_d20():
  """
  Generate a random integer between 1 and 20, inclusively.

  :return: an integer between 1 and 20, both included
  """
  return random.randint(1, 20)


def valid_player_input():
  """
  Returns a string.

  Accepts player input and checks for valid player input.

  :precondition: The player inputs a valid string that is either "attack" or "flee", in any case.
  :postcondition: A string representing the player's choice of action.
  :return: A string. # Returns?
  """
  player_action = input("What would you like to do? \nATTACK | FLEE\n").lower().strip()
  
  while player_action not in ["attack", "flee"]:
    player_action = input("Please choose either ATTACK or FLEE\n").lower().strip()
    
  return player_action


def player_combat_turn(enemy_hp):
  """
  Print a series of strings describing combat in the event that you attack first

  Simultes combat if player won the initiative roll. Determines player damage and calculates remaining enemy health
  points.
  
  
  :param: N/A, no paramters accepted.
  :precondition: N/A, this function does not accept parameters.
  :postcondition: Prints two strings and calculates remaining enemy health.
  :return: Prints two strings. # Returns?
  """
  enemy_hp = 5 # for testing
  player_attack_power = roll_d6()
  print("You deal %d damage!" % player_attack_power)
  enemy_hp -= player_attack_power
  return enemy_hp


def enemy_combat_turn(character):
  """
  Print a series of strings describing combat in the event that the enemy attacks first

  Simultes combat if the enemy won the initiative roll. Determines enemy damage and calculates remaining player health points.
  
  
  :param: N/A, no paramters accepted.
  :precondition: N/A, this function does not accept parameters.
  :postcondition: Prints two strings and calculates remaining player health points.
  :return: Prints two strings. # Returns?
  """
  player_hp = 5 # for testing
  enemy_attack_power = roll_d6()
  print("The enemy slashed you for %d damage!" % enemy_attack_power)
  character[2] -= enemy_attack_power
  return character

def flee_success_calculator(character):
  """
  Returns string.

  Calculates the flee success probability, if player fails the roll then enemy damage roll is done, and calcualtes
  remaining player hitpoints.

  :param: N/A, this function does not accept parameters.
  :precondition: N/A, this function does not accept parameters.
  :postcondition: Determines if player successfully flees, if not, calculates player damage taken.
  :return: Prints strings.
  """
  flee_roll = roll_d10()

  if flee_roll > 1:
    print("You successfully run away!")
  else:
    flee_damage = roll_d4()
    character[2] -= flee_damage
    print("The X slices your back as you run away, you take %d damage!" % flee_damage)


def encounter(character, achieved_goal):
  """
  Calls helper function combat_round(), or returns false.

  Determines if the player encounters an enemy. If player encounters an enemy then combat_round() function is called.

  :param: 
  :precondition: 
  :postcondition: Calls combat_round() function if conditional statement are True. ##
  :return: Prints a string, or else calls a helper function.
  """
  # encounter_value = roll_d4()
  encounter_value = 1 # For testing

  if encounter_value == 1:
    print("You see X sprinting towards you...and you prepare to fight!")
    combat_round(character, achieved_goal)
  else:
    return False


def initiative_calculator():
  """
  Returns strin or boolean.

  Determines if the player or the enemy has initiative. Uses conditional statements to determine who goes first.

  :param: N/A, this function does not accept parameters.
  :precondition: N/A, this function does not accept parameters.
  :postcondition: Prints strings and returns booleans based on conditional statements, or else the function
                  calls itself.
  :return: Prints strings and returns booleans.
  """
  input("Press enter to roll for initiative. \n")

  player_speed = roll_d20()
  enemy_speed = roll_d20()

  if player_speed > enemy_speed:
    print("Player first.")
    return True
    
  elif player_speed < enemy_speed:
    print("Enemy first.")
    return False

  elif player_speed == enemy_speed:
    print("Both same time.")
    initiative_calculator()


def combat_round(character, achieved_goal):
  """
  Returns ...

  Drives the combat system. Enemy healthpoints are initialized at 5.
  
  # Would be come after the encounter while function(?)

  # Needs function to determine initiative
 
  # Needs function to determine damage rolls

  # Needs function to print flavor text at beginning of combat, during, and after

  """
  enemy_hp = 5
  # player_hp = 10 # For testing
  # flee = False

  player_action = valid_player_input()
  
  while character[2] > 0 and enemy_hp > 0:

    if player_action == "attack":
      
      if initiative_calculator():
        player_combat_turn(enemy_hp)
        enemy_combat_turn(character)

      else:
        enemy_combat_turn(character)
        player_combat_turn(enemy_hp)
        
    if enemy_hp < 1:
      achieved_goal += 1
      print("You win!")
        

    elif player_action == "flee":
      flee_success_calculator(character)
      
      flee = True
  


  # elif player_hp < 1:
  #   break # Breaks main loop
  




def main():
    """Drives the program."""
    print("Hello, Chris!")

    game()


if __name__ == "__main__":
    main()
