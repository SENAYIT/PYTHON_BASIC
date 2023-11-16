#functions

def greet_user(): #declaration of function
    print('hi there.')
    print('welcome abroad !!')


print('start')   
greet_user()  #call function
print('finished.')


#function with parameter can use more than one

def greet_user(name): #declaration of function with parameter
    print(f'hi {name} .')
    print('welcome abroad !!')


print('start')   
greet_user('john')  #call function
print('finished.')


#function with parameter can use more than one

def greet_user(first_name,last_name): #declaration of function with 2 parameter
    print(f'hi {first_name} {last_name}')
    print('welcome abroad !!')

print('start')   
greet_user('john','smith')  #call function with 2 argument
print('finished.')

#function with keyword parameter can use more than one

def greet_user(first_name,last_name): #declaration of function with 2 parameter
    print(f'hi {first_name} {last_name}')
    print('welcome abroad !!')

print('start')   

greet_user('john',last_name='smith')  #call function with 2 argument in keyword arg. after pos.arg.
greet_user(last_name='john',first_name='smith')  #call function with 2 argument in keyword arg. after pos.arg.

print('finished.')


