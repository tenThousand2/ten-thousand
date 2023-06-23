from ten_thousand.game_logic import GameLogic
from collections import Counter
dice_roller = GameLogic.roll_dice

def play():
  global dice_roller
  print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
  playerInput = input("> ")
  playerInput = playerInput.replace(" ", "") 
  
  if playerInput.lower() == 'n':
    print("OK. Maybe another time")
  elif playerInput.lower() == "y":
    start_game()
  else:
    print("put in y or n")
    play()
    

def roll_dice(int):
  roll_dice = GameLogic.roll_dice(int)
  print(roll_dice)
  return roll_dice

def random_roll(score, round, dice, int = 6):
  # print(f"*** {roll_dice[0]} {roll_dice[1]} {roll_dice[2]} {roll_dice[3]} {roll_dice[4]} {roll_dice[5]} ***")
  if if_farkled(dice, round):
    return False
  else:
    while True:
      print("Enter dice to keep, or (q)uit:")
      playerInput = input("> ")
      playerInput = playerInput.replace(" ", "") 
      if playerInput == "q":
        quit_game(score)
      dice_list = Counter(dice)
      formatted = format_player_input(playerInput)
      players_choice = Counter(formatted)
      if playerInput == "q":
        quit_game(score)
      if all(dice_list[element] >= count for element, count in players_choice.items()):
        return playerInput
      else:
        print("Cheater!!! Or possibly made a typo...")
        continue
        # random_roll(score, round, dice, int)
  
def bank_or_roll(calc_points, dice_remaining):
  if dice_remaining > 0:
    print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    playerInput = input("> ")
    playerInput = playerInput.replace(" ", "") 
    return playerInput
  else:
    print(f"You have {calc_points} and {dice_remaining}")
    print("(b)ank your points or (q)uit:")
    playerInput = input("> ")
    playerInput = playerInput.replace(" ", "") 
    return playerInput

def count_dice(dice):
    counts = {}
    for num in dice:
        counts[num] = counts.get(num, 0) + 1
    return counts

def if_farkled(dice, round):
  round += 1
  if 1 not in dice and 5 not in dice and GameLogic.calculate_score(dice) == 0:
    print("Farkle!")
    print(f"You lost all your unbanked points. Round {round}")
    return True
  else:
    return False
  
def dice_left(intPlayerInput, dice_to_go):
  randomRoll = dice_roller(dice_to_go)
  dice_remaining = len(randomRoll) - len(intPlayerInput)
  return dice_remaining
  
def unbanked_points_message(round, total_score, calc_points, dice_remaining):
  # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")

def quit_game(total_score):
  print(f"Thanks for playing. You earned {total_score} points")
  quit()
  
def start_game():
  total_score = 0
  calc_points = 0
  round = 1
  dice_leftovers = 6

  while True:
    if total_score == 10000:
      print("you win")
      quit_game(total_score)
    roll = roll_dice(dice_leftovers)
    dice = random_roll(total_score, round, roll, dice_leftovers)
    if dice == False:
      calc_points = 0
      round += 1
      dice_leftovers = 6
      continue
    else:
      dice_leftovers = dice_left(dice, dice_leftovers)
      calc_points += GameLogic.calculate_score(format_player_input(dice))
      playerInput = bank_or_roll(calc_points, dice_leftovers)
      if playerInput == "b":
        print(f"""You banked {calc_points} points in round {round}
  Total score is {total_score} points""")
        total_score += calc_points
        round += 1
        calc_points = 0
        print(f"Starting round {round}\nRolling 6 dice...")
        dice_leftovers = 6
        continue
      if playerInput == "r":  
        continue
        # random_roll(dice_remaining, round, total_score)
      if dice_leftovers == 0:
          print("Sorry, no rolls left")
          calc_points = 0
          round += 1
          dice_leftovers = 6
          continue
      if playerInput == "q":
        quit_game()
      else:
        unbanked_points_message(round, total_score, calc_points, dice_leftovers)
  
def format_player_input(player_input_string):
  int_list = []
  for i in range(len(player_input_string)):
    int_list.append(int(player_input_string[i]))
  return int_list

if __name__ == "__main__":
  play()