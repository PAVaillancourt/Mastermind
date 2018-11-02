#test

error_message = "Invalid selection!"

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

# checks if the pin input is between the accepted values
def pin_check (pin, difficulty):
  if difficulty == "hard":
    if pin not in range(1,9):
      print (error_message)
      return False
    else:
      return True
  elif difficulty == "normal":
    if pin not in range(1,7):
      print (error_message)
      return False
    else:
      return True

# prompts player to select the pins to guess
def pin_choices(difficulty):
  pin_list = []
  if difficulty == "normal":
    for position in ["first", "second", "third", "fourth"]:
      pin = int(input("Select the %s pin (between 1 and 6)" %position))
      while pin_check(pin, difficulty) != True:
        pin = int(input("Select the %s pin (between 1 and 6)" %position))
      pin_list.append(pin)
  elif difficulty == "hard":
    for position in ["first", "second", "third", "fourth", "fifth"]:
      pin = int(input("Select the %s pin (between 1 and 8)" %position))
      while pin_check(pin, difficulty) != True:
        pin = int(input("Select the %s pin (between 1 and 8)" %position))
      pin_list.append(pin)
  return pin_list

# difficulty_selection()
# print(pin_check(3, "normal"))
print(pin_choices(difficulty_selection()))