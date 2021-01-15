"""
COMP-1510-Midterm-Hackathon
Single User Dungeon (SUD)

Michael Yu and Aaron Tansley
"""

import random
import time

def game():
    board = make_board()
    character = make_character()
    end_game = 0

    while character[2] > 0 and end_game != 'exit' and character[4] != 5:
        time.sleep(1)
        print(f'\nYou are currently at', character[1],',', character[0])
        direction = get_user_direction()
        valid_move = validate_move(direction, character, board)
        
        if valid_move == True:
            move_character(direction, character)
            encounter(character)

        if valid_move == "exit":
            print('Game ended by user. Safe travels.')
            end_game = 'exit'
            
        elif valid_move == False:
            print('You cannot move that way!')

    if character[4] == 5:
        print('You have freed the souls of your clansmen! Congratulations!')
    elif character[2] <= 0:
        print('Despite your best efforts, you were slain in combat. Game over!')


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
    time.sleep(1)
    name = input('Welcome to Diabolical: Starter Edition. Please enter your name: ')
    health = 10
    x = 2
    y = 2
    achieved_goal = 0 # the number of enemies killed; kill 5 to win the game
    print(f'\nWelcome, brave', name)
    time.sleep(2)
    print('\nAn evil presence has emerged in the small town of Wristrum!')
    time.sleep(2)
    print('Quickly now, enter the catacombs and free the tormented souls of your clansmen.')
    return [x, y, health, name, achieved_goal]


def get_user_direction():
    """
    Calculate player movement based on user input.
    
    :param character_info: A list that contains the player's x and y position
    :return:
    """
    print('\nMovement:\n1 or N = North\n2 or S = South\n3 or E = East\n4 or W = West')
    choice = input('\nIn which direction will you move?: ').lower().strip()
    return choice
    
    
def move_character(choice, character_info):
    """
    Change the x or y position of the player depending on user choice

    :param choice: a string or integer that represents player's desired direction
    :param character_info: a list that contains the player's x and y position
    :precondition: choice must be a valid movement input
    :postcondition: adjusts either the x or y position in character_info according to user choice
    :return: a list that contains the player's modified x and y position

    >>> print(move_character("3", [2, 2, 10, 'name']))
    [3, 2, 10, 'name']
    >>> print(move_character("s", [3, 1, 5, 'name']))
    [3, 2, 5, 'name']
    >>> print(move_character("west", [4, 0, 7, 'name']))
    [3, 0, 7, 'name']
    >>> print(move_character("n", [3, 3, 9, 'name']))
    [3, 2, 9, 'name']
    """
    if choice == '1' or choice == 'n' or choice == 'north':
        character_info[1] -= 1
        return character_info
    if choice == '2' or choice == 's' or choice == 'south':
        character_info[1] += 1
        return character_info
    if choice == '3' or choice == 'e' or choice == 'east':
        character_info[0] += 1
        return character_info
    if choice == '4' or choice == 'w' or choice == 'west':
        character_info[0] -= 1
        return character_info


def validate_move(choice, player_info, board):
  """
  Validate if player inputted movement is within boundaries of the board.
  
  :param choice: a string or integer that represents player's desired direction
  :param player_info: a list that contains the player's x and y position 
  :parapm board: A 2d list representing all positions on the 
  :precondition: choice must be a valid movement input
  :postcondition: determines if player movement is possible
  :return: a boolean value or a string to quit the game
  
  >>> print(validate_move('1', [2, 2, 10, 'name']))
  True
  >>> print(validate_move('east', [4, 3, 3, 'name']))
  False
  >>> print(validate_move('1', [0, 2, 8, 'name']))
  False
  >>> print(validate_move('w', [0, 1, 8, 'name']))
  False
  >>> print(validate_move('2', [3, 4, 8, 'name']))
  False
  """
  # Check if player x or y position after movement is a value contained in board.
  valid = False
  if choice == '1' or choice == 'n' or choice == 'north':
    if (player_info[1] - 1) in board[0]:
      valid = True
      return valid
  if choice == '2' or choice == 's' or choice == 'south':
    if (player_info[1] + 1) in board[0]:
      valid = True
      return valid
  if choice == '3' or choice == 'e' or choice == 'east':
    if (player_info[0] + 1) in board[0]:
      valid = True
      return valid
  if choice == '4' or choice == 'w' or choice == 'west':
    if (player_info[0] - 1) in board[0]:
      valid = True
      return valid
  if choice == 'quit':
      valid = 'exit'
      return valid
  else:  
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

  return player_action


