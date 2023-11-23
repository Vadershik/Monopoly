import logging
import sys
MINPlayers = 2
MAXPlayers = 8
players = 2

class Game:
    board = [[] for _ in range(12)]

    def __init__(self, board):
        self.board = board
        logging.basicConfig(filename='log.txt',level=logging.WARNING,
                            format='%(asctime)s:%(levelname)s:%(message)s')

    def makeBoard(self, playersCount: int):
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
        assert MINPlayers <= numPlayer <= MAXPlayers
        assert 0 <= startIndex <= 11
        assert 0 <= endIndex <= 11
        self.board[startIndex].remove(numPlayer)
        self.board[endIndex].append(endIndex)
        logging.info(f"{numPlayer} moved from {startIndex+1} to {endIndex+1}")
    def getTask(self, numPlayer: int):
        pass

    def getPosPlayer(self, numPlayer: int):
        pass

    def getNewPosPlayer(self, currentIndex: int):
        """Function to make a roll dice."""
        #Formula: (currentIndex+random(1,6))%12
        pass

    def checkPosPlayer(self, Pos) -> bool:
        return MINPlayers <= Pos <= MAXPlayers

def startMenu():
    """This function need for emulation of game."""
    print("Hello. How many users?")
    try:
        players = int(input())
    except:
        print("INPUTERROR: Players need to be integer value")
        sys.exit(0)
    assert MINPlayers <= players <= MAXPlayers
    board = [[] for i in range(12)]
    a = Game(board)
    a.getBoard()
    a.makeBoard(players)
    a.getBoard()


if __name__ == "__main__":
    startMenu()
