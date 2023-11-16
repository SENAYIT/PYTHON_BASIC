
#list
#classwork_ write aprogram to find a largest no. in list 

numbers=[4,8,0,12,5,67]

print(numbers)
print("the length of numers is: ", len(numbers))

largest=numbers[0] # never change below of the for loop write

for i in range(len(numbers)):

    if largest<numbers[i]:
        largest=numbers[i]

    else:
       largest=largest

    #print(f"the largest in numbers list is: {largest}") # @this compare and write the largest for each index 
print(f"the largest in numbers list is: {largest}")





#or in simple &correction
print('   correction by him is ')
numbers=[4,8,0,12,5,67]

print(numbers)

largest=numbers[0]
for number in numbers:
    if number> largest:
        largest =number
print("the largest is:", largest)