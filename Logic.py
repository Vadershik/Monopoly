from settings import MINPLAYERS, MAXPLAYERS, MINDICE, MAXDICE, BOARDSIZE
from Parser import Parser
from typing import Optional, Union

import logging
import random
import sys


class Game:
    board = [[] for _ in range(BOARDSIZE)]
    ownersBoard = [0 for _ in range(BOARDSIZE)] #For rewarding new cards

    def __init__(self):
        logging.basicConfig(filename='log.txt',level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')

    def setPlayersOnBoard(self, playersCount: int):
        for i in range(playersCount):
            self.board[0].append(i+1)
        logging.info("Maked a board")

    def getBoard(self):
        """Print a game board."""
        
        for i in range(len(self.board)):
            print(self.board[i])
        logging.info("Maked a request to show board.")

    def movePlayer(self, numPlayer: int, startIndex: int, endIndex: int):
        """Function to move a player in board."""
        
        assert MINPLAYERS-1 <= numPlayer <= MAXPLAYERS
        assert 0 <= startIndex <= 11
        assert 0 <= endIndex <= 11
        
        self.board[startIndex].remove(numPlayer)
        self.board[endIndex].append(numPlayer)
        logging.info(f"{numPlayer} moved from {startIndex+1} to {endIndex+1}")

        #Checking owner of this place
        if self.getOwnerOfPos(endIndex)==0:
            logging.info(f"{numPlayer} get new place {endIndex+1}")
            self.setNewOwnerOfPos(numPlayer, endIndex)
        else:
            logging.info(f"{numPlayer} get in place of a {self.getOwnerOfPos(endIndex)} player.")
            self.getTask(numPlayer)


    def getTask(self, numPlayer: int):
        """Function to give a random task from tasks.txt"""

        parser = Parser()
        logging.info(f"{numPlayer} get task")

        task = parser.getTask()
        print(task)
        
        return parser.getTask()

    def getPosPlayer(self, numPlayer: int):
        """Function to get position of a player."""

        for i in range(len(self.board)):
            if numPlayer in self.board[i]:
                return i
        return False

    def getNewPosPlayer(self, currentIndex: int) -> int:
        """Function to make a roll dice."""
        
        #Formula: (currentIndex+random(1,6))%12
        #CurrentIndex start from 0 to 11
        
        newPos = ((currentIndex)+random.randint(MINDICE, MAXDICE))%12
        
        assert self.checkPosPlayer(newPos)
        
        return newPos

    def checkPosPlayer(self, position: int) -> bool:
        return 0 <= position <= 11

    def getOwnerOfPos(self, position: int) -> int:
        return self.ownersBoard[position]
    
    def setNewOwnerOfPos(self, numPlayer: int, position : int):
        self.ownersBoard[position] = numPlayer

    def removePlayer(self, numPlayer: int, killer: Union[int, None] = None):
        #removing from board
        position = self.checkPosPlayer(numPlayer)
        self.board[position].remove(numPlayer)

        if killer!=None:
            for i in range(len(self.ownersBoard)):
                if self.ownersBoard[i]==numPlayer:
                    self.ownersBoard[i]=killer
                logging.info(f"{killer} get all places by {numPlayer}")
        logging.info(f"{numPlayer} be removed")



def startMenu():
    """This function need for emulation of game."""
    print("Hello. How many users?")
    try:
        players = int(input())
    except:
        print("INPUTERROR: Players need to be integer value")
        sys.exit(0)
    assert MINPLAYERS <= players <= MAXPLAYERS
    a = Game()
    a.getBoard()
    a.setPlayersOnBoard(players)
    a.movePlayer(2, 0, a.getNewPosPlayer(a.getPosPlayer(2)))
    a.setNewOwnerOfPos(2, a.getPosPlayer(2))
    a.movePlayer(1, 0, a.getPosPlayer(2))
    print()
    print(a.getOwnerOfPos(a.getPosPlayer(1)))
    a.getBoard()


if __name__ == "__main__":
    startMenu()