def player_combat_turn(enemy_hp):
  """
  Print a series of strings describing combat in the event that you attack first.
  
  Simulates combat if player won the initiative roll. Determines player damage and calculates remaining enemy health points.
  
  :param enemy_hp: integer represents current enemy health
  :precondition: enemy_hp must be > 0
  :postcondition: prints combat information and calculates remaining enemy health.
  :return: the modified enemy health value as an integer
  """
  player_attack_power = roll_d6()
  time.sleep(1)
  print("You deal %d damage!" % player_attack_power)
  print("The enemy shrieks menacingly. \n")
  enemy_hp -= player_attack_power
  return enemy_hp


def enemy_combat_turn(character):
  """
  Print a series of strings describing combat in the event that the enemy attacks first

  Simulates combat if the enemy won the initiative roll. Determines enemy damage and calculates remaining player health points.
  
  :param character: Accepts a list that contains player health and kill count.
  :precondition: A list containing 3 integers and a string, in that order.
  :postcondition: Prints two strings and calculates remaining player health points.
  :return: Prints two strings.
  """
  enemy_attack_power = roll_d6()
  time.sleep(1)
  print("The enemy slashed you for %d damage!\n" % enemy_attack_power)
  character[2] -= enemy_attack_power
  return character


def flee_success_calculator(character):
  """
  Returns string.

  Calculates the flee success probability, if player fails the roll then enemy damage roll is done, and calcualtes
  remaining player hitpoints.

  :param character: Accepts a list that contains player health and kill count.
  :precondition: A list containing 3 integers and a string, in that order.
  :postcondition: Determines if player successfully flees, if not, calculates player damage taken.
  :return: Prints strings.
  """
  flee_roll = roll_d10()

  if flee_roll > 1:
    time.sleep(1)
    print("You successfully escape the encounter!")

  else:
    flee_damage = roll_d4()
    character[2] -= flee_damage
    time.sleep(1)
    print("The enemy slices your back as you run away, you take %d damage!" % flee_damage)
    

def encounter(character):
  """
  Calls helper function combat_round(), or returns false.

  Determines if the player encounters an enemy. If player encounters an enemy then combat_round() function is called.

  :param character: Accepts a list that contains player health and kill count.
  :precondition: A list containing 3 integers, a string, and 1 integer, in that order.
  :postcondition: Calls combat_round() function if conditional statement are True. 
  :return: Prints a string, or else calls a helper function.
  """
  encounter_value = roll_d4()

  # Conditional statement if the player does have an encounter
  if encounter_value == 1:
    print("\nAn Undead Clansman has found you.\n")
    return combat_round(character)
    
  elif encounter_value != 1:
    
    if character[2] + 2 > 10:
      character[2] = 10
      print(f'Your hp is full: ', character[2])
      return character
      
    else:
      character[2] += 2
      print(f'You recover 2 hp. Your hp is now: ', character[2])
      return character


def initiative_calculator():
  """
  Return string or boolean.

  Determines if the player or the enemy has initiative. Uses conditional statements to determine who goes first.

  :postcondition: Prints strings and returns booleans based on conditional statements, or else the function calls itself.
  :return: Prints strings and returns booleans.
  """
  input("\nPress enter to roll for initiative. \n")

  player_speed = roll_d20()
  enemy_speed = roll_d20()

  # Checks for who rolled higher for initiative
  if player_speed > enemy_speed:
    print("You strike first!")
    return True
    
  elif player_speed < enemy_speed:
    print("The enemy strikes first.")
    return False

  elif player_speed == enemy_speed:
    print("Both you and your enemy whiff attacks!")
    initiative_calculator()


def combat_round(character):
  """
  Drives the combat system. Enemy healthpoints are initialized at 5.
  
  :param character: Accepts a list that contains player health and kill count.
  :precondition: A list containing 3 integers, a string, and 1 integer, in that order.
  :postcondition: Calculates player health and kill count after combat or flee scenario
  :return: Boolean, integer, and/or string(s).
  """
  enemy_hp = 5 # Enemy healthpoints set at 5.
  flee = False # Flee set to false

  # Checks for valid user input and and cleans input
  player_action = valid_player_input()
  
  # Main loop that drives the combat system
  while character[2] > 0 and enemy_hp > 0 and flee == False:

    if player_action == "attack":
      
      if initiative_calculator():
        enemy_hp = player_combat_turn(enemy_hp)
        enemy_combat_turn(character)
        
      else:
        enemy_combat_turn(character)
        enemy_hp = player_combat_turn(enemy_hp)
    
    if enemy_hp < 1:
      print("You have defeated the enemy!")
      
    elif player_action == "flee":
      flee_success_calculator(character)
      flee = True

  character[4] += 1
  return character
  

def main():
    """Drives the program."""
    print("Hello, wanderer.")

    game()


if __name__ == "__main__":
    main()
