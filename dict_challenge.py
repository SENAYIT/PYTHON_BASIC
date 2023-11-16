
#challenge
# asks the phone the print each no. in word 
 # example. input 1234 #output -- one two three four 


phone= input ("phone: ")  

dict_of_num ={
    '0':'zero',
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine'
}

print(len(dict_of_num))


for num in phone:#1 2 
    for i in range(len(dict_of_num)): # 
        if int(num)==i:
           dict_of_num[num]
    print(dict_of_num[num]) 

#or 
for num in phone:#1 2 
    print(dict_of_num[num])   

#from teacher

output=" "
for num in phone:#1 2 
    output +=dict_of_num[num] + " "
print(output)    
        
  


