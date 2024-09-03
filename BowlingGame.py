#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    def __init__(self):
        '''
        The function initializes the 'rolls' list
        
        Args:
            rolls (list): Records the number of pins dropped in each roll during a game
        '''
        self.rolls=[]

    def roll(self,pins):
        '''
        The function adds the new score to the 'rolls' list. This needs to be done as 'rolls' is a local variable, and therefore not accessible from exterior scripts
        
        Args:
            pins (float): The given value of how many pins were knocked down in a single roll
        '''
        self.rolls.append(pins)

    def score(self):
        '''
        The function determines if certain conditions have been met, being a strike, spare or normal roll, and calculates the increase in score based on which. This along with the other functions are used to simulate the scoring system for a game of 10-pin bowling.
        
        Args:
            result (float): The total score of the rolls being calculated
            rollIndex (int): The index being checked in the 'rolls' list
        
        Returns:
            int: The combined total of the two rolls in a single round
        '''
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        '''
        The function determines whether a chosen roll is a strike. a strike is when you knock down all the pins, therefore achieving the max score of 10.
        
        Args:
            rollIndex (int): The index being checked in the 'rolls' list
        
        Returns:
            bool: Whether or not the chosen roll meets the condition for being considered a strike
        '''
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        '''
        The function determines whether the two chosen consecutive rolls is a spare. a spare is when you don't knock down all the pins on your first roll, but knock down the remaining pins on your second roll, therefore achieving the max score of 10.
        
        Args:
            rollIndex (int): The index being checked in the 'rolls' list
        
        Returns:
            bool: Whether or not the chosen roll meets the condition for being considered a spare
        '''
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    def strikeScore(self,rollIndex):
        '''
        In the event of a strike, the function determines how much the score increases
        
        Args:
            rollIndex (int): The index being chosen in the 'rolls' list
        
        Returns:
            int: The score of 10, plus the next two rolls
        '''
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        '''
        In the event of a spare, the function determines how much the score increases
        
        Args:
            rollIndex (int): The index being chosen in the 'rolls' list
        
        Returns:
            int: The score of 10, plus the next roll that isn't involved in the spare
        '''
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        '''
        In bowling, each round consists of two rolls, this function adds together the two rolls in a single round and returns the resulting score
        
        Args:
            rollIndex (int): The index being chosen in the 'rolls' list
        
        Returns:
            int: The combined total of the two rolls in a single round
        '''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
