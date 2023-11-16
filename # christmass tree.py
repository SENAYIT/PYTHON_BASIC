# christmass tree

for star in range(1, 6):
    intial=int(star)//2 
    for space in range(intial , 0): 
        if int(star) % 2 == 1:
            spaces= '  ' * int(space)
            stars=' * ' * int(star)          
            print(f"{spaces} {stars} {spaces}")

             
            #print(' ' * int(space), ' * ' * int(star), ' ' * int(space))