# A basic code for matrix input from user

R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

R1 = int(input("Enter the number of rows: "))
C1 = int(input("Enter the number of columns: "))

# Initialize matrix
matrix1 = []
print("Enter the entries rowwise:")

# For user input
for i in range(R1):  # A for loop for row entries
    a1 = []
    for j in range(C1):  # A for loop for column entries
        a1.append(int(input()))
    matrix1.append(a1)

# For printing the matrix
for i in range(R1):
    for j in range(C1):
        print(matrix1[i][j], end=" ")
    print()

result = [[0 for i in range(C)] for i in range(R)]
# iterate through rows
for i in range(R):
    # iterate through columns
    for j in range(C):
        result[i][j] = matrix[i][j] + matrix1[i][j]

print("Resultant Matrix is:")
for i in range(R):
    for j in range(C):
        print(result[i][j], end=" ")
    print()
