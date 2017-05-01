import sys

    #####################################
    # CHESS GAME - AP COMP SCI P - 2017 #
    #####################################

# Width & Height of chess board
SIZE   = 8

# List of board data (piece positions)
BOARD  = [None] * (SIZE * SIZE)

# SCORE
ROUND = 0

# Default plan for piece positions
DEFAULT_BOARD_PLAN = [
    4, 2, 3, 6, 5, 3, 2, 4,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    7, 7, 7, 7, 7, 7, 7, 7,
    10,8, 9, 12,11,9, 8,10
]

# main()
# Main function to start the game
def main():
    setupBoard()    # Setup board
    printBoard()    # Print board to console
    loop()

# setupBoard()
# Sets up the chess board with default values
# Loops through DEFAULT_BOARD_PLAN and sets BOARD equal
def setupBoard():
    global BOARD
    for i in range(SIZE * SIZE):
        BOARD[i] = getByID(DEFAULT_BOARD_PLAN[i])

# printBoard()
# Prints the chess board to the console
def printBoard():
    print()
    print("    --------------------------")
    print("   | ROUND : " + str(ROUND + 1), end="")
    for _i in range(17 - len(str(ROUND))):
        print(" ", end="")
    print("|")
    print("   | ------------------------ |")
    for y in range(SIZE):
        print(" " + str(y + 1) + " | ", end='')
        for x in range(SIZE): 
            temp = getPiece(x, y)
            if(temp == None):
                print(" _ ", end='')
            else:
                print(temp.getText() + "", end='')
        print(" |")
    print("    --------------------------")
    print("      A  B  C  D  E  F  G  H")
    print()

# getByID(ID)
# Parameters:
#    ID - id of piece to return
# returns the object pair of id
def getByID(ID):
    if(ID == 1) : return BlackPawn()
    if(ID == 2) : return BlackKnight()
    if(ID == 3) : return BlackBishop()
    if(ID == 4) : return BlackRook()
    if(ID == 5) : return BlackQueen()
    if(ID == 6) : return BlackKing()
    if(ID == 7) : return WhitePawn()
    if(ID == 8) : return WhiteKnight()
    if(ID == 9) : return WhiteBishop()
    if(ID == 10): return WhiteRook()
    if(ID == 11): return WhiteQueen()
    if(ID == 12): return WhiteKing()
    
# getPiece(x, y) 
# Parameters :
#    x - x Position
#    y - y Position
# returns id code from 2D points
def getPiece(x, y):
    return BOARD[x + (y * SIZE)]

# setPiece(x, y, id) 
# Parameters :
#    x - x Position
#    y - y Position
#    id - id of set piece
# returns id code from 2D points
def setPiece(x, y, piece):
    BOARD[x + (y * SIZE)] = piece

# loop()
# Main game loop
# Loops through the ask() method, increments the round, and prints the board
def loop():
    global ROUND
    while(True):
        ask()
        ROUND = ROUND + 1
        printBoard()

# ask()
# Parses the users input
# Available inputs:
#    move [i1] [i2]      - moves piece i1 to i2
#    set  [x]  [y] [ID]  - sets coordinates (x,y) to piece id (for testing)
#    exit                - ends the program
def ask():
    global ROUND
    player = ""
    
    if(ROUND % 2):
        player = "[BLACK]"
    else :
        player = "[WHITE]"
        
    lineArray = input(player + "> ").casefold().split(" ")
    
    if(lineArray[0] == "quit"):
        print("Thank you for playing!")
        sys.exit()
    elif(lineArray[0] == "move"):
        result = moveBySet(lineArray[1], lineArray[2])
        if(result == False):
            ask()
    elif(lineArray[0] == "set"):
        setPiece(int(lineArray[1]), int(lineArray[2]), getByID(int(lineArray[3])))
        printBoard()
        ask()
    else:
        print("Unknown command...")
        ask()

# moveBySet(start, end)
# Parameters:
#    start - string start coordinate (letter | number)
#    end   - string end coordinate (letter | number)
# Return:
#    boolean - successful move
# Takes string coordinates and attempts to move the corresponding pieces
def moveBySet(start, end):
    startColumn = start[0]
    startRow    = start[1]
    endColumn   = end[0]
    endRow      = end[1]
     
    return move(ord(startColumn) - 97, int(startRow) - 1, ord(endColumn) - 97, int(endRow) - 1)

