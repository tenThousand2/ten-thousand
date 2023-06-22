from ten_thousand.game_logic import GameLogic
dice_roller = GameLogic.roll_dice

def play(roller=None):
  global dice_roller
  dice_roller = roller
  print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
  playerInput = input("> ")
  
  if playerInput == 'n':
    print("OK. Maybe another time")
    
  else:
    start_game()
  
def start_game():
  print("""Starting round 1
Rolling 6 dice...""")
  
  total_score = 0
  calc_points = 0
  randomRoll = dice_roller(6)
  print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
  print("Enter dice to keep, or (q)uit:")
  # continue_game = True


  while True:
    playerInput = input("> ")
    if playerInput == "b":
      print(f"""You banked {calc_points} points in round 1
  Total score is {total_score} points
  Starting round 2
  Rolling 6 dice...""")
      
      randomRoll = dice_roller(6)
      formated_roll = format_player_input(randomRoll)
      # print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
      print(f"*** {formated_roll} ***")
      print("Enter dice to keep, or (q)uit:")
    elif playerInput == "q":
      print(f"Thanks for playing. You earned {total_score} points")
      return -1

    else:
      intPlayerInput = format_player_input(playerInput)
      calc_points = GameLogic.calculate_score(intPlayerInput)
      total_score += calc_points
      dice_remaining = len(randomRoll) - len(intPlayerInput)
      print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")
      print("(r)oll again, (b)ank your points or (q)uit:")
      playerInput = input("> ")
    
  
def format_player_input(player_input_string):
  int_list = []
  str_list = player_input_string.split()
  for i in range(len(str_list)):
    int_list.append(int(str_list[i]))
    # print(f"*** {int_list} ***")
  return int_list

  