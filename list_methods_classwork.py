

#classwork
# write a program to remove the duplicate no. in a list 


num=[2,4,6,6,7,2,3,5,2,2,2]  # it works by mine

for value in num:
    if num.count(value)>=2:
        num.remove(value)
print(num)



# or in other 
print('from teach')

num=[2,4,6,6,7,2,3,5,2,2,2]
uniques=[]

for number in num:
    if number not in uniques: 
        uniques.append(number)   
print(uniques)