# move(startX, startY, endX, endY)
# Parameters:
#    startX - piece starting X value
#    startY - piece starting Y value
#    endX   - piece ending X value
#    endY   - piece ending Y value
# Return:
#    boolean - successful move
# Attempts to move a piece from one coordinate to another
def move(startX, startY, endX, endY):
    start = getPiece(startX, startY)
    if(start == None):
        print("Cannot move blank space")
        return False
    else:
        if(start.canMove(startX, startY, endX, endY)):
            setPiece(endX, endY, start)
            setPiece(startX, startY, None);
            return True
        else:
            print("Invalid Move, try again...")
            return False
    
    # Check win condition

# ChessPiece Class
# Abstract class designed as a framework for all chess pieces
class ChessPiece():
    
    ID   = 0
    isBlack = False
    text = ""
    name = ""
    
    def __init__(self, ID = 0, name = "NONE", isBlack = False, text = "_"):
        self.ID   = ID
        self.name = name
        self.text = text
        
    def canMove(self, startX, startY, endX, endY):
        print("Cannot move abstract piece...")
        return False
    
    def getTeamByID(self, team):
        if(team == self.BLACK): return "BLACK"
        if(team == self.WHITE): return "WHITE"
        
    def isBlack(self):
        return self.isBlack;
    
    def getID(self):
        return self.ID
    
    def getText(self):
        return self.text
        
    def getName(self):
        return self.name

# BlackPawn Class
class BlackPawn(ChessPiece):
    
    validMoves = [[0,1],[1,1],[-1,1]]
    
    def __init__(self):
        ChessPiece.__init__(self, 1, "PAWN", True, "[P]")
        
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 1):
            if(startY == 1):
                if(endY - startY == 2 and endX - startX == 0):
                    return True
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(self.validMoves[i][0] != 0):
                            if(getPiece(endX, endY) == None):
                                return False
                            else:
                                if(getPiece(endX, endY).isBlack()):
                                    return True
                                else:
                                    return False
                        else:
                            return True
        return False
            
# WhitePawn Class
class WhitePawn(ChessPiece):
    
    validMoves = [[0,-1],[1,-1],[-1,-1]]
    
    def __init__(self):
        ChessPiece.__init__(self, 7, "PAWN", False, "(P)")
        
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 0):
            if(startY == 6):
                if(endY - startY == -2 and endX - startX == 0):
                    return True
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(self.validMoves[i][0] != 0):
                            if(getPiece(endX, endY) == None):
                                return False
                            else:
                                if(getPiece(endX, endY).isBlack()):
                                    return True
                                else:
                                    return False
                        else:
                            return True
        return False

# BlackKnight Class
class BlackKnight(ChessPiece):
    
    validMoves = [[1,2],[-1,2],[2,1],[-2,1],[2,-1],[-1,-2],[1,-2],[-2,-1]]
    
    def __init__(self):
        ChessPiece.__init__(self, 2, "KNIGHT", True, "[K]")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 1):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(not getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# WhiteKnight Class
class WhiteKnight(ChessPiece):
    
    validMoves = [[1,2],[-1,2],[2,1],[-2,1],[2,-1],[-1,-2],[1,-2],[-2,-1]]
    
    def __init__(self):
        ChessPiece.__init__(self, 8, "KNIGHT", False, "(K)")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 0):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False
    
