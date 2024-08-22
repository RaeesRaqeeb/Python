import math

def Finding_angle(x,y):
        third_side=math.sqrt((x**2)+(y** 2))
        print(third_side)
        angle=math.asin((third_side/2)/y)
        angle_degree=math.degrees(angle)
        angle_degree=round(angle_degree)
        print(f"{angle_degree}°" )

#main function
        
print("Enter the length of perpendicular and base of a triangle whose one angle is 90:")
perpendicular=int(input("\nPerpendicular side:"))
base=int(input("\nBase of triangle:"))
Finding_angle(perpendicular,base)
