

#strings

course='python for beginners'
course1="python for beginners"
course3="python's for beginners"
course4='python for "beginners"'
course5="python for beginners"


print(course)
print(course1)
print(course3)
print(course4)
print(course5)

print(course[0]) # it print the start character -p
print(course[1]) # it print the 2nd character -y
print(course[-1]) # it print the end  character -s
print(course[-2]) # it print the start in end and the 2nd character r


print(course[0:]) # it print all upto end begin  from the start character  ??? 
print(course[1:]) # it print all upto end begin from the 2nd character  ???
print(course[:-1]) # it print all upto end begin from the start character 
print(course[:-2]) # it print all upto end 2nd begin from the start character

print(course[0:3]) # it print start begin upto 3rd(excluding 3rd)
print(course[2:5]) # it print start 012 @ 2 start upto 5th(excluding 3rd)
print(course[1:-1]) # it print start 01 @ 1 start upto -1th( end excluding 3rd)


another= course[:]

print("another is ",another)


