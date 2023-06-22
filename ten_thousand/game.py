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
    
def random_roll(int, round, score):
  # print("AAAAAAAA round inside radnom roll ", round)
  roll_dice = GameLogic.roll_dice(int)
#   print(f"""Starting round {round}
# Rolling {int} dice...""")
  # randomRoll = dice_roller
  print(f"*** {roll_dice[0]} {roll_dice[1]} {roll_dice[2]} {roll_dice[3]} {roll_dice[4]} {roll_dice[5]} ***")
  print("Enter dice to keep, or (q)uit:")
  playerInput = input("> ")
  if playerInput == "q":
    quit_game(score)
  else:
    return playerInput
  
def bank_or_roll(calc_points, dice_remaining):
  print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")
  print("(r)oll again, (b)ank your points or (q)uit:")
  playerInput = input("> ")
  return playerInput
  
def dice_left(intPlayerInput):
  randomRoll = dice_roller(6)
  dice_remaining = len(randomRoll) - len(intPlayerInput)
  return dice_remaining
  
def unbanked_points_message(round, total_score, calc_points, dice_remaining):
  print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
  print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")

def quit_game(total_score):
  print(f"Thanks for playing. You earned {total_score} points")
  quit()
  
def start_game():
  total_score = 0
  calc_points = 0
  round = 1

  while True:
    dice = random_roll(6, round, total_score)
    calc_points += GameLogic.calculate_score(format_player_input(dice))
    total_score += calc_points
    dice_remaining = dice_left(dice)
    playerInput = bank_or_roll(calc_points, dice_remaining)
    if playerInput == "b":
      print(f"""You banked {calc_points} points in round {round}
Total score is {total_score} points""")
      # print("this is the round before ", round)
      round += 1
      calc_points = 0
      print(f"Starting round {round}\nRolling 6 dice...")
      # print("this is the round after ", round)
    else:
      unbanked_points_message(round, total_score, calc_points, dice_remaining)

      

    if playerInput == "q":
      print(f"Thanks for playing. You earned {total_score} points")
      return -1
  
def format_player_input(player_input_string):
  int_list = []
  for i in range(len(player_input_string)):
    int_list.append(int(player_input_string[i]))
  return int_list

if __name__ == "__main__":
  play()