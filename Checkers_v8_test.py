from graphics import *
import sys
import tkMessageBox

class Checkers:
    def __init__(s):
        s.state = 'CustomSetup'
        s.is1P = False
        s.placeColour = 'White'
        s.placeRank = 'Pawn'
        s.placeType = 'Place'                   #Place or Delete (piece)
        s.pTurn = 'White'                       #White or Black (turn)
        s.isTileSelected = False
        s.selectedTile = ''

        s.win = GraphWin('Checkers',600,600)    #draws screen
        s.win.setBackground('White')
        s.win.setCoords(-1,-3,11,9)              #creates a coordinate system for the window
        s.ClearBoard()

        s.tiles = [[Tile(s.win,i,j,False) for i in range(8)] for j in range(8)]  #creates the 2D list and initializes all 8x8 entries to an empty tile


        gridLetters = ['A','B','C','D','E','F','G','H',]
        for i in range(8):
            Text(Point(-0.5,i+0.5),i+1).draw(s.win)                 #left and right numbers for grid
            Text(Point(8.5,i+0.5),i+1).draw(s.win)
            Text(Point(i+0.5,-0.5),gridLetters[i]).draw(s.win)      #bottom and top letters
            Text(Point(i+0.5,8.5),gridLetters[i]).draw(s.win) 
        
        s.SetButtons()
        
        
        s.SetupBoard()

        


    def ClearBoard(s):
        s.tiles=[[Tile(s.win,i,j,False) for i in range(8)] for j in range(8)]  #creates the 2D list and initializes all 8x8 entries to an empty tile
        for i in range(8):
            for j in range(8):
                s.ColourButton(s.TileColour(i,j),i,j)
        s.SetButtons()
        

        #reset state, buttons
        #re-count and re-draw numWhitePieces, numBlackPieces
        #set pTurn to 1 --probably

    def ColourButton(s,colour,X,Y,width=1,height=1):        #function to create a rectangle with a given colour, size, and location
        rect = Rectangle(Point(X,Y),Point(X+width,Y+height))
        rect.setFill(colour)
        rect.draw(s.win)
            
    def TileColour(s,x,y):
        if (x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1):
            return 'Red'   #sets every other square to red 
        else:
            return 'White' #every non red square to white

        
    def SetButtons(s):
        s.ColourButton('White',-1,-3,12,2)
        s.ColourButton('White',9,-1,2,10)

        if s.state == 'CustomSetup':
            s.DrawStandard()
            s.DrawStart()
            s.DrawClear()
            s.Draw1P()
            s.Draw2P()
            s.DrawLoad()
            s.DrawSave()
            s.DrawTurn()
            s.DrawX()
            
            s.DrawW()
            s.DrawB()
            s.DrawK()
            s.DrawDel()

            s.DrawScore() #not actually a button
        elif s.state == 'Play':
            s.DrawQuit()
            s.DrawSave()
            s.DrawTurn()
            s.DrawX()

            s.DrawScore() #not actually a button
            

    def DrawStandard(s):
        s.ColourButton('White',-1,-2,2,1)    #Standard Setup button
        Text(Point(0,-1.3),'Standard').draw(s.win)
        Text(Point(0,-1.7),'Setup').draw(s.win)
    def DrawCustom(s):
        s.ColourButton('White',-1,-3,2,1)    #Custom Setup button
        Text(Point(0,-2.3),'Custom').draw(s.win)  
        Text(Point(0,-2.7),'Setup').draw(s.win)
    def DrawStart(s):
        s.ColourButton('White',1,-2,2,1)    #Start! button
        Text(Point(2,-1.5),'Start!').draw(s.win)
    def DrawClear(s):
        s.ColourButton('White',1,-3,2,1)    #Clear Board button
        Text(Point(2,-2.3),'Clear').draw(s.win)
        Text(Point(2,-2.7),'Board').draw(s.win)
    def Draw1P(s):
        col = 'Red'
        if s.is1P:
            col = 'Green'
        s.ColourButton(col,4,-2,2,1)    #1Player   -- (1AI)
        Text(Point(5,-1.3),'1Player').draw(s.win)
        Text(Point(5,-1.7),'Game').draw(s.win)
    def Draw2P(s):
        col = 'Green'
        if s.is1P:
            col = 'Red'
        s.ColourButton(col,4,-3,2,1)    #2Player
        Text(Point(5,-2.3),'2Player').draw(s.win)  
        Text(Point(5,-2.7),'Game').draw(s.win)
    def DrawLoad(s):
        s.ColourButton('White',6,-3,2,1)    #Load
        Text(Point(7,-2.5),'Load').draw(s.win)
    def DrawSave(s):
        s.ColourButton('White',8,-3,2,1)    #Save
        Text(Point(9,-2.5),'Save').draw(s.win)
    def DrawX(s):
        s.ColourButton('Red',10,-3)    #X
        Exit_txt = Text(Point(10.5,-2.5),'X')
        Exit_txt.draw(s.win)
        Exit_txt.setFill('White')
    def DrawW(s):
        col = 'Green'
        if s.placeColour != 'White':
            col = 'Red'
        s.ColourButton(col,6,-2)    #W
        Text(Point(6.5,-1.5),'W').draw(s.win)
    def DrawB(s):
        col = 'Red'
        if s.placeColour != 'White':
            col = 'Green'
        s.ColourButton(col,7,-2)    #B
        Text(Point(7.5,-1.5),'B').draw(s.win)
    def DrawK(s):
        col = 'Red'
        if s.placeRank == 'King':
            col = 'Green'
        s.ColourButton(col,8,-2)    #K
        Text(Point(8.5,-1.5),'K').draw(s.win)
    def DrawDel(s):
        col1 = 'Black'#square colour
        col2 = 'White'#text colour
        if s.placeType == 'Delete':
            col1 = 'Green'
            col2 = 'Black'        
        s.ColourButton(col1,9,-2)    #Del
        deleteTxt = Text(Point(9.5,-1.5),'Del')
        deleteTxt.draw(s.win)
        deleteTxt.setFill(col2)
    def DrawQuit(s):
        s.ColourButton('White',6,-3,2,1)    #Load
        Text(Point(7,-2.5),'Quit').draw(s.win)
    def DrawTurn(s):
        col1 = 'White'
        col2 = 'Black'
        if s.pTurn == 'Black':
            col1 = 'Black'
            col2 = 'White'
        s.ColourButton(col1,9,8,2,1)    #Standard Setup button
        txt1 = Text(Point(10,8.7),col1)
        txt2 = Text(Point(10,8.3),'Turn')
        txt1.draw(s.win)
        txt2.draw(s.win)
        txt1.setFill(col2)
        txt2.setFill(col2)
    def DrawScore(s):
        Text(Point(10,7.5),'# White').draw(s.win)
        Text(Point(10,7.1),'Pieces:').draw(s.win)
        Text(Point(10,6.7),s.numColour('White')).draw(s.win)
        Text(Point(10,5.9),'# Black').draw(s.win)
        Text(Point(10,5.5),'Pieces').draw(s.win)
        Text(Point(10,5.1),s.numColour('Black')).draw(s.win)

                 
    def Click(s):
        click = s.win.getMouse()        #Perform mouse click
        X, Y = s.ClickedSquare(click)   #Gets click coords
        print [X,Y]
        print [s.placeType,s.placeRank,s.state]
        
        if (-1<=X<1 and -2<=Y<-1) and s.state != 'Play': #Standard clicked
            s.StandardSetup()  
        elif (1<=X<3 and -2<=Y<-1) and s.state != 'Play': #Start! clicked
            s.state = 'Play'
            s.SetButtons()
        elif (1<=X<3 and -3<=Y<-2) and s.state != 'Play': #Clear Board clicked
            s.ClearBoard()
        elif (4<=X<6 and -2<=Y<-1) and s.state != 'Play': #1Player clicked
            s.is1P = True
            s.SetButtons()
        elif (4<=X<6 and -3<=Y<-2) and s.state != 'Play': #2Player clicked
            s.is1P = False
            s.SetButtons()
        elif (8<=X<10 and -3<=Y<-2) and s.state != 'Play': #Save clicked
            s.SaveSetupToFile()
        elif (6<=X<8 and -3<=Y<-2) and s.state != 'Play': #Load clicked
            s.LoadSetupFromFile()
        elif (6<=X<7 and -2<=Y<-1) and s.state == 'CustomSetup': #W clicked
            s.placeColour = 'White'
            s.placeType = 'Place'
            s.SetButtons()
        elif (7<=X<8 and -2<=Y<-1) and s.state == 'CustomSetup': #B clicked
            s.placeColour = 'Black'
            s.placeType = 'Place'
            s.SetButtons()
        elif (8<=X<9 and -2<=Y<-1) and s.state == 'CustomSetup': #K clicked
            if s.placeRank == 'King':
                s.placeRank = 'Pawn'
            elif s.placeRank == 'Pawn':
                s.placeRank = 'King'
            s.placeType = 'Place'
            s.SetButtons()
        elif (9<=X<10 and -2<=Y<-1) and s.state == 'CustomSetup': #Del clicked
            if s.placeType == 'Place':
                s.placeType = 'Delete'
            elif s.placeType == 'Delete':
                s.placeType = 'Place'
            print s.placeType
            s.SetButtons()
        elif (6<=X<8 and -3<=Y<-2) and s.state == 'Play': #Quit clicked
            s.state = 'CustomSetup'
            s.SetButtons()
        elif (9<=X<11 and 8<=Y<9) and s.state != 'Play': #pTurn button clicked during setup
            if s.pTurn == 'White':
                s.pTurn = 'Black'
            elif s.pTurn == 'Black':
                s.pTurn = 'White'
            s.SetButtons()
        elif (10<=X<11 and -3<=Y<-2): #X clicked
            ExitGame(s.win)
        elif (0<=X<8 and 0<=Y<8) and s.state == 'CustomSetup': #Tile clicked in CustomSetup
            if s.tiles[X][Y].TileColour(X,Y) == 'White': #Clicked tile is white
                tkMessageBox.showinfo("Error", "Illegal Placement")
            elif s.numColour(s.placeColour) >= 12 and s.placeType == 'Place': #clicked tile would result in too many of colour being placed
                tkMessageBox.showinfo("Error", "Illegal Placement")
            else: #Valid tile update action (i.e. piece placement or deletion)
                s.tiles[X][Y] = Tile(s.win,X,Y,s.placeType == 'Place',s.placeColour,s.placeRank)    #updates that square in array
                s.SetButtons()
        elif (0<=X<8 and 0<=Y<8) and s.state == 'Play': #Tile Clicked in Play
