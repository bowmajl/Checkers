from graphics import *
import sys

#king pieces need to place kings not standard
#only place 12 of each colour
#add functionality to play button so program knows to exit custom board
#when leaving custom setup erase white black and king buttons
#maybe others, will get to it tomorrow most likely so post somewhere if you edit this




class Board:

    
    def __init__(s):
        s.win = GraphWin('Checkers',600,600)   #draws screen
        s.win.setBackground("white")
        s.win.setCoords(-1,-3,9,9)              #creates a coordinate system for the window
        s.ClearBoard()
        s.isCustom = False
        s.isStart = False
        s.PlaceColour = 'White'
        s.isKing = 'null'           #refers to state of a piece i.e. Pawn/King


        letters = ['A','B','C','D','E','F','G','H',]
        for i in range(8):
            gridTxt = Text(Point(-0.5,i+0.5),i+1).draw(s.win)    #left and right numbers for grid
            gridTxt = Text(Point(8.5,i+0.5),i+1).draw(s.win)
            gridTxt = Text(Point(i+0.5,-0.5),letters[i]).draw(s.win)     #bottom and top letters
            gridTxt = Text(Point(i+0.5,8.5),letters[i]).draw(s.win)     
            
##        s.sqr = Rectangle(Point(6,-1),Point(7,-1))    
##        s.sqr.setFill('Red')
##        s.sqr.draw(s.win)
##        ExtTxt = Text(Point(6.5,-1.5),'Test Mode')
##        ExtTxt.draw(s.win)
            
## Does nothing but its here for reference code at the moment

         
        ColourRect(s.win,-1,-3,1,-1,'White')   #These 4 lines create the buttons (which are inactive right now)
        ColourRect(s.win,1,-3,3,-1,'White')
        ColourRect(s.win,-1,-2,1,-1,'White')
        ColourRect(s.win,1,-2,3,-1,'White')

        ColourRect(s.win,4,-3,6,-2,'White')
        ColourRect(s.win,6,-3,8,-2,'White')
        ColourSquare(s.win,8,-3,'Red')

        ColourSquare(s.win,3,-3,'White')
        ColourSquare(s.win,3,-2,'White')
        ColourSquare(s.win,4,-2,'White')
        ColourSquare(s.win,5,-2,'White')
        ColourSquare(s.win,6,-2,'White')
        ColourSquare(s.win,7,-2,'White')
        ColourSquare(s.win,8,-2,'White')

