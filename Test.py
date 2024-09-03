#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        '''
        An initialization of the 'game' variable that works to access the BowlingGame.py script
        
        Args:
            self.game (class): The 'BowlingGame' files class and functions
        '''
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        '''
        The function adds several rolls to the game, then calls the score() function in the BowlingGame script and determines whether it recieved the expected result of 0
        
        Returns:
            assertion: confirms whether or not the score is exactly 0, resulting in an error during testing if not.
        '''
        for i in range(0, 20):
            self.game.roll(0)
        assert self.game.score()==0
    def testAllOnes(self):
        '''
        The function adds several rolls of 1 to the game, then calls the score() function in the BowlingGame script and determines whether it recieved the expected result of 20
        
        Returns:
            assertion: confirms whether or not the score is exactly 20, resulting in an error during testing if not.
        '''
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testOneSpare(self):
        '''
        The function adds several rolls to the game, including several results of 0, then calls the score() function in the BowlingGame script and determines whether it recieved the expected result of 16
        
        Returns:
            assertion: confirms whether or not the score is exactly 16, resulting in an error during testing if not.
        '''
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        '''
        The function adds several rolls to the game, including several results of 0, then calls the score() function in the BowlingGame script and determines whether it recieved the expected result of 24
        
        Returns:
            assertion: confirms whether or not the score is exactly 24, resulting in an error during testing if not.
        '''
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testPerfectGame(self):
        '''
        The function adds several rolls of 10 to the game, then calls the score() function in the BowlingGame script and determines whether it recieved the expected result of 300
        
        Returns:
            assertion: confirms whether or not the score is exactly 300, resulting in an error during testing if not.
        '''
        self.rollMany(10,12)
        assert self.game.score()==300
    def testOneSpare(self):
        '''
        The function adds several rolls of 5 to the game, then calls the score() function in the BowlingGame script and determines whether it recieved the expected result of 150
        
        Returns:
            assertion: confirms whether or not the score is exactly 150, resulting in an error during testing if not.
        '''
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        '''
        The function repeatedly adds a given number of rolls to the game with a given score

        Args:
            pins (int): the value of each roll being added
            rolls (int): the number of rolls being added to the game
        '''
        for i in range(rolls):
            self.game.roll(pins)
