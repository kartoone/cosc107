# Starter program: loop practice
# Goal: Add up all numbers, find min, max, and average

numbers = [8, 3, 12, 5, 7]

# Initialize variables
total = 0
minimum = numbers[0]
maximum = numbers[0]

# ------------------------------
# TODO: Write a loop that:
# 1. Adds each number to total
# 2. Updates minimum if needed
# 3. Updates maximum if needed
# ------------------------------

for num in numbers:
    total = total + num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

# Calculate average
average = total / len(numbers)

# Output results
print("Numbers:", numbers)
print("Sum:", total)
print("Min:", minimum)
print("Max:", maximum)
print("Average:", average)
