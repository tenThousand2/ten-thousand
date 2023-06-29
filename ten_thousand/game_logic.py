import random
from collections import Counter

class GameLogic:
    @staticmethod
    def calculate_score(dice):
        # This function calculates the score of a roll of dice.

        score = 0
        counter = Counter(dice)  # This creates a dictionary that counts the number of each type of die that was rolled.

        # Scoring for individual dice

        score += counter[1] * 100  # Each '1' is worth 100 points.
        score += counter[5] * 50   # Each '5' is worth 50 points.

        # Scoring for combinations

        for num, count in counter.items():  # This loops over each number and the number of times it was rolled.
            if count >= 3:  # If there are three or more of a kind, we add points based on the number.
                if num == 1:  # If there are three 1's, we add 1000 points.
                    score += 1000
                else:  # Otherwise, we add 100 points for each of the three dice.
                    score += num * 100

                if count > 3:  # If there are more than three of a kind, we add additional points for each additional die.
                    score += (count - 3) * num * 100

            # Special scoring for specific combinations

            if num == 1 or num == 5:  # We don't score 1's or 5's in any other combinations.
                continue

            if count == 4:  # If there are four of a kind, we add 100 points.
                score += num * 100

            if count == 5:  # If there are five of a kind, we add 200 points.
                score += num * 200

            if count == 6:  # If there are six of a kind, we add 300 points.
                score += num * 300

        return score  # This returns the total score.


    @staticmethod
    def roll_dice(number_of_dice):
        # This function rolls a specified number of dice and returns a list of the results.

        if number_of_dice < 1 or number_of_dice > 6:
            # This raises an error if the number of dice is not between 1 and 6.
            raise ValueError("Number of dice must be between 1 and 6.")

        results = tuple(random.randint(1, 6) for _ in range(number_of_dice))
        # This creates a tuple of random numbers between 1 and 6, the length of which is equal to the number of dice rolled.

        return results
