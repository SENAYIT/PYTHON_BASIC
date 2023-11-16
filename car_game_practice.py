

#practice_car_game

start=False
choise=' '

while True: 

    choise=input('Enter your choise please : >').lower()
   
    if choise=='help':
        print(f''' Please type
        'start' - a car ready to go 
        'stop' - a car stopped
        'quit' - to exit the game ''')
            
    elif choise=='start':
        if start:
            print('the car already started !.')
        else:
            start=True # if it the car stop ,make it start and say the car ready to go
            print('a car ready to go...')

    elif choise=='stop':
        if  not start:
            print(' the car is already stopped !' )
        else:
            start=False  # if it started make stop and say the car is stopped.
            print(' the car is stopped !' )

    
    elif choise=='quit' :
        break
    
    else:
         print('you are incorrect please try again !!!')
