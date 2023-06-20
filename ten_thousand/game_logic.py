import random

class GameLogic:
  @staticmethod
  def calculate_score(dice_roll):
    score = 0
    counts = [0] * 7 
    for dice in dice_roll:
      counts[dice] += 1
    if counts[1] >= 3:
      score += 1000
      counts[1] -= 3
    for i in range(2, 7):
      if counts[i] >= 3:
        score += i * 100
        counts[i] -= 3
    score += counts[1] * 100 
    score += counts[5] * 50  
    return score
  
  @staticmethod
  def roll_dice(number_of_dice):
    if number_of_dice < 1 or number_of_dice > 6:
      raise ValueError("Number of dice must be between 1 and 6.")
    results = tuple(random.randint(1, 6) for _ in range(number_of_dice))
    return results
