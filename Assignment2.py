# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if len(numbers) < 2:
        return numbers[0], None  # Return the first element and None for the second maximum

    max_val = second_max_val = float('-inf')

    for num in numbers:
        if num > max_val:
            second_max_val = max_val
            max_val = num
        elif num > second_max_val and num != max_val:
            second_max_val = num

    if second_max_val == float('-inf'):
        return max_val, None  # Return None if there's no second maximum

    return max_val, second_max_val

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
     return sorted(set(numbers))
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    current_sum = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        result.append(current_sum)
    
    return result

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    if step <= 0:
        raise ValueError("Step must be a positive integer")
    
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The lists must have the same length")
    
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("The number of columns in A must be equal to the number of rows in B")

    # Get the dimensions of the result matrix
    result_rows = len(matrix1)
    result_cols = len(matrix2[0])

    # Initialize the result matrix with zeros
    result = [[0] * result_cols for _ in range(result_rows)]

    # Perform matrix multiplication
    for i in range(result_rows):
        for j in range(result_cols):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result