
#list methods

num=[2,3,6,0,9,7,8]

print (10 in num)   # to check if it is 10 alive 

num.append(5) # to add value at end
print(num)

num.insert(0, 9)  # to insert the element @wanted place
print(num)

num.remove(6) # to delete the value
print(num)

num.pop()  # it will remove the end value from the list 
print(num)

print(num.index(3)) # to know index of value if the value exit it shows error

print(num.count(9)) # to count the no.of reapeted in one value

num.sort() # ascending order
print(num)

num.reverse() # for descending order 
print(num)


num2=num.copy()
num.append(1) # the num2 is not affected even if the num is change when the copy is first done

print(num2)



num.clear()
print(num)



###practice for other methods

n=[3,5,6]
n.extend("3") # to add the string
print(n)

stt=['abcd']
stt.append('2') # it also works when it replce with extend 
print(stt)