##        
##        ColourRect(s.win,-1,-3,1,-2,'White')
##        ColourRect(s.win,1,-3,3,-2,'White')
##        
        Standardtxt = Text(Point(0,-1.3),'Standard').draw(s.win)  #These sets of 2 add the text to the buttons
        BoardStxt = Text(Point(0,-1.7),'Setup').draw(s.win)
        Customtxt = Text(Point(0,-2.3),'Custom').draw(s.win)  
        BoardCtxt = Text(Point(0,-2.7),'Setup').draw(s.win)
        Cleartxt = Text(Point(2,-2.3),'Clear').draw(s.win)
        BoardCltxt = Text(Point(2,-2.7),'Board').draw(s.win)
        Start_txt = Text(Point(2,-1.5),'Start!').draw(s.win)

        Save_txt = Text(Point(5,-2.5),'Save').draw(s.win)
        Load_txt = Text(Point(7,-2.5),'Load').draw(s.win)
        Exit_txt = Text(Point(8.5,-2.5),'X')
        Exit_txt.draw(s.win)
        Exit_txt.setFill('White')
        
 
        s.SetPieces()

    def SetPieces(s):   #so multiple clicks can happen without errors
        while not s.isStart:
            s.Click()

        #The following is temporary and is as a conclusion to assign 1

        s.win.close()
        w = GraphWin('Checkers Start Time')
        w.setCoords(0,0,10,10)
        txt = Text(Point(5,5),'Game will now begin..later').draw(w)
        txt = Text(Point(5,4),'..in assign2').draw(w)
        


    def Click(s):
        click = s.win.getMouse()
        X, Y = s.ClickedSquare(click)
        if (X==8 and Y==-3):         #if exit button (in bottom right) is pressed
            ExitGame(s.win)
        elif (1<=X<3 and Y==-2):    #Clicked Start!
            s.isStart = True
            s.isCustom = False
        elif (-1<=X<1 and Y == -2):   #if mouse click is in standard board button range
            s.StandardSetup()
        elif (1<=X<3 and Y == -3):  #if mouse click is in clear board button range
            s.ClearBoard()
        elif (-1<=X<1 and Y == -3):   #if click custom setup
            s.CustomSetup()
        elif (s.isCustom and s.PlaceColour == 'Black' and X==4 and Y==-2 and s.Place):   #if W is clicked
            
            s.PlaceColour = 'White'
        
            ColourSquare(s.win,4,-2,'Green')
            txt = Text(Point(4.5,-1.5),'W').draw(s.win)
            
            ColourSquare(s.win,5,-2,'Red')
            txt = Text(Point(5.5,-1.5),'B').draw(s.win)
        elif (s.isCustom and s.PlaceColour == 'White' and X==5 and Y==-2 and s.Place):  # if B is clicked
            
            s.PlaceColour = 'Black'
        
            ColourSquare(s.win,4,-2,'Red')
            txt = Text(Point(4.5,-1.5),'W').draw(s.win)
            
            ColourSquare(s.win,5,-2,'Green')
            txt = Text(Point(5.5,-1.5),'B').draw(s.win)
        elif (s.isCustom and s.PlaceState == 'Pawn' and X==6 and Y==-2 and s.Place): #if K is clicked and it is false already
            s.PlaceState = 'King'
            ColourSquare(s.win,6,-2,'Green')
            txt = Text(Point(6.5,-1.5),'K').draw(s.win)
        elif (s.isCustom and s.PlaceState == 'King' and X==6 and Y==-2 and s.Place): #if K is clicked and it is true already
            s.PlaceState = 'Pawn'
            ColourSquare(s.win,6,-2,'Red')
            txt = Text(Point(6.5,-1.5),'K').draw(s.win)
        elif (X==7 and Y==-2 and s.Place == False):     #pressed delete (to stop deleting)
            s.Place = True
            s.PlaceColour = 'White'
            s.PlaceState = 'Pawn'
            
            ColourSquare(s.win,4,-2,'Green')   #makes white button green, and others red below
            WTxt = Text(Point(4.5,-1.5),'W')
            WTxt.draw(s.win)
            
            ColourSquare(s.win,5,-2,'Red')
            BTxt = Text(Point(5.5,-1.5),'B')
            BTxt.draw(s.win)
            
            ColourSquare(s.win,6,-2,'Red')
            KTxt = Text(Point(6.5,-1.5),'K')
            KTxt.draw(s.win)

            ColourSquare(s.win,7,-2,'Black')
            deleteTxt = Text(Point(7.5,-1.5),'Del')
            deleteTxt.draw(s.win)
            deleteTxt.setFill('White')
            
        elif (X==7 and Y==-2 and s.Place == True):      #pressed delete (to start deleting)
            s.Place = False
            s.PlaceColour = 'White'
            s.PlaceState = 'Pawn'

            ColourSquare(s.win,4,-2,'Red')   #makes white button green, and others red below
            WTxt = Text(Point(4.5,-1.5),'W')
            WTxt.draw(s.win)
            
            ColourSquare(s.win,5,-2,'Red')
            BTxt = Text(Point(5.5,-1.5),'B')
            BTxt.draw(s.win)
            
            ColourSquare(s.win,6,-2,'Red')
            KTxt = Text(Point(6.5,-1.5),'K')
            KTxt.draw(s.win)
            
            ColourSquare(s.win,7,-2,'Green')
            deleteTxt = Text(Point(7.5,-1.5),'Del')
            deleteTxt.draw(s.win)
            
        elif (0<=X<8 and 0<=Y<8 and s.isCustom and (((s.numWhite() < 12 or s.PlaceColour != 'White') and (s.numBlack() < 12 or s.PlaceColour != 'Black')) or not s.Place)):                    #within range of board
            if (X%2 == 0 and Y%2 == 0) or (X%2 == 1 and Y%2 == 1):  #only on red squares
                s.P_array[X][Y] = Piece(s.win,X,Y,s.PlaceColour,s.PlaceState,s.Place)    #updates that square in array
                print s.numWhite()      #testing only
                print s.numBlack()      #testing only

        elif 0<=X<8 and 0<=Y<8 and s.isCustom and ((s.numWhite >= 12 and s.PlaceColour == 'White' and s.Place) or (s.numBlack >= 12 and s.PlaceColour == 'Black' and s.Place) or (not((X%2 == 0 and Y%2 == 0) or (X%2 == 1 and Y%2 == 1)))):
            w = GraphWin('Warning')
            w.setCoords(0,0,10,10)
            Text(Point(5,8),'Warning illegal placement!').draw(w)
            ColourSquare(s.win,5,4,'White')
            Text(Point(5.5,4.5),'OK').draw(w)
            while True:
                s.ClickInWarningWin(w)
            

    def ClickInWarningWin(w):
        click = win.getMouse()
        try:
            X, Y = int(click.getX()), int(click.getY())

            if X==5 and Y==4:
                w.close()
        except IndexError:
                s.ClickInWarningWin(w)

        

    def CustomSetup(s):         #gives functionality to the custom button
        s.isCustom = True       #selects custom mode
        s.PlaceColour = 'White' #defaults the next colour to white
        s.PlaceState = 'Pawn'   #defaults to not a king

        s.Place = True          #False if removing a piece
        #delete piece funtionality
        
        ColourSquare(s.win,4,-2,'Green')   #makes white button green, and others red below
        WTxt = Text(Point(4.5,-1.5),'W')
        WTxt.draw(s.win)
        
        ColourSquare(s.win,5,-2,'Red')
        BTxt = Text(Point(5.5,-1.5),'B')
        BTxt.draw(s.win)
        
        ColourSquare(s.win,6,-2,'Red')
        KTxt = Text(Point(6.5,-1.5),'K')
        KTxt.draw(s.win)

        ColourSquare(s.win,7,-2,'Black')
        deleteTxt = Text(Point(7.5,-1.5),'Del')
        deleteTxt.draw(s.win)
        deleteTxt.setFill('White')

        while s.isCustom:               
            s.Click()

        ColourSquare(s.win,4,-2,'White')
        ColourSquare(s.win,5,-2,'White')
        ColourSquare(s.win,6,-2,'White')
        ColourSquare(s.win,7,-2,'White')
        WTxt.undraw()
        BTxt.undraw()
        KTxt.undraw()
        deleteTxt.undraw()

                        
    def StandardSetup(s):       #defines the standard button
        s.ClearBoard()
        s.isCustom = False       #not in custom mode
        for j in range(8):
            for i in range(8):
                if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and (j < 3):
                    s.P_array[i][j] = Piece(s.win,i,j,'White','Pawn',True)
                if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and (j > 4):
                    s.P_array[i][j] = Piece(s.win,i,j,'Black','Pawn',True)
                    #places all the pieces in standard order

    def numWhite(s):
        c = 0
        for j in range(8):
            for i in range(8):
                if s.P_array[i][j].isWhite:
                    c += 1
        return c

    def numBlack(s):
        k = 0
        for j in range(8):
            for i in range(8):
                if s.P_array[i][j].isBlack:
                    k += 1
        return k
                
    def ClearBoard(s):
        s.P_array=[[Piece(s.win,i,j,'null','null',False) for i in range(8)] for j in range(8)]  #creates the 2D list and initializes all 8x8 entires to 1
        for j in range(8):
            for i in range(8):
                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                    s.colour = 'Red'   #sets every other squre to red 
                else:
                    s.colour = 'White' #every non red square to white 
                ColourSquare(s.win,i,j,s.colour)


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
        except IndexError:
            s.Click()
            
            
