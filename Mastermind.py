# Pierre Antoine Vaillancourt
# Last edit 2019-01-19

import random
error_message = "Please make a valid selection."

# difficulty: normal (4 pins, 6 colours) or hard (5 pins, 8 colours)
def difficulty_selection():
  chosen_difficulty = ""
  while chosen_difficulty != "hard" or chosen_difficulty != "normal":
    chosen_difficulty = input("Select your difficulty (normal or hard):")
    chosen_difficulty = chosen_difficulty.lower()
    if chosen_difficulty == "hard" or chosen_difficulty == "normal":
      return chosen_difficulty
    else:
      print (error_message)

# checks if entered pin is within accepted range
def single_pin_check(pins, difficulty):
  if difficulty == "hard":
    highest_pin = "8"
  elif difficulty == "normal":
    highest_pin = "6"
  for i in range(len(pins)):
    if pins[i] < "1" or pins[i] > highest_pin:
      return False
  return True

# checks if the pin input is between the accepted values
def pin_check (pins, difficulty):
  if difficulty == "hard":
    max_pins_lgth = 5
  elif difficulty == "normal":
    max_pins_lgth = 4
  if len(pins) != max_pins_lgth or single_pin_check(pins, difficulty) != True:
    print (error_message)
    return False
  else:
    return True

# prompts player to select the pins to guess
def pin_choices(difficulty):
  pin_list = []
  if difficulty == "normal":
    pin_input_message = "Select the four pins (between 1 and 6)"
  elif difficulty == "hard":
    pin_input_message = "Select the five pins (between 1 and 8)"
  pin_list_raw = input(pin_input_message)
  pin_list = [c for c in pin_list_raw]
  while pin_check(pin_list, difficulty) != True:
    pin_list_raw = input(pin_input_message)
    pin_list = [c for c in pin_list_raw]
  return pin_list

# chooses a random string of 4 or 6 pins for the player to guess
def code_generator(difficulty):
  pin_list = []
  if difficulty == "normal":
    available_pins = [1,1,2,2,3,3,4,4,5,5,6,6]
    code_length = 4
  elif difficulty == "hard":
    available_pins = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
    code_length = 5
  for i in range(code_length):
    chosen_pin = random.choice(available_pins)
    pin_list.append(chosen_pin)
    available_pins.remove(chosen_pin)
  return pin_list

# prints the board in the console
def print_board(pin_code, guessed_rows, difficulty, victory):
  board = ""
  
  if difficulty == "hard":
    # top row
    if victory == 1 or victory == -1:
      # revealed top row
      board += """
 _____________________________
| _-*-_   MASTER MIND   _-*-_ |
|===========|=================|
|           |  """
      for i in pin_code:
        board += str(i) 
        board += "  "
      board +=  "|\n|___________|_________________|"


    else:
      # hidden top row
      board += """
 _____________________________
| _-*-_   MASTER MIND   _-*-_ |
|===========|=================|
|           |  X  X  X  X  X  |
|___________|_________________|"""

    # empty rows
    for i in range(12-len(guessed_rows)):
      board += """
|           |                 |
|           |                 |
|___________|_________________|"""

    # rows containing guesses
    for i in range(len(guessed_rows)):
      board += guessed_rows[i] 
    
    #bottom row
    board += """
|           |                 |
|===========|=================|
|___________|_________________|"""

  elif difficulty == "normal":
    # top row
    if victory == 1 or victory == -1:
      # revealed top row
      board += """
 _____________________________
| _-*-_   MASTER MIND   _-*-_ |
|===========|=================|
|           |  """
      for i in pin_code:
        board += str(i) 
        board += "  "
      board +=  "   |\n|___________|_________________|"

    else:
      # hidden top row
        board += """
 _____________________________
| _-*-_   MASTER MIND   _-*-_ |
|===========|=================|
|           |  X  X  X  X     |
|___________|_________________|"""

    # empty rows
    for i in range(12-len(guessed_rows)):
      board += """
|           |                 |
|           |                 |
|___________|_________________|"""

    # rows containing guesses
    for i in range(len(guessed_rows)):
      board += guessed_rows[i] 
    
    #bottom row
    board += """
|                             |
| x: correct number and place |
| o: correct number           |
|_____________________________|"""

  return board

