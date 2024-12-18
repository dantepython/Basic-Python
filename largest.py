#This problem focuses on finding the largest number in a list of numbers. It's a fundamental task in programming and helps practice basic list manipulation and comparison operations.
def find_largest(numbers):
    """Finds the largest number in a list.

    Args:
        numbers: A list of numbers.

    Returns:
        The largest number in the list, or None if the list is empty.
    """
    if not numbers:
        return None  # Handle empty list case

    largest = numbers[0]  # Initialize largest to the first element

    for number in numbers:
        if number > largest:
            largest = number

    return largest


# Example usage:
numbers = [10, 5, 25, 15, 30]
largest_number = find_largest(numbers)

if largest_number is not None:
    print("The largest number is:", largest_number)
else:
    print("The list is empty.")


# Additional test cases:
print(find_largest([1, 2, 3, 4, 5]))  # Output: 5
print(find_largest([-1, -2, -3]))  # Output: -1
print(find_largest([])) # Output: The list is empty.
print(find_largest([5, 5, 5]))  # Output: 5
print(find_largest([3, 1, 4, 1, 5, 9, 2, 6])) # Output: 9

