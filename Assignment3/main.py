


#we ask the user to input rows and columns
rows1 = int(input("Enter the number of rows: "))
columns1 = int(input("Enter the number of columns: "))
#We create an empty matrix to work with
matrix1 = []
rows2 = int(input("Enter the number of rows: "))
columns2 = int(input("Enter the number of columns: "))
matrix2 = []
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

def addMatrices():
    #first we ensure that the matrices are equal with this if statement
    if rows1 != rows2 or columns1 != columns2:
        print("Please run the program again and insert equal matrices")
        exit()
    #Create an empty list to store the result matrix
    matrix3 = []
    # Iterate over the rows of matrix1 and create a new row in matrix3 for each row. Then iterate over the columns of
    # the row
    # Then for each column , the function adds elements of matrix1 and matrix2 and stores the result in matrix3
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix3.append(row)
    return matrix3

# matrix3 = addMatrices(matrix1,matrix2)
# print(matrix3)

def checkRotation(matrix1,matrix2):
    for i in range(len(matrix1[0])):
        for j in range(len(matrix1)):
            if matrix1[i][j] != matrix2[j][i]:
                return False
    return True
if checkRotation(matrix1,matrix2) :
     print("The first matrix is the rotation of the second matrix.")
else:
    print("The first matrix is not the rotation of the second matrix.")

print(checkRotation(matrix1,matrix2))

def invertDictionary():
    pass

def convertMatrixToDictionary():
    pass


def isPalindrome(s):
    pass


def searchAndmergeSort():
    pass


def main():
    while True:
        print("\nMenu:")
        print("1. Add Matrices")
        print("2. Check Rotation")
        print("3. Invert Dictionary")
        print("4. Convert Matrix to Dictionary")
        print("5. Check Palindrome")
        print("6. Search for an Element & Merge Sort")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            addMatrices()
        elif choice == "2":
            checkRotation()
        elif choice == "3":
            invertDictionary()
        elif choice == "4":
            convertMatrixToDictionary()
        elif choice == "5":
            string_input = input("Enter a string: ")
            result = isPalindrome(string_input)
            print(f'The string "{string_input}" is {"a palindrome" if result else "not a palindrome"}.')
        elif choice == "6":
            searchAndmergeSort()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


main()