def ColourRect(win,Xmin,Ymin,Xmax,Ymax,colour):        #function to create a rectangle with a given colour and size
    rect = Rectangle(Point(Xmin,Ymin),Point(Xmax,Ymax))
    rect.setFill(colour)
    rect.draw(win)                
def ColourSquare(win,X,Y,colour):
    sqr = Rectangle(Point(X,Y),Point(X+1,Y+1))      #makes a 1x1 square with a given colour
    sqr.setFill(colour)
    sqr.draw(win)

def ExitGame(win):
    win.close()
    sys.exit()



class Piece:                                #creates a piece
    def __init__(s,win,X,Y,colour,state,isPiece):
        s.x = X
        s.y = Y
        s.isPiece = isPiece
        s.isWhite = ('White' == colour) and s.isPiece
        s.isBlack = ('Black' == colour) and s.isPiece
        s.isKing = ('King' == state) and s.isPiece
        s.isPawn = ('Pawn' == state) and s.isPiece
        
        
        if s.isPiece:
            s.c = Point(s.x+.5,s.y+.5)
            s.circ = Circle(s.c,0.4)
            s.circ.draw(win)
            
            if s.isWhite and s.isKing:              #WK
                s.circ.setFill('White')
                kingTxt = Text(s.c,'K').draw(win)
            elif s.isBlack and s.isKing:            #BK
                s.circ.setFill('Black')
                kingTxt = Text(s.c,'K')
                kingTxt.draw(win)
                kingTxt.setTextColor('White')
            elif s.isWhite:                         #W
                s.circ.setFill('White')
            elif s.isBlack:                         #B
                s.circ.setFill('Black')
        else:
            if (s.x%2 == 0 and s.y%2 == 0) or (s.x%2 == 1 and s.y%2 == 1):
                s.colour = 'Red'   #sets every other squre to red 
            else:
                s.colour = 'White' #every non red square to white 
            ColourSquare(win,s.x,s.y,s.colour)
        


    
        
board = Board()