####################################
            if s.isTileSelected: #move if able
                if s.selectedTile == s.tiles[X][Y]:
                    s.isTileSelected = False
                    s.selectedTile = ''
                elif s.pTurn == s.tiles[X][Y]:
                    s.isTileSelected = True
                    s.selectedTile = s.tiles[X][Y]
                elif s.moveIsValid(selectedTile.x,selectedTile.y,X,Y):
                    s.move()
                else:
                    tkMessageBox.showinfo("Error", "Can not move there.")
            else: #Select a Piece to move
                if s.pTurn != s.tiles[X][Y].pieceColour:
                    tkMessageBox.showinfo("Error", "Select a piece of current player's colour")
                elif not s.PieceCanCapture and s.PlayerCanCapture():
                    tkMessageBox.showinfo("Error", "Invalid selection, current player must take a piece")
                else:
                    s.isTileSelected = True
                    s.selectedTile = s.tiles[X][Y]

    def moveIsValid(s,x,y,X,Y): #parameters -> self,starting X,starting Y,final X,final Y
        if s.tiles[X][Y].isPiece: #valid if can jump target piece
            return PieceCanCapturPiece(s.tiles[x][y],s.tiles[X][Y])
        elif #valid if can jump to target location
        elif #valid if piece can travel to X,Y normally and PlayerCanCapture==False
        return valid
        