# returns a table containing rows containing clue pins and guessed pins
def print_row(pin_choice, clue_pins, difficulty):
  row = "\n|           |                 |"
  row += "\n"
  row += "| "
  if difficulty == "hard":
    for i in clue_pins:
      row += (i+" ")

    row += "|  "
    for i in range(len(pin_choice)):
      row += str(pin_choice[i])
      row += "  "
    row += "|\n"
  
  elif difficulty == "normal":
    for i in clue_pins:
      row += (i+" ")

    row += "  |  "
    for i in range(len(pin_choice)):
      row += str(pin_choice[i])
      row += "  "
    row += "   |\n"

  row += "|___________|_________________|"

  return row

# returns a list of clue pins
def clue_pins_generator(guessed_pins, pin_code):
  dummy_guessed_pins = guessed_pins.copy()
  dummy_pin_code = pin_code.copy()

  clue_pins = {"x":0, "o": 0, " ":0}

  for i in range(len(dummy_guessed_pins)):
    for j in range(i, len(dummy_pin_code)):
      if dummy_guessed_pins[i] == dummy_pin_code[j]:
        if i != j:
          continue
        elif i == j:
          clue_pins["x"] += 1
          dummy_pin_code[j] = 9
          dummy_guessed_pins[i] = 0
          break

  for i in range(len(dummy_guessed_pins)):
    for j in range(len(dummy_pin_code)):
      if dummy_guessed_pins[i] == dummy_pin_code[j]:
        clue_pins["o"] += 1
        dummy_pin_code[j] = 9
        dummy_guessed_pins[i] = 0
        break

  for i in range(len(dummy_guessed_pins)):
    # no identical unmatched pin left  
    if dummy_guessed_pins[i] not in dummy_pin_code and dummy_guessed_pins[i] != 0:
      clue_pins[" "] += 1

  clue_pins_list = []
  clue_pins_list += (["x"]*clue_pins["x"]) + (["o"]*clue_pins["o"]) + ([" "]*clue_pins[" "])
  return clue_pins_list

# converts a list of characters to a list of integers
def char_to_int(char_list):
  int_list = []
  for i in char_list:
    int_list.append(int(i))
  return int_list

# return true if player wants to play again or false if not
def play_again():
  answer = input("Play again?")
  if answer in ["Yes", "yes", "y"]:
    return True
  elif answer in ["No", "no", "n"]:
    return False
  elif answer == "maybe".lower():
    print("Make up your mind!")
    return play_again()
  else:
    print (error_message)
    return play_again()

# main game 
def mastermind():
  difficulty = difficulty_selection()
  code = code_generator(difficulty)
  guesses_left = 12
  victory = 0
  guesses = []
  print(print_board(code, guesses, difficulty, victory))

  while guesses_left > 0 and victory == 0:
    guess_char = pin_choices(difficulty)
    guess = char_to_int(guess_char)
    clues = clue_pins_generator(guess, code)
    guesses.insert(0,print_row(guess, clues, difficulty))
    if guess == code:
      victory = 1
    elif guesses_left == 1:
      victory = -1
    print(print_board(code, guesses, difficulty, victory))
    guesses_left -= 1
  
  if victory == 1:
    print("\nVictory!")
  else:
    print("\nBetter luck next time!")
  if play_again():
    mastermind()
  else:
    print("Thank you for playing!")



# TODO
# settings (board length, number of pins to guess, number of numbers)
# bot

# Tests

#difficulty_selection()
#print(pin_check([9,8,9,8,9], "hard"))
#pin_choices("normal")
#print(code_generator("hard"))
#print(print_board([1,2,3,4,5],[print_row([1,2,3,4,5],[1,1,0,-1,-1]),
#print_row([1,9,3,4,5],[1,0,0,-1,-1])
#print_row([1,2,3,4,5],[1,1,0,-1,-1])
#print(clue_pins_generator([2,2,3,4,5],[9,8,3,3,4])==["x","o"," "," "," "])
#print(clue_pins_generator([1,2,6,1,1],[1,2,6,7,1]))
#print(clue_pins_generator([2,2,3,4,5],[9,8,3,3,4])==["x","o"," "," "," "])
#print(clue_pins_generator([1,1,2,1,1],[1,2,1,1,2]))
#pin_check([1,2,3,4,9], "hard")

mastermind()