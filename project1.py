
#project 1

weight = int(input('Enter your weight : '))
unit=input("weight in (L) or (KG) : ")

if unit .upper() == 'L':
   converted =weight / 0.45
   print(f"your weight in Kg is: {converted} Kg")

elif unit .upper() == 'KG':
    converted=weight * 0.45
    print(f"your weight in Pound is: {converted} pounds")

else:
    print('please enter your weight...')
