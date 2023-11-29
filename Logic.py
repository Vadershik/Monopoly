from settings import MINPLAYERS, MAXPLAYERS, MINDICE, MAXDICE, BOARDSIZE
from Parser import Parser
from typing import Optional, Union
from tkinter import messagebox

import logging
import random
import sys


class Game:
    board = [[] for _ in range(BOARDSIZE)]
    ownersBoard = [0 for _ in range(BOARDSIZE)] #For rewarding new cards
    playersInGame = []

    def __init__(self, players):
        logging.basicConfig(filename='log.txt',level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.players = players
        self.playersInGame = [i+1 for i in range(players)]
        self.setPlayersOnBoard(players) #Распологаем игроков на новой позиции

    def setPlayersOnBoard(self, playersCount: int):
        for i in range(playersCount):
            self.board[0].append(i+1)
        logging.info("Maked a board")

    def getOwnersBoard(self):
        return self.ownersBoard
    def getPlayersInGame(self):
        return self.playersInGame
    def getBoard(self):
        """Print a game board."""
        
        if __name__ == "__main__":
            print(*self.board)
        logging.info("Maked a request to show board.")
        return self.board
    def movePlayer(self, numPlayer: int, startIndex: int, endIndex: int):
        """Function to move a player in board."""
        
        assert MINPLAYERS-1 <= numPlayer <= MAXPLAYERS
        assert 0 <= startIndex <= BOARDSIZE-1
        assert 0 <= endIndex <= BOARDSIZE-1
        
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

    def completeTask(self, status: str) -> bool:
        """Function to check task be completed"""
        trust = ['1',"yes","ye",'y','д']
        #falsed = ['0',"no",'n','н']
#        print("You will be make a task?(Y/N)")
#        ans = input().lower()
        return status in trust
    
    def getTask(self, numPlayer: int):
        """Function to give a random task from tasks.txt"""

        parser = Parser()
        logging.info(f"{numPlayer} get task")

        task = parser.getTask()
        if __name__ == "__main__":
            print(task)
        else:
            messagebox.showinfo(title="{numPlayer} get task!",
                                message=task)
#        if not self.completeTask():
#            print("YOU LOSE")
#            self.removePlayer(numPlayer)
#            print(f"{numPlayer} lose.")
        
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
        
        newPos = ((currentIndex)+random.randint(MINDICE, MAXDICE))%BOARDSIZE
        
        assert self.checkPosPlayer(newPos)
        
        return newPos

    def checkPosPlayer(self, position: int) -> bool:
        return 0 <= position <= BOARDSIZE-1

    def getOwnerOfPos(self, position: int) -> int:
        return self.ownersBoard[position]
    
    def setNewOwnerOfPos(self, numPlayer: int, position : int):
        self.ownersBoard[position] = numPlayer

    def removePlayer(self, numPlayer: int, killer: Union[int, None] = None):
        #removing from board
        position = self.getPosPlayer(numPlayer)
        self.board[position].remove(numPlayer)
        self.playersInGame.remove(numPlayer)
        if len(self.playersInGame)==1:
#            print(f"PLAYER {self.playersInGame[0]} WON!")
#            sys.exit(0)
            return f"PLAYER {self.playersInGame[0]} WON!"

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
    a = Game(players)
    index = 0
    while True:
        print("What are you want?\n1 - Make roll\n2 - Remove Player\n3 - Show Board\n0 - exit")
        print("Lived players: ", *a.playersInGame)
        print(f"Player {a.playersInGame[index]} move:")
        ans = int(input())
        numPlayer = a.playersInGame[index]
        posPlayer = a.getPosPlayer(numPlayer)
        match ans:
            case 1:
                newPos = a.getNewPosPlayer(posPlayer)
                a.movePlayer(numPlayer,posPlayer,newPos)
                index+=1
            case 2:
                print("Type num of player:")
                numPlayer = int(input())
                a.removePlayer(numPlayer)
                if numPlayer not in a.playersInGame:
                    print("This player not in game!")
            case 3:
                a.getBoard()
            case 0:
                break
        if index>=len(a.playersInGame):
            index-=len(a.playersInGame)


if __name__ == "__main__":
    startMenu()
