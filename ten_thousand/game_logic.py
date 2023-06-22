import random
from collections import Counter

class GameLogic:
  @staticmethod
  def calculate_score(dice):
    score = 0
    counter = Counter(dice)
    # Scoring for individual dice
    score += counter[1] * 100  # Each '1' is worth 100 points
    score += counter[5] * 50   # Each '5' is worth 50 points

    # Scoring for combinations
    for num, count in counter.items():
      if count >= 3:  # Three or more of a kind
        if num == 1:  # Three '1's
          score += 1000
        else:         # Three of any other number
          score += num * 100

        if count > 3:  # Additional dice beyond three
          score += (count - 3) * num * 100

      # Special scoring for specific combinations
      if num == 1 or num == 5:
        continue

      if count == 4:  # Four of a kind
        score += num * 100

      if count == 5:  # Five of a kind
        score += num * 200
          
      if count == 6:  # Six of a kind
        score += num * 300
    return score




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
