
#car game

choise=' '

while True:  #while True:    # while choise!='quit':

    choise=input('Enter your choise please : >').lower()
  

    if choise=='help':
         print(f''' Please type
        'start' - a car ready to go 
        'stop' - a car stopped
        'quit' - to exit the game ''')
   
    elif choise=='start':
        print('a car ready to go...')

    elif choise=='stop':
         print(' a car stopped !' )
    
    elif choise=='quit' :
        break
    
    else:
         print('you are incorrect please try again !!!')


       # elif choise!='quit' :
          # print('you are incorrect please try again !!!')
        

        


  