#the below few functions need conditions added to handle out of bounds errors (for being off grid, i.e. 0<=X<8 or 0<=Y<8 doesn't hold)            
    def PlayerCanCapture(s):
        for i in range(8):
            for j in range(8):
                if s.pTurn == s.tiles[i][j].pieceColour: #Current piece belongs to current player
                    if s.PieceCanCapture(s.tiles[i][j]):
                        return True
        return False

    def PieceCanCapture(s,piece):
        if piece.isWhite:
            if s.tiles[piece.x+1][piece.y+1].isBlack and \
               not s.tiles[piece.x+2][piece.y+2].isPiece:
                return True
            elif s.tiles[piece.x-1][piece.y+1].isBlack and \
                 not s.tiles[piece.x-2][piece.y+2].isPiece:
                return True
            elif piece.isKing:
                if s.tiles[piece.x+1][piece.y-1].isBlack and \
                   not s.tiles[piece.x+2][piece.y-2].isPiece:
                    return True
                elif s.tiles[piece.x-1][piece.y-1].isBlack and \
                     not s.tiles[piece.x-2][piece.y-2].isPiece:
                    return True

        elif piece.isBlack:
            if s.tiles[piece.x+1][piece.y-1].isWhite and \
               not s.tiles[piece.x+2][piece.y-2].isPiece:
                return True
            elif s.tiles[piece.x-1][piece.y-1].isWhite and \
                 not s.tiles[piece.x-2][piece.y-2].isPiece:
                return True
            elif piece.isKing:
                if s.tiles[piece.x+1][piece.y+1].isWhite and \
                   not s.tiles[piece.x+2][piece.y+2].isPiece:
                    return True
                elif s.tiles[piece.x-1][piece.y+1].isWhite and \
                     not s.tiles[piece.x-2][piece.y+2].isPiece:
                    return True

        else:
            return False

    def PieceCanCapturePiece(s,piece1,piece2): #Checks if first piece can jump the second
        if piece1.isWhite and piece2.isBlack:
            if piece1.x+1 == piece2.x and piece1.y+1 == piece2.y and \
               not s.tiles[piece1.x+2][piece1.y+2].isPiece:
                return True
            elif piece1.x-1 == piece2.x and piece1.y+1 == piece2.y and \
                 not s.tiles[piece1.x-2][piece1.y+2].isPiece:
                return True
            elif piece1.isKing:
                if piece1.x+1 == piece2.x and piece1.y-1 == piece2.y and \
                   not s.tiles[piece1.x+2][piece1.y-2].isPiece:
                    return True
                elif s.tiles[piece.x-1][piece.y-1].isBlack and \
                     not s.tiles[piece1.x-2][piece1.y-2].isPiece:
                    return True

        elif piece1.isBlack and piece2.isWhite:
            if piece1.x+1 == piece2.x and piece1.y-1 == piece2.y and \
               not s.tiles[piece1.x+2][piece1.y-2].isPiece:
                return True
            elif piece1.x-1 == piece2.x and piece1.y-1 == piece2.y and \
                 not s.tiles[piece1.x-2][piece1.y-2].isPiece:
                return True
            elif piece1.isKing:
                if piece1.x+1 == piece2.x and piece1.y+1 == piece2.y and \
                   not s.tiles[piece1.x+2][piece1.y+2].isPiece:
                    return True
                elif piece1.x-1 == piece2.x and piece1.y+1 == piece2.y and \
                     not s.tiles[piece1.x-2][piece1.y+2].isPiece:
                    return True

        else:
            return False


