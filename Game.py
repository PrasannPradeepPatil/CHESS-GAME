import Utils


class Game:
    def __init__(self):
        '''
        Class constructor
        '''
        self.board = Utils.Utils()
        self.board.printMatrix()

    def playGame(self):
        '''
        Summary:
        function to play the game

        Parameters:
        no parameters


        Returns:
        void

        '''
        print("\nEnter the startRow, startColumn, endRow, endColumn for the pawn to move \nThe row must be integer and column must be a lowercase letter\n")

        isGameEnded = False
        currentPlayer = 2
        while not isGameEnded:
            capturePositions = []
            isMovePlayed = False
            while not isMovePlayed:
                # Get pawn's start position and end positions position from user 
                [startPosition,endPosition] = self.board.getMovePositions(currentPlayer)

                # if the pawn to move has captured the opponent pawn then dont move thant pawn 
                if startPosition in capturePositions:
                    print("The pawn you are trying to move has captured the opponent's pawn so try moving another pawn")
                    continue

                # move the pawn from start position to end position and change the variables affected by that move
                [wonGame,changeUser,captureMoveEndingPosition] = self.board.pawnMove(currentPlayer,startPosition,endPosition)
                if wonGame is True:
                    isGameEnded = True
                    isMovePlayed = True
                    break
                if changeUser is True:
                    currentPlayer = 2 if (currentPlayer == 1) else 1
                    isMovePlayed = True
                else:
                    if captureMoveEndingPosition is not None:
                        capturePositions.append(captureMoveEndingPosition)
                        continue





######DRIVER CODE###########
game = Game()
game.playGame()