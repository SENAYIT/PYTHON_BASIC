a = "Hello World!"
b = a.split()
print(b)


a = "Hello, World!"
b = a.split()
print(b)

a = "Hello, World!"
b = a.split(",")
print(b)

""" outputs difference
['Hello', 'World!']
['Hello,', 'World!']
['Hello', ' World!']

"""