# BlackBishop Class
class BlackBishop(ChessPiece):
    
    validMoves = [
        [ 1, 1],[ 2, 2],[ 3, 3],[ 4, 4],[ 5, 5],[ 6, 6],[ 7, 7],[ 8, 8],
        [-1, 1],[-2, 2],[-3, 3],[-4, 4],[-5, 5],[-6, 6],[-7, 7],[-8 ,8],
        [ 1,-1],[ 2,-2],[ 3,-3],[ 4,-4],[ 5,-5],[ 6,-6],[ 7,-7],[ 8,-8],
        [-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8]
        ]
    
    def __init__(self):
        ChessPiece.__init__(self, 3, "BISHOP", True, "[B]")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 1):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(not getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# WhiteBishop Class
class WhiteBishop(ChessPiece):
    
    validMoves = [
        [ 1, 1],[ 2, 2],[ 3, 3],[ 4, 4],[ 5, 5],[ 6, 6],[ 7, 7],[ 8, 8],
        [-1, 1],[-2, 2],[-3, 3],[-4, 4],[-5, 5],[-6, 6],[-7, 7],[-8 ,8],
        [ 1,-1],[ 2,-2],[ 3,-3],[ 4,-4],[ 5,-5],[ 6,-6],[ 7,-7],[ 8,-8],
        [-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8]
        ]
    
    def __init__(self):
        ChessPiece.__init__(self, 9, "BISHOP", False, "(B)")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 0):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            print("hi")
                            if(getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# BlackRook Class
class BlackRook(ChessPiece):
    
    validMoves = [
        [0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[0, 7],[0, 8],
        [0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],
        [1, 0],[2, 0],[3, 0],[4, 0],[5, 0],[6, 0],[7, 0],[8, 0],
        [-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0]
        ]
    
    def __init__(self):
        ChessPiece.__init__(self, 4, "ROOK", True, "[R]")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 1):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(not getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# WhiteRook Class
class WhiteRook(ChessPiece):
    
    validMoves = [
        [0, 1],[0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[0, 7],[0, 8],
        [0,-1],[0,-2],[0,-3],[0,-4],[0,-5],[0,-6],[0,-7],[0,-8],
        [1, 0],[2, 0],[3, 0],[4, 0],[5, 0],[6, 0],[7, 0],[8, 0],
        [-1,0],[-2,0],[-3,0],[-4,0],[-5,0],[-6,0],[-7,0],[-8,0]
        ]
    
    def __init__(self):
        ChessPiece.__init__(self, 10, "ROOK", False, "(R)")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 0):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# BlackQueen Class
class BlackQueen(ChessPiece):
    
    validMoves = [
        [ 0, 1],[ 0, 2],[ 0, 3],[ 0, 4],[ 0, 5],[ 0, 6],[ 0, 7],[ 0, 8],
        [ 0,-1],[ 0,-2],[ 0,-3],[ 0,-4],[ 0,-5],[ 0,-6],[ 0,-7],[ 0,-8],
        [ 1, 0],[ 2, 0],[ 3, 0],[ 4, 0],[ 5, 0],[ 6, 0],[ 7, 0],[ 8, 0],
        [-1, 0],[-2, 0],[-3, 0],[-4, 0],[-5, 0],[-6, 0],[-7, 0],[-8, 0],
        [ 1, 1],[ 2, 2],[ 3, 3],[ 4, 4],[ 5, 5],[ 6, 6],[ 7, 7],[ 8, 8],
        [-1, 1],[-2, 2],[-3, 3],[-4, 4],[-5, 5],[-6, 6],[-7, 7],[-8 ,8],
        [ 1,-1],[ 2,-2],[ 3,-3],[ 4,-4],[ 5,-5],[ 6,-6],[ 7,-7],[ 8,-8],
        [-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8]
        ]
    
    def __init__(self):
        ChessPiece.__init__(self, 5, "QUEEN", True, "[&]")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 1):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(not getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# WhiteQueen Class
class WhiteQueen(ChessPiece):
    
    validMoves = [
        [ 0, 1],[ 0, 2],[ 0, 3],[ 0, 4],[ 0, 5],[ 0, 6],[ 0, 7],[ 0, 8],
        [ 0,-1],[ 0,-2],[ 0,-3],[ 0,-4],[ 0,-5],[ 0,-6],[ 0,-7],[ 0,-8],
        [ 1, 0],[ 2, 0],[ 3, 0],[ 4, 0],[ 5, 0],[ 6, 0],[ 7, 0],[ 8, 0],
        [-1, 0],[-2, 0],[-3, 0],[-4, 0],[-5, 0],[-6, 0],[-7, 0],[-8, 0],
        [ 1, 1],[ 2, 2],[ 3, 3],[ 4, 4],[ 5, 5],[ 6, 6],[ 7, 7],[ 8, 8],
        [-1, 1],[-2, 2],[-3, 3],[-4, 4],[-5, 5],[-6, 6],[-7, 7],[-8 ,8],
        [ 1,-1],[ 2,-2],[ 3,-3],[ 4,-4],[ 5,-5],[ 6,-6],[ 7,-7],[ 8,-8],
        [-1,-1],[-2,-2],[-3,-3],[-4,-4],[-5,-5],[-6,-6],[-7,-7],[-8,-8]
        ]
    
    def __init__(self):
        ChessPiece.__init__(self, 11, "QUEEN", False, "(&)")
    
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 0):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# BlackKing Class
class BlackKing(ChessPiece):
    
    validMoves = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]
    
    def __init__(self):
        ChessPiece.__init__(self, 6, "KING", True, "[@]")
        
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 1):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(not getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False

# WhiteKing Class
class WhiteKing(ChessPiece):
    
    validMoves = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,0],[-1,1],[-1,-1]]
    
    def __init__(self):
        ChessPiece.__init__(self, 12, "KING", False, "(@)")
        
    def canMove(self, startX, startY, endX, endY):
        if(ROUND % 2 == 0):
            for i in range(len(self.validMoves)):
                if(endX - startX == self.validMoves[i][0]):
                    if(endY - startY == self.validMoves[i][1]):
                        if(getPiece(endX, endY) != None):
                            if(getPiece(endX, endY).isBlack()):
                                return True
                            else:
                                return False
                        else:
                            return True
        return False
    
# start the main method
main()
