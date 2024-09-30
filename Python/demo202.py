import random

def third_largest(numbers):
    if len(numbers) < 3:
        return None

    first = second = third = float('-inf')

    for number in numbers:
        if number > first:
            third = second
            second = first
            first = number
        elif number > second and number != first:
            third = second
            second = number
        elif number > third and number != second and number != first:
            third = number

    return third if third != float('-inf') else None

# Example usage
# numbers = [12, 45, 23, 67, 45, 89, 23, 56]
numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

result = third_largest(numbers)

if result is not None:
    print("The third largest element is:", result)
else:
    print("There are not enough unique elements to find the third largest.")
