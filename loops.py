
#loops

i=0
while i<=5:
    print(i)
    i=i+1
print('done')

i=0
while i<=5:
    print('*' * i)
    i=i+1



#class work

a=9

j=1
while j<=3:

    b=int(input('GUESS the no. : '))
    if a==b:   
        print('you win ')
        break
    else:
        if  j==3:
            print("you fail")
    j=j+1
    
# learn it is same out put

a=9

j=1
while j<=3:

    b =int(input('GUESS the no. : '))
    j=j+1

    if a==b:   
        print('you win ')
        break
else:
    print(" sorry you fail")
    

  
    

