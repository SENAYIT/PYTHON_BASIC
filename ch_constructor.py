
#class challenge

class Person:
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        print('talk that you want to talk me ...')

    def talk2(self):
        print(f'{self.name} talk that you want to talk me ...')
        print('end')


person1=Person('senay')

print (person1.name)
person1.talk()


person1.talk2() # the same with the first two statement as  together in short.
