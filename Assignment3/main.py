#we ask the user to input rows and columns
rows1 = int(input("Enter the number of rows: "))
columns1 = int(input("Enter the number of columns: "))
#We create an empty matrix to work with
matrix1 = []
rows2 = int(input("Enter the number of rows: "))
columns2 = int(input("Enter the number of columns: "))
matrix2 = []
def addMatrices():
    #first we ensure that the matrices are equal with this if statement
    if rows1 != rows2 or columns1 != columns2:
         print("Please run the program again and insert equal matrices")

    # We ask the user to enter the elements of the matrix and we iterate through the rows/columns then appending the
    # elements to the matrix
    for row in range(rows1):
        row_list = []
        for col in range(columns1):
            element = input("Enter element {} of row {}: ".format(col + 1, row + 1))
            row_list.append(element)
            matrix1.append(row_list)
    print(matrix1)

    for row in range(rows2):
        row_list = []
        for col in range(columns2):
            element = input("Enter element {} of row {}: ".format(col + 1, row + 1))
            row_list.append(element)
            matrix2.append(row_list)
    print(matrix2)


addMatrices()