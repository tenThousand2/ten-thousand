Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.

      class GameLogic:
          @staticmethod
          def calculate_score(dice_roll):
              score = 0

              # Calculate score based on the rules of the game
              counts = [0] * 7  # Initialize a list to count the occurrences of each dice value

              for dice in dice_roll:
                  counts[dice] += 1

              # Check for scoring combinations
              if counts[1] >= 3:
                  score += 1000
                  counts[1] -= 3

              for i in range(2, 7):
                  if counts[i] >= 3:
                      score += i * 100
                      counts[i] -= 3

              score += counts[1] * 100  # Add remaining 1's
              score += counts[5] * 50  # Add remaining 5's

              return score


