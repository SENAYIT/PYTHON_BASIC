
#exerice2nd

birth_date=input('enter your birth date : ')
print(type(birth_date))  # to know class (type ) of birth ,,class str

now=input('enter what is the date now? : ')
print(type(now)) # class str


age = int(now) - int(birth_date)

print(type(age)) # class int

print("your age is : " ,age) # must not use "+" for concatnet in type of int use "," but only in str 




#class work 

weight=input('please enter your weight in pounds : ')

weight_in_Kg=int(weight)*1000

print('your weight in Kg is ' ,weight_in_Kg)


