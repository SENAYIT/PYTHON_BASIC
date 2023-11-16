
# tuples , unPacking , Dictionaries

#tuples -it can be only count and index not access other methods

tup=(1,2,3)
 
print(tup)


print(tup.index(3)) 

tup.count(2)
print(tup.count(2))

print(tup[2])

coordinates=(1,2,3)

x=coordinates[0]
y=coordinates[1]
z=coordinates[2]

print(x,y,z)

#the same with below is called UNPACKING the below one it can work for list
x,y,z=coordinates
print(x,y,z)


#dictionary - not have the same name,

docment={
    "name":'senay awoke',
    "age":'12',
    "phone":1234
}

print(docment.get("name")) # they all the same with the second,dict must be find by "their string name" for each all index
print(docment['name'])

docment["age"]=20  # it changes the first age value and save it. i can use with out " " to nos. but not to string 
print(docment)



#practice time

print(len(docment))

d1=docment.copy()
print(d1)


print(docment.items()) #it's output - dict_items([('name', 'senay awoke'), ('age', 20), ('phone', 1234)])


docment.fromkeys('name')
print(docment.fromkeys('name age'))  #??output - {'n': None, 'a': None, 'm': None, 'e': None, ' ': None, 'g': None}


print(docment.keys()) # displays dictionarie's key_output - dict_keys(['name', 'age', 'phone'])



print(docment.pop('name')) #output-{'age': 20, 'phone': 1234}
print(docment)

docment.popitem()   #it pops the end item
print(docment)

docment.setdefault('name') #out put_{'age': 20, 'name': None}
print(docment)

docment.setdefault('age') #output_{'age': 20, 'name': None}
print(docment)

docment.values()   # it displays the dict values_ dict_values([20, None])
print(docment.values())





