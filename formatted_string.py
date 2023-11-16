#formatted_string.py

first='john'
last='smith'

  # all are the same
message=  first + ' [' + last  + '] is a coder' # using by concstenate as before
msg= f'{first} [{last}] is a coder'  # use f as prefix , '  ' and { } for variables inside

print(message)
print(msg)
