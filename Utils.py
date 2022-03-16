
class Utils:

    # board constructor
    def __init__(self):
        self.board = [[0]*8 for i in range(8)]
        self.height = 8
        self.width = 8
        self.generateGrid()
        self.columnMap = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
        self.reverseColumnMap = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

    # function to get the start and end positions of the pawn
    def getMovePositions(self, currentPlayer):
        print("Player " + str(currentPlayer) + "'s turn.")
        startRow = input("Enter the row of the pawn to move: ")
        startCol = input("Enter the column of the pawn to move: ")
        endRow = input("Enter the row of the destination: ")
        endCol = input("Enter the column of the destination: ")
        print("")

        return [(int(startRow),startCol),(int(endRow),endCol)]


    # function to populate initial grid with player 1 & 2 pawns
    def generateGrid(self):
        for j in range(self.width):
            self.board[1][j] = 1
            self.board[6][j] = 2

    # function to print the board at any state
    def printBoard(self):
        for i in range(self.height):
            print("(" + str(self.height - i) + ") ", end="")
            for j in range(self.width):
                print(str(self.board[i][j]) + " ", end="")
            print("")
        print("    a b c d e f g h")

    # function to check the available capture moves for a given user
    def availablecapturePositions(self,user):
        availableCaptures = []
        if user == 1:
            for i in range(self.height-1):
                for j in range(self.width):
                    if j == 0:
                        if self.board[i][j] == user and self.board[i+1][j+1] == 2:
                            start = (self.height-i,self.reverseColumnMap[j])
                            end = (self.height-i-1,self.reverseColumnMap[j+1])
                            availableCaptures.append((start,end))
                    if j == 7:
                        if self.board[i][j] == user and self.board[i+1][j-1] == 2:
                            start = (self.height-i,self.reverseColumnMap[j])
                            end = (self.height-i-1,self.reverseColumnMap[j-1])
                            availableCaptures.append((start,end))
                    else:
                        if self.board[i][j] == user and self.board[i+1][j+1] == 2:
                            start = (self.height - i, self.reverseColumnMap[j])
                            end = (self.height-i-1, self.reverseColumnMap[j+1])
                            availableCaptures.append((start,end))
                        if self.board[i][j] == user and self.board[i+1][j-1] == 2:
                            start = (self.height-i,self.reverseColumnMap[j])
                            end = (self.height-i-1,self.reverseColumnMap[j-1])
                            availableCaptures.append((start,end))

        if user == 2:
            for i in range(self.height-1):
                for j in range(self.width):
                    if j == 0:
                        if self.board[i][j] == user and self.board[i-1][j+1] == 1:
                            start = (self.height-i,self.reverseColumnMap[j])
                            end = (self.height-i+1,self.reverseColumnMap[j+1])
                            availableCaptures.append((start,end))
                    if j == 7:
                        if self.board[i][j] == user and self.board[i-1][j-1] == 1:
                            start = (self.height-i,self.reverseColumnMap[j])
                            end = (self.height-i+1,self.reverseColumnMap[j-1])
                            availableCaptures.append((start,end))
                    else:
                        if self.board[i][j] == user and self.board[i-1][j+1] == 1:
                            start = (self.height - i, self.reverseColumnMap[j])
                            end = (self.height-i+1, self.reverseColumnMap[j+1])
                            availableCaptures.append((start,end))
                        if self.board[i][j] == user and self.board[i-1][j-1] == 1:
                            start = (self.height-i,self.reverseColumnMap[j])
                            end = (self.height-i+1,self.reverseColumnMap[j-1])
                            availableCaptures.append((start,end))

        return availableCaptures

    # function to move a pawn for a given user, start and end are tuples of the form (row,col) e.g. (2,"a")
    # returns tuple -> (wonGame,changeUser,captureMoveEndingSpot)
    def movePawn(self,user,start,end):
        # check valid user
        if user not in [1,2]:
            print("You have entered invalid input for user.")
            return False,False,None

        if user == 1: opponent = 2
        else: opponent = 1

        # check if appropriate start/end coordinates and if user has pawn in that position
        if isinstance(start[0],int) is False:
            print("Starting row coordinate not an integer!")
            return False,False,None
        if start[0] < 1 or start[0] > 8:
            print("Invalid starting row coordinate given!")
            return False,False,None
        if isinstance(start[1],str) is False:
            print("Starting column coordinate not a letter!")
            return False,False,None
        if start[1] not in self.columnMap:
            print("Invalid starting column coordinate given!")
            return False,False,None
        if isinstance(end[0],int) is False:
            print("Ending row coordinate not an integer!")
            return False,False,None
        if end[0] < 1 or end[0] > 8:
            print("Invalid ending row coordinate given!")
            return False,False,None
        if isinstance(end[1],str) is False:
            print("Ending column coordinate not a letter!")
            return False,False,None
        if end[1] not in self.columnMap:
            print("Invalid ending column coordinate given!")
            return False,False,None
        if self.board[self.height-start[0]][self.columnMap[start[1]]] != user:
            print("You do not have a pawn to move at that spot!")
            return False,False,None

        # check if valid move
        capturingMove = False
        capturePositions = self.availablecapturePositions(user)
        if len(capturePositions) > 0:
            capturingMove = True

        if user == 1:
            if capturingMove:
                if (start,end) not in capturePositions:
                    print("You cannot move to that end spot from the given start spot!")
                    return False,False,None
            else:
                if not ((end[0] == start[0] - 1) and (self.columnMap[end[1]] == self.columnMap[start[1]])):
                    print("You cannot move to that end spot from the given start spot!")
                    return False,False,None
        if user == 2:
            if capturingMove:
                if (start, end) not in capturePositions:
                    print("You cannot move to that end spot from the given start spot!")
                    return False,False,None
            else:
                if not ((end[0] == start[0] + 1) and (self.columnMap[end[1]] == self.columnMap[start[1]])):
                    print("You cannot move to that end spot from the given start spot!")
                    return False,False,None
        if not capturingMove:
            if self.board[self.height - end[0]][self.columnMap[end[1]]] == opponent:
                print("You cannot move to that end spot from the given start spot!")
                return False,False,None

        # do the move & display new board
        self.board[self.height - end[0]][self.columnMap[end[1]]] = user
        self.board[self.height - start[0]][self.columnMap[start[1]]] = 0
        self.printBoard()

        # check if either user has won after this move
        if self.checkIfWon(user):
            print("User " + str(user) + " has reached the other side and won the game!!!!!")
            return True,False,None

        if self.checkNoMoves(opponent):
            print("User " + str(opponent) + " has no moves to make, User" + str(user) + " has won the game!!!!!")
            return True,False,None

        if capturingMove:
            return False,False,end

        return False,True,None

    # check if a given user has won the game
    def checkIfWon(self,user):
        # check valid user
        if user not in [1,2]:
            print("You have entered invalid input for user.")
            return False
        # check for user 1
        if user == 1:
            for j in range(self.width):
                if self.board[-1][j] == 1:
                    return True
        # check for user 2
        if user == 2:
            for j in range(self.width):
                if self.board[0][j] == 2:
                    return True

        return False

    # check if a given user has no possible moves left and has therefore lost
    def checkNoMoves(self,user):
        capturePositions = self.availablecapturePositions(user)
        if len(capturePositions) > 0: return False

        if user == 1:
            for i in range(self.height-1):
                for j in range(self.width):
                    if self.board[i][j] == user and self.board[i+1][j] == 0:
                        return False

        if user == 2:
            for i in range(self.height-1):
                for j in range(self.width):
                    if self.board[i][j] == user and self.board[i-1][j] == 0:
                        return False
        return True
