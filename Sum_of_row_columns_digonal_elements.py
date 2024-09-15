R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

# Function to calculate sum of each row
def row_sum(matrix, R) :
    print("\nFinding Sum of each row:\n")
    # finding the row sum
    for i in range(R) :
        sum = 0
        for j in range(C) :
            # Add the element
            sum += matrix[i][j]
        # Print the row sum
        print("Sum of the row",i,"=",sum)

# Function to calculate sum of each column
def column_sum(matrix, R) :
    print("\nFinding Sum of each column:\n")
    # finding the column sum
    for i in range(C) :
        sum = 0
        for j in range(R) :
            # Add the element
            sum += matrix[j][i]
        # Print the column sum
        print("Sum of the column",i,"=",sum)

def printDiagonalSums(matrix, R):
    principal = 0
    secondary = 0
    for i in range(0, R):
        for j in range(0, R):
            # Condition for principal diagonal
            if (i == j):
                principal += matrix[i][j]
            # Condition for secondary diagonal
            if ((i + j) == (R - 1)):
                secondary += matrix[i][j]
    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)

row_sum(matrix, R)
column_sum(matrix, R)
printDiagonalSums(matrix, R)
