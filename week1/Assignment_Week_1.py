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
    number_of_rows = int(input("Enter the number of rows for the patterns: "))
    if number_of_rows <= 0:
        print("Please enter a positive integer for the number of rows.")
    else:
        lower_triangular(number_of_rows)
        upper_triangular(number_of_rows)
        pyramid(number_of_rows)
except ValueError:
    print("Invalid input.")
