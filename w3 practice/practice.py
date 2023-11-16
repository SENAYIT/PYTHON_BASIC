mylist = ["a", "b", "a", "c", "c"]
for x in mylist:
    y = mylist.count(x)
    if y > 1:
        mylist.remove(x)
print(mylist) 

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)