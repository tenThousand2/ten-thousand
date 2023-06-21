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
    randomRoll = rolled(6)
    print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
    print("Enter dice to keep, or (q)uit:")
    playerInput = input("> ")
  
  
  if playerInput == "5":
    print("You have 50 unbanked points and 5 dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    playerInput = input("> ")
    if playerInput == "b":
      print("""You banked 50 points in round 1
Total score is 50 points
Starting round 2
Rolling 6 dice...""")
    # randomRoll = rolled(6)
    # print(f"*** {randomRoll[0]} {randomRoll[1]} {randomRoll[2]} {randomRoll[3]} {randomRoll[4]} {randomRoll[5]} ***")
    print("*** 6 4 5 2 3 1 ***")
    print("Enter dice to keep, or (q)uit:")
    playerInput = input("> ")
    
  if playerInput == "q":
    print("Thanks for playing. You earned 0 points")
  