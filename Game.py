import Board


class Game:

    def __init__(self):
        self.board = Board.Board()
        self.board.printBoard()

    def playGame(self):
        print("To make a move, you will enter row and column identifiers for both start and end coordinates ")
        print("The rows should be integers, like '2', and the columns should be letters, like 'c'.")
        print("")
        playerHasWon = False
        currentMove = 2
        while not playerHasWon:
            captureMoves = []
            done = False
            while not done:
                print("Player " + str(currentMove) + " it's your turn.")
                startRow = input("Enter the row of the pawn to move: ")
                startCol = input("Enter the column of the pawn to move: ")
                endRow = input("Enter the row of the destination: ")
                endCol = input("Enter the column of the destination: ")
                print("")
                startTup = (int(startRow),startCol)
                endTup = (int(endRow),endCol)
                if startTup in captureMoves:
                    print("You cannot move a pawn that captured an opponent's in the same turn. Try again.")
                    continue
                result = self.board.movePawn(currentMove,startTup,endTup)
                if result[0] is True:
                    playerHasWon = True
                    done = True
                    break
                if result[1] is True:
                    if currentMove == 1:
                        currentMove = 2
                    else:
                        currentMove = 1
                    done = True
                else:
                    if result[2] is not None:
                        captureMoves.append(result[2])
                        continue

game = Game()
game.playGame()