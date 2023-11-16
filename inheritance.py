

#inheritnce

class Mammal:

    def walk(self):
        print('walk')

class Bird:

    pass # if we want to empty do this
      
class Dog(Mammal): # write inside the braket the name of inherite class if you don't want ,it can empty remove bracket 

    def bark(self):
        print('bark')
    

class Cat(Mammal): # write inside the brachet the name of inherite class

    def be_annoying(self):
        print('annoying')


dog1=Dog()
dog1.walk()

cat1=Cat()
cat1.be_annoying()


  
