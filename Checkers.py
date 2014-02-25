from graphics import *
import sys

class Board:

    P_array=[[1 for x in range(8)] for y in range(8)]
    
    def __init__(s):
        s.win = GraphWin('Checkers',400,400)
        s.win.setCoords(0,-1,8,8)
        for j in range(8):
            for i in range(8):
                if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
                    s.colour = 'Black'
                else:
                    s.colour = 'White'
                    
                ColourSquare(s.win,i,j,s.colour)

                if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and (j < 3):
                    s.P_array[i][j] = Piece(s.win,i,j,'Red')
                if ((i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1)) and (j > 4):
                    s.P_array[i][j] = Piece(s.win,i,j,'Blue')

        s.sqr = Rectangle(Point(6,-1),Point(7,-1))
        s.sqr.setFill('Red')
        s.sqr.draw(s.win)
        ExtTxt = Text(Point(6.5,-.5),'Test Mode')
        ExtTxt.draw(s.win)
        print s.P_array[1][1].colour
        print s.P_array[1][2]
        print s.P_array[1][2] #.colour
        print s.P_array[2][2].colour
        print s.P_array[5][1].colour
        print s.P_array[7][7].colour

        #play()
            
                
def ColourSquare(win,X,Y,colour):
    sqr = Rectangle(Point(X,Y),Point(X+1,Y+1))
    sqr.setFill(colour)
    sqr.draw(win)

def ExitGame(win):
    win.close()
    sys.exit()

def initialize_twodlist(foo):
    twod_list = []
    new = []
    for i in range (8):
        for j in range (8):
            new.append(foo)
        twod_list.append(new)
        new = []

class Piece:
    def __init__(s,win,X,Y,colour):
        s.x = X
        s.y = Y
        s.colour = colour
        s.c = Point(s.x+.5,s.y+.5)
        s.circ = Circle(s.c,0.4)
        s.circ.draw(win)
        s.circ.setFill(colour)


    



    def ClickedSquare(s,click):
        try:
            clickX = click.getX()
            clickY = click.getY()
            if clickX < 0:
                clickX = int(clickX) - 1
            else:
                clickX = int(clickX)
            if clickY < 0:
                clickY = int(clickY) - 1
            else:
                clickY = int(clickY)
            return clickX, clickY
        except IndexError:
            s.Click()


    def Click(s):
        click = s.win.getMouse()
        X, Y = s.ClickedSquare(click)
        if X == s.x-1 and (Y == -2 or Y == -1):
            s.disarmClick = not s.disarmClick
            s.UpdateDisarmSpace()
        elif s.disarmClick:
            s.disarmClick = False
            s.UpdateDisarmSpace()
            s.DisarmClicked(X,Y)
        elif s.squares[X][Y] != 10 and X >= 0 and Y >= 0:
            s.TriggerSquare(X,Y)

        
        
board = Board()


