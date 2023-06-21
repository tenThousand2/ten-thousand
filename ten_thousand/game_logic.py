import random

class GameLogic:
  @staticmethod
  def calculate_score(dice_roll):
    score = 0
    counts = [0] * 7 # [0, 0, 0, 0, 0, 0, 0]
    for dice in dice_roll: # (5, 5, 5, 2, 2, 3)
      counts[dice] += 1 # [0, 0, 0, 1, 0, 3, 0]
      
    if all(counts[i] == 1 for i in range(1, 7)): # 1, 2, 3, 4, 5, 6
      score += 1500 # 1500
      return score # 1500
    
    if counts[1] == 6: # 6
      score += 4000 # 4000
      return score # 4000
    
    # check for four one's
    if counts[1] == 4: # 4
      score += 2000 # 2000
      return score # 2000
    
    if counts[1] == 5:
      score += 3000 
      return score 
    
    if counts[2] == 2:
      if counts[3] == 2:
        if counts[6] == 2:
          score += 1500
          return score
        
    for i in range(1, 7): # 1, 2, 3, 4, 5, 6
      if counts[i] >= 4: # 4
        score += i * 200 # 800
        score += (counts[i]-4) * i * 100 # 800
        return score # 800
      
    if counts[1] >= 3: # 3
      score += 1000 # 1000
      counts[1] -= 3 # [0, 0, 0, 1, 0, 0, 0]
      
    for i in range(2, 7): # 2, 3, 4, 5, 6
      if counts[i] >= 3: # 3, 3, 3, 3, 3
        score += i * 100 # 200, 300, 400, 500, 600
        counts[i] -= 3 # [0, 0, 0, 0, 0, 0, 0]
    score += counts[1] * 100 # 100
    score += counts[5] * 50  # 150
    return score # 1000 + 200 + 300 + 400 + 500 + 600 + 100 + 150 = 3250
  #    first we create a list of 7 zeros
  #    then we loop through the dice rolls and increment the count of the dice roll
  #    if the count of the dice roll is greater than or equal to 3, we add 1000 to the score
  #    and subtract 3 from the count of the dice roll
  #    then we loop through the dice rolls again, this time starting at 2
  #    if the count of the dice roll is greater than or equal to 3, we add the dice roll times 100 to the score
  #    and subtract 3 from the count of the dice roll
  #    then we add the count of 1 times 100 to the score
  #    and the count of 5 times 50 to the score
  #    then we return the score
  @staticmethod
  def roll_dice(number_of_dice):
    if number_of_dice < 1 or number_of_dice > 6: # 6
      raise ValueError("Number of dice must be between 1 and 6.") # ValueError("Number of dice must be between 1 and 6.")
    results = tuple(random.randint(1, 6) for _ in range(number_of_dice)) # (5, 5, 5, 2, 2, 3)
    return results # (5, 5, 5, 2, 2, 3)
