from Logic import Game
from settings import BOARDSIZE
import tkinter as tk
root = tk.Tk()
root.title("Спортивная Монополия!")
mainboard = []
players = 4
game = Game(players)
board = game.getBoard()
playersInGame = game.getPlayersInGame()
indexPlayer = 0
def FillBoard():
    global mainboard, players, board
    for i in range(len(mainboard)):
        mainboard[i]["text"] = ",".join(map(str, board[i]))
def move():
    global game, playersInGame, indexPlayer, mainboard, board
    player = playersInGame[indexPlayer]
    newPos = game.getNewPosPlayer(player)
    posPlayer = game.getPosPlayer(player)
    mainboard[posPlayer]["text"] = ",".join(map(str, [i for i in board[posPlayer] if i!=player]))
    mainboard[newPos]["text"] = mainboard[newPos]["text"]+f",{player}" if len(mainboard[newPos]["text"])>=1 else f"{player}"
    game.movePlayer(player, posPlayer, newPos)
    #After move make a update a board.
    board = game.getBoard()
    #Set index to next player
    indexPlayer+=1
    if indexPlayer==len(playersInGame):
        indexPlayer=0
    #In the next updates here be made a remove a player...
    #####
    #Updating players in game
    playersInGame = game.getPlayersInGame()

def main():
    global BOARDSIZE
    for i in range(BOARDSIZE):
        mainboard.append(tk.Button(text="",fg='white',bg='black',width=7, height=10, command=move))
    FillBoard()
    for i in range(BOARDSIZE):
        mainboard[i].grid(row=0,column=i)
    root.mainloop()

if __name__ == "__main__":
    main()
