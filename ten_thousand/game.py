from ten_thousand.game_logic import GameLogic

def play(roller=None):
  rolled = roller or GameLogic.roll_dice
  print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
  playerInput = input("> ")
  
  if playerInput == 'n':
    print("OK. Maybe another time")
    
  elif playerInput == "y":
    print("""Starting round 1
Rolling 6 dice...""")
    print(f"""*** 4 4 5 2 3 1 ***""")
    print("Enter dice to keep, or (q)uit:")
    playerInput = input("> ")
    if playerInput == "q":
      print("Thanks for playing. You earned 0 points")
