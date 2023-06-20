Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

      @staticmethod
          def roll_dice(number_of_dice):
              """
              Rolls a specified number of dice and returns a tuple of the results.

              Args:
                  number_of_dice: The number of dice to roll.

              Returns:
                  A tuple of the results of the dice rolls.
              """

              if number_of_dice < 1 or number_of_dice > 6:
                  raise ValueError("Number of dice must be between 1 and 6.")

              results = tuple(random.randint(1, 6) for _ in range(number_of_dice))
              return results
