from graphics import *
import sys

class Board:

    
    def __init__(s):
        s.win = GraphWin('Checkers',600,600)   #draws screen
        s.win.setCoords(-1,-3,9,9)              #creates a coordinate system for the window
        s.ClearBoard()
                

        letters = ['A','B','C','D','E','F','G','H',]
        for i in range(8):
            gridTxt = Text(Point(-0.5,i+0.5),i+1)    #left and right numbers for grid
            gridTxt.draw(s.win)
            gridTxt = Text(Point(8.5,i+0.5),i+1)
            gridTxt.draw(s.win)
            
            gridTxt = Text(Point(i+0.5,-0.5),letters[i])     #bottom and top letters
            gridTxt.draw(s.win)        
            gridTxt = Text(Point(i+0.5,8.5),letters[i])     
            gridTxt.draw(s.win)
            
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
##        
##        ColourRect(s.win,-1,-3,1,-2,'White')
##        ColourRect(s.win,1,-3,3,-2,'White')
##        
        Standardtxt = Text(Point(0,-1.3),'Standard')  #These sets of 2 add the text to the buttons
        Standardtxt.draw(s.win)
        BoardStxt = Text(Point(0,-1.7),'Board')
        BoardStxt.draw(s.win)
        Customtxt = Text(Point(0,-2.3),'Custom')  
        Customtxt.draw(s.win)
        BoardCtxt = Text(Point(0,-2.7),'Board')
        BoardCtxt.draw(s.win)        
        Cleartxt = Text(Point(2,-2.3),'Clear')
        Cleartxt.draw(s.win)
        Start_txt = Text(Point(2,-1.5),'Start!')
        Start_txt.draw(s.win)
        BoardCltxt = Text(Point(2,-2.7),'Board')
        BoardCltxt.draw(s.win)        


        
##        WPtxt = Text(Point(0,-2.5),'White Piece')
##        WPtxt.draw(s.win)
##        BPtxt = Text(Point(2,-2.5),'Black Piece')
##        BPtxt.draw(s.win)
        
        s.SetPieces()

    def SetPieces(s):
        while True:
            s.Click()


    def Click(s):
        click = s.win.getMouse()
        X, Y = s.ClickedSquare(click)
        if (-1<=X<1 and Y == -2):   #if mouse click is in standard board button range
            s.StandardSetup()
        elif (1<=X<3 and Y == -3):  #if mouse click is in clear board button range
            s.ClearBoard()
        elif (-1<=X<1 and Y == -3):
        if (0<=X<8 and 0<=Y<8):  #if in board range
            if (X%2 == 0 and Y%2 == 0) or (X%2 == 1 and Y%2 == 1): #if on red squares
                s.P_array[X][Y] = Piece(s.win,X,Y,'White')
                
    def StandardSetup(s):
        s.ClearBoard()
        for j in range(8):
            for i in range(8):
                if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and (j < 3):
                    s.P_array[i][j] = Piece(s.win,i,j,'White')
                if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and (j > 4):
                    s.P_array[i][j] = Piece(s.win,i,j,'Black')
                    #places all the pieces in standard order

    def ClearBoard(s):
        s.P_array=[[1 for x in range(8)] for y in range(8)]  #creates the 2D list and initializes all 8x8 entires to 1
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


        #play()
            
def ColourRect(win,Xmin,Ymin,Xmax,Ymax,colour):
    rect = Rectangle(Point(Xmin,Ymin),Point(Xmax,Ymax))
    rect.setFill(colour)
    rect.draw(win)                
def ColourSquare(win,X,Y,colour):
    sqr = Rectangle(Point(X,Y),Point(X+1,Y+1))
    sqr.setFill(colour)
    sqr.draw(win)

def ExitGame(win):
    win.close()
    sys.exit()

##def initialize_twodlist(foo):
##    twod_list = []
##    new = []
##    for i in range (8):
##        for j in range (8):
##            new.append(foo)
##        twod_list.append(new)
##        new = []

class Piece:
    def __init__(s,win,X,Y,colour):
        s.x = X
        s.y = Y
        s.colour = colour
        s.c = Point(s.x+.5,s.y+.5)
        s.circ = Circle(s.c,0.4)
        s.circ.draw(win)
        s.circ.setFill(colour)


    
##def Click(s):
##    click = s.win.getMouse()
##    X, Y = s.ClickedSquare(click)
##    if X == s.x-1 and (Y == -2 or Y == -1):
##        s.disarmClick = not s.disarmClick
##        s.UpdateDisarmSpace()
##    elif s.disarmClick:
##        s.disarmClick = False
##        s.UpdateDisarmSpace()
##        s.DisarmClicked(X,Y)
##    elif s.squares[X][Y] != 10 and X >= 0 and Y >= 0:
##        s.TriggerSquare(X,Y)







        
        
board = Board()


