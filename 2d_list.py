

#2d list

matrix=[
    [1,2,3],
    [6,7,6],
    [1,3,2]
]

print(matrix)

print(matrix[0][2])
print(matrix[0][0])


for row in matrix:  # to list the all element of matrix it is used
    for item in row:
        print(item)