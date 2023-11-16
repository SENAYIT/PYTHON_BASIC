
# class

class Point:
    def draw(self):
        print('draw')
    
    def move(self):
        print('move')
  
point1=Point()
point1.x=20
point1.draw() # more prefferale 
Point().draw() #it is the same with the above

print(point1.x)

point2=Point()
#print(point2.x) # AttributeError: 'Point' object has no attribute 'x'