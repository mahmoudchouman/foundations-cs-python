def initializeMatrix(rows, cols, matrix_name):    #O(n^2) | nested loops
    #initialize an empty matrix
    matrix = []
    #Loop through the rows and columns to get the elements values from the user
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i + 1}, {j + 1}) for {matrix_name}: "))
            row.append(element)
        matrix.append(row)
    return matrix

def addMatrices(): #O(N^2) | Nested loop and for loop O(n)
    #Get matrix rows and columns as input
    rows1 = int(input("Please enter number of rows for matrix 1: "))
    cols1 = int(input("Please enter number of columns for matrix 1: "))
    rows2 = int(input("Please enter number of rows for matrix 2 : "))
    cols2 = int(input("Please enter number of columns for matrix 2: "))

    #we ensure the matrices are of equal dimensions
    if rows1 != rows2 or cols1 != cols2:
        print("Matrices should be of same size")
        return

    #create the 2 matrices using the initialize function we did before
    matrix1 = initializeMatrix(rows1,cols1,"matrix1")
    matrix2 = initializeMatrix(rows2,cols2,"matrix2")

    # create an empty matrix in which the matrices will be  added , using thefor loop below
    matrix3 = []

    for i in range(rows1):
        row = []
        for j in range(cols1):
            result_element = matrix1[i][j] + matrix2[i][j]
            row.append(result_element)
        matrix3.append(row)


    print("Matrix 3 is equal to : ")
    for row in matrix3:
        print(row)

def checkRotation():
    rows1 = int(input("Please enter number of rows for matrix 1: "))
    cols1 = int(input("Please enter number of columns for matrix 1: "))
    rows2 = int(input("Please enter number of rows for matrix 2 : "))
    cols2 = int(input("Please enter number of columns for matrix 2: "))

    matrix1 = initializeMatrix(rows1, cols1, "matrix1")
    matrix2 = initializeMatrix(rows2, cols2, "matrix2")

    # We loop through matrix 1 "elements" (rows and columns)
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            # We check if matrix 1 is the rotation of matrix 2 by using an if statement and reversing the indices
            if matrix1[i][j] != matrix2[j][i]:
                return False

    return True

def invertDictionary():
    # acquiring the number of items in the dictionary from the user and then creating 2 empty dictionaries (the original
    # and the inverted)
    number_of_items = int(input("enter the number of items in the dictionary: "))
    original = {}
    inverted = {}
    #looping in number of items and asking the user to input keys and variables in the original dictionary
    for _ in range(number_of_items):
        key = input("please enter key : ")
        value = input("please enter value : ")
        original[key] = value

        if value in inverted:
            # If it is, append the key to the list of values for that key
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            # If it is not, create a new list or a single value with the key as the only element
            inverted[value] = key

    print("\noriginal:")
    print(original)
    print("\ninverted:")
    print(inverted)



def convertMatrixToDictionary():
    num_users = int(input("Enter the number of users: "))

    # Make an empty matrix
    user_matrix = []

    # fill up the matrix with user input
    for _ in range(num_users):
        user_data = [
            input("Enter First Name: "),
            input("Enter Last Name: "),
            input("Enter ID: "),
            input("Enter Job Title: "),
            input("Enter Company: "), ]

        user_matrix.append(user_data)

    # Display the original matrix
    print("\nOriginal Matrix:")
    for user_data in user_matrix:
        print(user_data)

    # Convert the matrix to a dictionary
    user_dict = {}
    for user_data in user_matrix:
        user_id = user_data[2]  # Knowing ID is always at index 2
        user_info = user_data[:2] + user_data[3:]  # Exclude ID from user_info
        user_dict[user_id] = user_info

    # Display the converted dictionary
    print("\nConverted Dictionary:")
    print(user_dict)


def isPalindrome(s):
    # Base case: if the string has 0 or 1 characters, it's a palindrome
    if len(s) <= 1:
        return True

    # Recursive case: check if the first and last characters are the same
    if s[0] == s[-1]:
        # If they are, recursively check the substring without the first and last characters
        return isPalindrome(s[1:-1])
    else:
        # If the first and last characters are not the same, it's not a palindrome
        return False



def searchAndmergeSort():
    def custom_merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            custom_merge_sort(left_half)
            custom_merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def search_and_merge_sort():
        # Get user input for list creation
        num_elements = int(input("Enter the number of elements in the list: "))

        # Initialize an empty list
        my_list = []

        # Populate the list with user input
        for _ in range(num_elements):
            element = int(input("Enter an element: "))
            my_list.append(element)

        # Display the original list
        print("\nOriginal List:")
        print(my_list)

        # Get user input for element to search
        search_element = int(input("Enter the element to search: "))

        # Search for the element
        if search_element in my_list:
            index = my_list.index(search_element)
            print(f"Element found at index: {index}")

            # Sort the list using merge sort
            custom_merge_sort(my_list)

            # Display the sorted list
            print("Sorted List:")
            print(my_list)

        else:
            print(f"Element {search_element} not found in the list.")


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
            if checkRotation():
                print("The first matrix is the rotation of the second matrix.")
            else:
                print("The first matrix is not the rotation of the second matrix.")
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
