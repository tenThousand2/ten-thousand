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
    
  elif playerInput == "y":
    print("""Starting round 1
Rolling 6 dice...""")
    start_game()
  
def start_game():
  total_score = 0
  randomRoll = dice_roller(6)
  print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
  print("Enter dice to keep, or (q)uit:")
  playerInput = input("> ")
  if type(playerInput) == int:
    calc_points = GameLogic.calculate_score(playerInput)
    total_score += calc_points
    dice_remaining = len(randomRoll) - len(playerInput)
    print(f"You have {calc_points} unbanked points and {dice_remaining} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    
  elif playerInput == "b":
    print(f"""You banked {calc_points} points in round 1
Total score is {total_score} points
Starting round 2
Rolling 6 dice...""")
    
    randomRoll = dice_roller(6)
    print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
    print("Enter dice to keep, or (q)uit:")
  elif playerInput == "q":
    print(f"Thanks for playing. You earned {total_score} points")
  



#   if playerInput == "5":
#     print("You have 50 unbanked points and 5 dice remaining")
#     print("(r)oll again, (b)ank your points or (q)uit:")
#     playerInput = input("> ")
#     if playerInput == "b":
#       print("""You banked 50 points in round 1
# Total score is 50 points
# Starting round 2
# Rolling 6 dice...""")
#     # randomRoll = rolled(6)
#     # print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
#     print("*** 6 4 5 2 3 1 ***")
#     print("Enter dice to keep, or (q)uit:")
#     playerInput = input("> ")
#     if playerInput == "q":
#       print("Thanks for playing. You earned 50 points")
    
  # if playerInput == "q":
  #   print("Thanks for playing. You earned 50 points")
  