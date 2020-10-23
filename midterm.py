"""
This file must contain your main function. This is the file
the repl.it interpreter will execute using the command python game.py.

Michael and Aaron
"""

import random


def game():
    board = make_board()
    character = make_character()
    player_hp = 10
    player_coords = (board, board) # (horizontal from left to right, vertical from top to bottom)
    achieved_goal = 0 # the number of souls freed; free 5 souls to win the game
    while achieved_goal < 5 and player_hp > 0:
        print(f'You are currently at', player_coords)
        direction = get_user_direction()
        valid_move = validate_move(direction)
        if valid_move:
            move_character(player_coords)
            encounter()
        else:
            print('You cannot move that way!')
    if achieved_goal == 5:
        print('You have freed the souls of your clansmen! Congratulations!')
    elif player_hp <= 0:
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
    return [x, y, health, name]


def get_user_direction(character_info, board):
    """
    Calculate player movement based on user input.
    
    :param character_info: A list that contains the player's x and y position
    :board: A 2d list representing all positions on the board
    :return:
    """
    choice = input('Where would you like to go: (North, South, East or West)').lower().strip()
    valid_move = validate_move(choice, player_info, board)
    if valid_move is True:
        if choice is 'n' or 'north':
            character[1] -= 1
        if choice is 's' or 'south':
            character[1] += 1
        if choice is 'e' or 'east':
            character[0] += 1
        if choice is 'w' or 'west':
            character[0] -= 1
    return character_info


def validate_move(choice, player_info, board):
  """
  Validate if player inputted movement is possible
  
  :param choice: a string representing player's desired direction
  :param player_info: a list that contains the player's x and y position 
  :board: A 2d list representing all positions on the board
  :return: a boolean value
  """
  # Something to do with checking if player_coords are < 0 or > 4
  if choice is 'n' or 'north':
    if board[character[1]] - 1 == -1:
      valid = False
    else:
      valid = True
     
  if choice is 's' or 'south':
    if board[character[1]] + 1 == 5:
      valid = False
    else:
      valid = True
  if choice is 'e' or 'east':
            character[0] += 1
  if choice is 'w' or 'west':
            character[0] -= 1
  

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
  return random.randint(1,20)


def player_combat_simulator():
  player_hp = 10 # For testing
  player_attack_power = roll_d6()
  enemy_attack_power = roll_d6()

  print("You strike the enemy for %d damage!" % player_attack_power)
  print("The enemy slashed you for %d damage!" % enemy_attack_power)

  player_hp -= enemy_attack_power

  return player_attack_power

def flee_success_calculator():
  """

  Calculates the flee success probability

  """
  flee_roll = roll_d10()

  if flee_roll > 1:
    print("You successfully run away!")
  else:
    flee_damage = roll_d4()
    player_hp -= flee_damage
    print("The X slices your back as you run away, you take %d damage!" % flee_damage)


def encounter():
  # encounter_value = roll_d4()
  encounter_value = 1 # For testing

  if encounter_value == 1:
    print("You see X sprinting towards you...and you prepare to fight!")

    combat_round()


def initiative_calculator():
  """
  Returns strin or boolean.

  Determines if the player or the enemy has initiative.

  """
  input("Please press enter to roll for initiative. \n")

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


def combat_round():
  """
  Returns 

  Drives the combat system.
  
  # Would be come after the encounter while function(?)

  # Needs function to determine initiative
 
  # Needs function to determine damage rolls

  # Needs function to print flavor text at beginning of combat, during, and after

  """
  enemy_hp = 5
  player_hp = 10 # For testing
  flee = False


  player_action = input("What would you like to do? \nATTACK | FLEE\n").lower().strip()


  while player_hp > 0 and enemy_hp > 0 and flee == False:

    if player_action == "attack":
      
      if initiative_calculator():
        player_attack_power = roll_d6()
        print("You strike the X for %d" % player_attack_power)
        enemy_hp -= player_attack_power

      else:
        enemy_attack_power = roll_d6()
        print("The X moves like the wind and strikes you for %d damage!" % enemy_attack_power)
        player_hp -= enemy_attack_power
      
    elif player_action == "flee":
      flee_success_calculator()
      flee = True
  


  # elif player_hp < 1:
  #   break # Breaks main loop
  




def main():
    """Drives the program."""
    print("Hello, Chris!")

    game()


if __name__ == "__main__":
    main()
