# Create lower triangular, upper triangular and pyramid containing the "*" character.
def lower_triangular(rows):

    print("Lower Triangular:")
    for i in range(1, rows + 1):
        print("*" * i)

def upper_triangular(rows):

    print("\nUpper Triangular:")
    for i in range(rows, 0, -1):
        print("*" * i)

def pyramid(rows):

    print("\nPyramid:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


try:
    num_rows = int(input("Enter the number of rows for the patterns: "))
    if num_rows <= 0:
        print("Please enter a positive integer for the number of rows.")
    else:
        lower_triangular(num_rows)
        upper_triangular(num_rows)
        pyramid(num_rows)
except ValueError:
    print("Invalid input. Please enter an integer.")