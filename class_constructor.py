
#constructor

class Point:

    def __init__(self,x,y): # constructor - it means must value in intialization in the first before we use 
        self.x=x
        self.y=y

    def draw(self):
        print('draw')
    
    def move(self):
        print('move')
  
point1=Point(5,'hi') # like this intialisation  the first  thing
point1.draw()

print(point1.x)

point1.x=30

print(point1.x)

print(point1.y)
