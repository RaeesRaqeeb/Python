import math

class Line:

    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
       result= (self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2
       print(math.sqrt(result))
    
    def slope(self):
        value=(self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])
        print("Slope of the given value:",value)


#main function

coordinate1=(3,2)
coordinate2=(8,10)

li=Line(coordinate1,coordinate2)

li.distance()
li.slope()




