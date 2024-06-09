# Get the dimensions of the matrix from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize the matrices with zeros
X = []
Y = []
result = [[0 for _ in range(cols)] for _ in range(rows)]

print("Enter the elements of matrix X:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element X[{i}][{j}]: "))
        row.append(element)
    X.append(row)

print("Enter the elements of matrix Y:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element Y[{i}][{j}]: "))
        row.append(element)
    Y.append(row)

# Perform matrix addition
for i in range(rows):
    for j in range(cols):
        result[i][j] = X[i][j] + Y[i][j]

# Print the result
print("Resultant matrix after addition:")
for r in result:
    print(r)