####################################



    def StandardSetup(s):       #defines the standard button
        s.ClearBoard()
        s.state = 'CustomSetup'       #in custom mode
        for i in range(8):
            for j in range(8):
                if s.tiles[i][j].TileColour(i,j) == 'Red' and (j < 3):
                    s.tiles[i][j] = Tile(s.win,i,j,True,'White','Pawn')
                if s.tiles[i][j].TileColour(i,j) == 'Red' and (j > 4):
                    s.tiles[i][j] = Tile(s.win,i,j,True,'Black','Pawn')
                    #places all the pieces in default checkers postitions

    def numColour(s,colour): #counts the number of pieces of a given colour
        c = 0                   #initiate counter
        for i in range(8):
            for j in range(8):
                if colour=='White' and s.tiles[i][j].isWhite:
                    c += 1
                elif colour=='Black' and s.tiles[i][j].isBlack:
                    c += 1
        return c

    #handles the setup of the board (i.e. piece placement)
    def SetupBoard(s):
        while s.state == 'CustomSetup':
            s.Click()
        if s.state == 'Play':
            s.Play()

    #handles the general play of the game
    def Play(s):
        while s.state == 'Play':
            s.Click()
        if s.state == 'CustomSetup':
            s.SetupBoard()
     
    def ClickedSquare(s,click):   #function returns the bottom left coordinate of the square clicked
        try:
            clickX = click.getX()
            clickY = click.getY()
            if clickX < 0:
                clickX = int(clickX)-1
            else:
                clickX = int(clickX)
            if clickY < 0:
                clickY = int(clickY)-1
            else:
                clickY = int(clickY)
            return clickX, clickY
        except IndexError:          #some positions on the outskirts of the screen are invalid locations
            s.Click()

    def SaveSetupToFile(s):   #method writes the tiles array to file checkers.txt
        # can have a dialog box to ask for the text file name to save to
        has_been_changed = False
        if (s.isCustom):
            s.isCustom = False
            has_been_changed = True
        saveFile = open ('checkers.txt' , 'w') #opens file to write
        for i in range(8):
            for j in range(8):
                if (s.tiles[i][j].isPiece):
                    i_string = str(i)
                    j_string = str(j)
                    saveFile.write(i_string + j_string + str(s.tiles[i][j].isPiece)[1] + \
                                   str(s.tiles[i][j].isBlack)[1] + str(s.tiles[i][j].isKing)[1] + \
                                   str(s.tiles[i][j].isPawn)[1] + str(s.tiles[i][j].isWhite)[1] + "\n")
        print "Saved to checkers.txt"
        if (has_been_changed) :
            s.isCustom = True
        saveFile.close()

    def LoadSetupFromFile(s): #method gets the setup saved and places pieces accordingly
        loadFile = open ('checkers.txt' , 'r') #opens file to read
        piece_list = loadFile.readlines()
        print "Going to clear the board and place the saved setup"
        s.ClearBoard()
        for i in range(len(piece_list)):
            tot_string = piece_list[i]
            x_var = int(tot_string[0])
            y_var = int(tot_string[1])
            #True is 'r', False is 'a'
            if (tot_string[2] == 'r'): #it is a piece
                if (tot_string[3] == 'r'): #piece is black
                    if (tot_string[4] == 'r'): #piece is black King
                        s.tiles[x_var][y_var] = Piece(s.win,x_var,y_var,'Black','King',True)
                    else : #piece is a black pawn
                        assert(tot_string[5] == 'r')
                        s.tiles[x_var][y_var] = Piece(s.win,x_var,y_var,'Black','Pawn',True)
                else: #piece is white
                    assert(tot_string[6] == 'r')
                    if (tot_string[4] == 'r'): #piece is white King
                        s.tiles[x_var][y_var] = Piece(s.win,x_var,y_var,'White','King',True)
                    else: #piece is white pawn
                        assert(tot_string[5] == 'r')
                        s.tiles[x_var][y_var] = Piece(s.win,x_var,y_var,'White','Pawn',True)
        loadFile.close()

