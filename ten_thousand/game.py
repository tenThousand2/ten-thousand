from ten_thousand.game_logic import GameLogic
dice_roller = GameLogic.roll_dice

def play():
  global dice_roller
  print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
  playerInput = input("> ")
  
  if playerInput == 'n':
    print("OK. Maybe another time")
    
  else:
    start_game()
    
def random_roll(score, round, int = 6):
  roll_dice = GameLogic.roll_dice(int)
  print(roll_dice)
  # print(f"*** {roll_dice[0]} {roll_dice[1]} {roll_dice[2]} {roll_dice[3]} {roll_dice[4]} {roll_dice[5]} ***")
  if if_farkled(roll_dice, round):
    return False
  else:
    print("Enter dice to keep, or (q)uit:")
    playerInput = input("> ")
    if playerInput == "q":
      quit_game(score)
    else:
      return playerInput
  
def bank_or_roll(calc_points, dice_remaining):
  if dice_remaining > 0:
    print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    playerInput = input("> ")
    return playerInput
  else:
    print(f"You have {calc_points} and {dice_remaining}")
    print("(b)ank your points or (q)uit:")
    playerInput = input("> ")
    return playerInput

def count_dice(dice):
    counts = {}
    for num in dice:
        counts[num] = counts.get(num, 0) + 1
    return counts
  
# def if_farkled(takes in dice roll):
#   if any dice number is equal to 1 and or 5 and or 3ofaKind or 3 pairs
#   prompt the user to bank dice of their choice
#   if they can bank all die and choose to do so move on to the next round and roll new die
#   if they bank some die and decide to roll again, if the new rolls are not 1 and or 5 and or 3ofaKind they will get farkled and will lose their points for this round and will move on to the next round

def if_farkled(dice, round):
  round += 1
  if 1 not in dice and 5 not in dice or GameLogic.calculate_score(dice) == 0:
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
    dice = random_roll(total_score, round, dice_leftovers)
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