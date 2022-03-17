
class Utils:


    def __init__(self):
        '''
        Class constructor
        '''
        self.board = [[0]*8 for i in range(8)]
        self.totalColumns = 8
        self.totalRows = 8
        self.fillMatrix()
        self.rowEquivalent = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}
        self.columnEquivalent = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

 
    def getMovePositions(self, user):
        '''
        Summary:
        takes the start and end positions of the pawn  as input from user
         
        Parameters:
        user(int) : type of user ie 1 or 2 

        Returns:
        movePositions(list) : list of tuples (startRow,startColumn) (endRow,endColumn)
        '''
        print("Player " + str(user) + "'s turn.")
        startRow = input("Enter the start row of the pawn to move: ")
        startCol = input("Enter the start column of pawn to move: ")
        endRow = input("Enter the destination row of the pawn to move: ")
        endCol = input("Enter the destination column of the pawn to move: ")
        print("")

        movePositions = [(int(startRow),startCol),(int(endRow),endCol)]

        return movePositions



    def fillMatrix(self):
        '''
        Summary:
        function to populate chess board for player1 and player2 pawns with "1" and "2" respectively
         
        Parameters:
        no input parameters

        Returns:
        void
        '''
        for i in range(0,self.totalRows):
            self.board[1][i] = 1
            self.board[6][i] = 2

    def printMatrix(self):
        '''
        Summary:
        function to print the chess board 
         
        Parameters:
        no input parameters

        Returns:
        void
        '''
        print("    a b c d e f g h")
        for i in range(0,self.totalColumns):
            print("(" + str(self.totalColumns - i) + ") ", end="")
            for j in range(self.totalRows):
                print(str(self.board[i][j]) + " ", end="")
            print("")
        

    
    def availablecapturePositions(self,user):
        '''
        Summary:
        return all the possible capture moves for a pawn  
         
        Parameters:
        user(int) : type of user ie 1 or 2 

        Returns:
        availableCapturePositions(list) : list of the available capture positions
        '''
        availableCapturePositions = []
        if user == 1:
            for i in range(self.totalColumns-1):
                for j in range(self.totalRows):
                    if j == 0:
                        if self.board[i][j] == user and self.board[i+1][j+1] == 2:
                            start = (self.totalColumns-i,self.columnEquivalent[j])
                            end = (self.totalColumns-i-1,self.columnEquivalent[j+1])
                            availableCapturePositions.append((start,end))
                    if j == 7:
                        if self.board[i][j] == user and self.board[i+1][j-1] == 2:
                            start = (self.totalColumns-i,self.columnEquivalent[j])
                            end = (self.totalColumns-i-1,self.columnEquivalent[j-1])
                            availableCapturePositions.append((start,end))
                    else:
                        if self.board[i][j] == user and self.board[i+1][j+1] == 2:
                            start = (self.totalColumns - i, self.columnEquivalent[j])
                            end = (self.totalColumns-i-1, self.columnEquivalent[j+1])
                            availableCapturePositions.append((start,end))
                        if self.board[i][j] == user and self.board[i+1][j-1] == 2:
                            start = (self.totalColumns-i,self.columnEquivalent[j])
                            end = (self.totalColumns-i-1,self.columnEquivalent[j-1])
                            availableCapturePositions.append((start,end))

        if user == 2:
            for i in range(self.totalColumns-1):
                for j in range(self.totalRows):
                    if j == 0:
                        if self.board[i][j] == user and self.board[i-1][j+1] == 1:
                            start = (self.totalColumns-i,self.columnEquivalent[j])
                            end = (self.totalColumns-i+1,self.columnEquivalent[j+1])
                            availableCapturePositions.append((start,end))
                    if j == 7:
                        if self.board[i][j] == user and self.board[i-1][j-1] == 1:
                            start = (self.totalColumns-i,self.columnEquivalent[j])
                            end = (self.totalColumns-i+1,self.columnEquivalent[j-1])
                            availableCapturePositions.append((start,end))
                    else:
                        if self.board[i][j] == user and self.board[i-1][j+1] == 1:
                            start = (self.totalColumns - i, self.columnEquivalent[j])
                            end = (self.totalColumns-i+1, self.columnEquivalent[j+1])
                            availableCapturePositions.append((start,end))
                        if self.board[i][j] == user and self.board[i-1][j-1] == 1:
                            start = (self.totalColumns-i,self.columnEquivalent[j])
                            end = (self.totalColumns-i+1,self.columnEquivalent[j-1])
                            availableCapturePositions.append((start,end))

        return availableCapturePositions


    def pawnMove(self,user,start,end):
        '''
        Summary:
        function to move a pawn for a given user, start and end postion

        Parameters:
        user(int) : type of user ie 1 or 2
        start(list): list of [startRow,startColumn]
        end(list) : list of [endRow,endColumn]

        Returns:
        (wonGame,changeUser,captureMoveEndingSpot)((int,boolean, list)) : tuple of return values

        '''
        #check input user validity 
        if user not in [1,2]:
            print("Invalid user , User must be 1 or 2")
            return False,False,None

        # check input start and end coordinates validity  
        [startRow,startColumn] = start
        [endRow,endColumn] = end
        if isinstance(startRow,int) is False:
            print("Start row coordinate must be integer")
            return False,False,None
        if isinstance(endRow,int) is False:
            print("End row coordinate must be integer")
            return False,False,None
        if isinstance(startColumn,str) is False:
            print("Start column coordinate must be character")
            return False,False,None
        if isinstance(endColumn,str) is False:
            print("End column coordinate must be character")
            return False,False,None

        if startRow < 1 or startRow > 8:
            print("Start row out of bounds")
            return False,False,None
        if endRow < 1 or endRow > 8:
            print("End row out of bounds")
            return False,False,None
        if startColumn not in self.rowEquivalent:
            print("Start column invalid")
            return False,False,None
        if endColumn not in self.rowEquivalent:
            print("End column invalid")
            return False,False,None
        if self.board[self.totalColumns- startRow][self.rowEquivalent[startColumn]   ] != user:
            print("Pawn cant be moved")
            return False,False,None

        # set opponent based on user
        opponent = 2 if user == 1 else 1  

        # set capturing move pased on available capture position for user
        isCapturingMove = False
        capturePositions = self.availablecapturePositions(user)
        if len(capturePositions) > 0:
            isCapturingMove = True

        # check if the move is valid  
        if user == 1:
            if isCapturingMove:
                if (start,end) not in capturePositions:
                    print("The move from start to end position cannot be made")
                    return False,False,None
            else:
                if not ((end[0] == start[0] - 1) and (self.rowEquivalent[end[1]] == self.rowEquivalent[start[1]])):
                    print("The move from start to end position cannot be made")
                    return False,False,None
        if user == 2:
            if isCapturingMove:
                if (start, end) not in capturePositions:
                    print("The move from start to end position cannot be made")
                    return False,False,None
            else:
                if not ((end[0] == start[0] + 1) and (self.rowEquivalent[end[1]] == self.rowEquivalent[start[1]])):
                    print("The move from start to end position cannot be made")
                    return False,False,None
        if not isCapturingMove:
            if self.board[self.totalColumns - end[0]][self.rowEquivalent[end[1]]] == opponent:
                print("The move from start to end position cannot be made!")
                return False,False,None

        # move the pawn by setting new position with user and old position with 0
        self.board[self.totalColumns - end[0]][self.rowEquivalent[end[1]]] = user
        self.board[self.totalColumns - start[0]][self.rowEquivalent[start[1]]] = 0
        self.printMatrix()

        # check if any of the user has won after this move
        if self.userHasWon(user):
            print("User " + str(user) + " has won the game by reaching other end ")
            return True,False,None

        if self.userHasNoMoves(opponent):
            print("User " + str(opponent) + " has no moves to make, Hence User" + str(user) + " has won the game")
            return True,False,None

        if isCapturingMove:
            return False,False,end

        return False,True,None


    def userHasWon(self,user):
        '''
        Summary:
        function to check if user has won the game

        Parameters:
        user(int) : type of user ie 1 or 2


        Returns:
        hasWon(boolean) : returns whether user has won or not 

        '''
        # check input user validity
        if user not in [1,2]:
            print("You have entered invalid input for user.")
            return False
        # check if user 1 has won
        if user == 1:
            for j in range(self.totalRows):
                if self.board[-1][j] == 1:
                    return True
        # check if user 2 has won
        if user == 2:
            for j in range(self.totalRows):
                if self.board[0][j] == 2:
                    return True

        return False


    def userHasNoMoves(self,user):
        '''
        Summary:
        function to check if user has moves ir nit

        Parameters:
        user(int) : type of user ie 1 or 2


        Returns:
        hasMves(boolean) : returns whether user has moves or not

        '''
        # check available capture positions validity for the user
        availablecapturePositionss = self.availablecapturePositions(user)
        if len(availablecapturePositionss) > 0: return False

        # check if user 1 has moves
        if user == 1:
            for i in range(self.totalColumns-1):
                for j in range(self.totalRows):
                    if self.board[i][j] == user and self.board[i+1][j] == 0:
                        return False
        # check if user 2 has won
        if user == 2:
            for i in range(self.totalColumns-1):
                for j in range(self.totalRows):
                    if self.board[i][j] == user and self.board[i-1][j] == 0:
                        return False
        return True
