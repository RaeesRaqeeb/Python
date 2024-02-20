#Tic Tak To
# Code by : Tayra Raqeeb
from ast import In
from tabnanny import check
import sys
import os
global row1
row1=[' ','|',' ','|',' ']
global row2
row2=[' ','|',' ','|',' ']
global row3
row3=[' ','|',' ','|',' ']

def Inputing(input,row,col):
    global row1
    global row2
    global row3
    if(row==0):
        if(col==0):
            if(row1[col]==' '):
                row1[col]=input
            else:
                return 0
            
        elif(col==1):
            if(row1[col+1]==' '):
                row1[col+1]=input
            else:
                return 0
        elif(col==2):
            if(row1[col+2]==' '):
                row1[col+2]=input
            else:
                return 0
    elif(row==1):
        if(col==0):
            if(row2[col]==' '):
                  row2[col]=input
            else:
                return 0
        elif(col==1):
            if(row2[col+1]==' '):
                row2[col+1]=input
            else:
                return 0
        elif(col==2):
            if(row2[col+2]==' '):
                row2[col+2]=input    
            else:
                return 0    
    elif(row==2):
        if(col==0):
            if(row3[col]==' '):
                row3[col]=input
            else:
                return 0
        elif(col==1):
            if(row3[col+1]==' '):
                row3[col+1]=input
            else:
                return 0
        elif(col==2):
            if(row3[col+2]==' '):
                row3[col+2]=input
            else:
                return 0
    return display_board(row1,row2,row3)

# Displaying Board
def display_board(row1,row2,row3):
    os.system('clear')
    line=['----------']
    print(row1[0],row1[1],row1[2],row1[3],row1[4])
    print(line[0])
    print(row2[0],row2[1],row2[2],row2[3],row2[4])
    print(line[0])
    print(row3[0],row3[1],row3[2],row3[3],row3[4])
    # Condition for checking if the Player 1 or Player 2 is win or not
    if((row1[0]=='X' and row1[2]=='X' and row1[4]=='X') or (row1[4]=='X' and row2[2]=='X' and row3[0]=='X')or(row1[0]=='X' and row2[2]=='X' and row3[4]=='X')or(row1[0]=='X'and row2[0]=='X'and row3[0]=='X')or(row3[0]=='X'and row3[2]=='X' and row3[4]=='X') or (row1[4]=='X' and row2[4]=='X' and row3[4]=='X')or(row1[2]=='X' and row2[2]=='X' and row3[2]=='X') or(row2[0]=='X' and row2[1]=='X' and row2[2]=='X')):
        return 1
    elif((row1[0]=='O' and row1[2]=='O' and row1[4]=='O') or(row1[0]=='O' and row2[2]=='O' and row3[4]=='O')or(row1[0]=='O'and row2[0]=='O'and row3[0]=='O')or(row3[0]=='O'and row3[2]=='O' and row3[4]=='O') or (row1[4]=='O' and row2[4]=='O' and row3[4]=='O')or(row1[2]=='O' and row2[2]=='O' and row3[2]=='O') or(row2[0]=='O' and row2[1]=='O' and row2[2]=='O')):
        return 2
    else:
        # Case for Game Draw
        counter=0
        counter2=0
        counter3=0
        for x,y,z in zip(row1,row2,row3):
            if(x!=' '):
                counter+=1
            if(y!=' '):
                counter2+=1
            if(z!=' '):
                counter3+=1
        if(counter==len(row1) and counter2==len(row2) and counter3==len(row3)):
            return 3
    

    


#main function

print("TIC TAK TO GAME")
checker=[]

while(1):
    Position_checker1=0
    while(Position_checker1!=1):
        # Player 1 
        print("Player 1 input(0,1,2):")
        print("ROw:")
        row=(input())
        if(row.isdigit()):
            
            print("Col")
            row=int(row)
            col=int(input())
            # Check for input range
            if((row>=0 and row<=2) and(col>=0 and col<=2))!=True:
                print("Enter only (0,1,2) according to the indexes of rows and columns")
                continue
            winning_value1=Inputing('X',row,col)
            if(winning_value1==1):
                print("Player 1 win the game")
                sys.exit()
                
            elif(winning_value1==2):
                print("Player 2 win the game")
                sys.exit()
                
            if(winning_value1==0):
                print("\nWrong input position already occupied")
                pass
            elif(winning_value1==3):
                print("Game Draw")
                sys.exit()
            else:
                Position_checker1+=1
            Position_checker=0
        # Player 2
            while(Position_checker!=1):
                print("Player 2 input:")
                print("Row:")
                row=input()
                if(row.isdigit()!=True):
                    print("Wrong input:")
                    pass
                else:
                    row=int(row)
                    print("Col:")
                    col=int(input())
                    if((row>=0 and row<=2) and(col>=0 and col<=2))!=True:
                        print("Enter only (0,1,2) according to the indexes of rows and columns")
                        continue                   
                    sum2=int(row+col)
                    winning_value2=Inputing('O',row,col) 
                    if(winning_value2==0):
                        print("Wrong input position, input again")
                        pass
                    else:
                        Position_checker+=1
                    if(winning_value2==1):
                        sys.exit()
                    elif(winning_value2==2):
                        sys.exit()
        else:
            print("\n*******Wrong input: enter from 0,1,2 according to indexes************\n")








