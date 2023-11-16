
#exception_ how to handle the error in python,, by using 'try' and 'except'
  # in except _I must write the error type  to handle the error 


try:
    age=int(input('Enter your AGE: ' ))
    print('your AGE is : ' ,age)

    result=100/age
    print('100/ age is: ',result)

except ZeroDivisionError: # I must write the error type  to handle the error 
    print('you canot enter 0 !!!')

except ValueError:
    print('INVALID AGE !!!')