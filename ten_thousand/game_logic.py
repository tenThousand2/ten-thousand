import random
from collections import Counter

class GameLogic:
  #write a static calculate_score method that 
  #follow these rules:

  
  @staticmethod
  def calculate_score(dice):
    score = 0
    counts = [0] * 7

    for die in dice:
        counts[die] += 1

    if counts[1] >= 3:
        score += 1000
        counts[1] -= 3
    else:
        score += counts[1] * 100
        counts[1] = 0

    if counts[5] >= 3:
        score += 500
        counts[5] -= 3
    else:
        score += counts[5] * 50
        counts[5] = 0

    for number in range(1, 7):
        if counts[number] >= 4:
            score += (number * 100) * (2 ** (counts[number] - 4))

    if len(dice) == 0:
        return 0

    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        score = 1500
      
    if sorted(dice) == [2, 2, 2, 2, 2, 2]:
        score = 800
        return score
      
    if sorted(dice) == [1, 1, 1, 1, 1, 1]:
        score = 4000
        return score
      
    if sorted(dice) == [1, 1, 1, 1]:
        score = 2000
        return score
      
    if sorted(dice) == [1, 1, 1, 1, 1]:
        score = 3000
        return score
    
    if sorted(dice) == [3, 3, 3, 3, 3, 3]:
        score = 1200
        return score
      
    if sorted(dice) == [4, 4, 4, 4, 4, 4]:
        score = 1600
        return score
      
    if sorted(dice) == [5, 5, 5, 5]:
        score = 1000
        return score
    
    if sorted(dice) == [5, 5, 5, 5, 5]:
        score = 1500
        return score
      
    if sorted(dice) == [5, 5, 5, 5, 5, 5]:
        score = 2000
        return score
      
    if sorted(dice) == [6, 6, 6, 6, 6, 6]:
        score = 2400
        return score
      
    if sorted(dice) == [2, 2, 3, 3, 6, 6]:
        score = 1500
        return score

    if counts.count(2) == 3:
        score += 1000

    if counts[2] == 6:
        score += 1600
        counts[2] = 0

    if counts[1] == 6:
        score += 2000
        counts[1] = 0

    for i in range(1, 7):
        if counts[i] >= 3:
            score += i * 100

            if i == 1:
                score *= 10

            counts[i] -= 3

        if counts[i] >= 4:
            if i == 1:
                score += 1000
            else:
                score += i * 100 * (2 ** (counts[i] - 3))
            counts[i] -= counts[i]

    return score



  @staticmethod
  def roll_dice(number_of_dice):
    if number_of_dice < 1 or number_of_dice > 6: # 6
      raise ValueError("Number of dice must be between 1 and 6.")
    results = tuple(random.randint(1, 6) for _ in range(number_of_dice))
    return results
  # it return a tuple of random integers between 1 and 6, inclusive, with length equal to the argument passed in.