class Tile:                                #defines a tile and holds its current state
    def __init__(s,win,X,Y,isPiece,pieceColour='',pieceType=''):
        s.win = win
        s.x = X
        s.y = Y
        s.isPiece = isPiece
        s.isWhite = ('White' == pieceColour) and s.isPiece
        s.isBlack = ('Black' == pieceColour) and s.isPiece
        s.isKing = ('King' == pieceType) and s.isPiece
        s.isPawn = ('Pawn' == pieceType) and s.isPiece
        if s.isWhite:
            s.pieceColour = 'White'
        elif s.isBlack:
            s.pieceColour = 'Black'
        if s.isKing:
            s.pieceType = 'King'
        elif s.isPawn:
            s.pieceType = 'Pawn'

        s.ColourButton(s.TileColour(s.x,s.y),s.x,s.y)
        if s.isPiece:
            s.DrawPiece()  

    def ColourButton(s,colour,X,Y,width=1,height=1):        #function to create a rectangle with a given colour, size, and location
        rect = Rectangle(Point(X,Y),Point(X+width,Y+height))
        rect.setFill(colour)
        rect.draw(s.win)
            
    def TileColour(s,x,y):
        if (x%2 == 0 and y%2 == 0) or (x%2 == 1 and y%2 == 1):
            return 'Red'   #sets every other square to red 
        else:
            return 'White' #every non red square to white

    def DrawPiece(s):        
        c = Point(s.x+.5,s.y+.5)
        circ = Circle(c,0.4)
        circ.draw(s.win)

        if s.isWhite:
            col1,col2 = 'White','Black'
        elif s.isBlack:
            col1,col2 = 'Black','White'

        circ.setFill(col1)

        if s.isKing:
            kingTxt = Text(c,'K')
            kingTxt.draw(s.win)
            kingTxt.setFill(col2)

def ExitGame(win):
    win.close()
    sys.exit()
    
game = Checkers()


