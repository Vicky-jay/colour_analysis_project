#NAME : Chukwudi Victor Ebubechukwu
#Which colour of the shirt is the mean colour ?
#Question 1
"""To calculate the mean color, you can first assign each color a numerical value, such as the
frequency of that color occurring throughout the week,and then find the mean (average)
of those frequencies."""
# List of all colors that appeared throughout the week
colours = [
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", 
    "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", # Monday
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", 
    "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUE", # Tuesday
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", 
    "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE", # Wednesday
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", 
    "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN", # Thursday
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", 
    "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"  # Friday
]

# Count the frequency of each color
from collections import Counter

colour_counts = Counter(colours)

# Calculate the mean (average) of the frequencies
total_colours = sum(colour_counts.values())
mean_frequency = total_colours / len(colour_counts)

# Find the colour(s) with the frequency closest to the mean
mean_colour = min(colour_counts, key=lambda x: abs(colour_counts[x] - mean_frequency))

print(f"The mean colour is =  {mean_colour}")

#Question 2  > Most worn colour (mode)
from collections import Counter

# Colour data from the table
colours = [
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 
    'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 
    'BLUE', 'BLUE', 'GREEN', # Monday
    'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 
    'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 
    'BLUE', 'BLUE', 'BLUE', # Tuesday
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 
    'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 
    'BLUE', 'WHITE', 'WHITE', # Wednesday
    'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 
    'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 
    'BLUE', 'BLUE', 'GREEN', # Thursday
    'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 
    'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 
    'BLUE', 'BLUE', 'WHITE'  # Friday
]

# Calculate frequencies
colour_counts = Counter(colours)
most_worn_colour = colour_counts.most_common(1)[0]


print(f"The most worn color is = {most_worn_colour}")

#Question 3 > Median colour
#The median is the middle value in an oredered list .
# Step 1: Count the frequency of each color
from collections import Counter

colors = [
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW',
    'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE',
    'BLUE', 'BLUE', 'GREEN', # Monday
    'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK',
    'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE',
    'BLUE', 'BLUE', 'BLUE', # Tuesday
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW',
    'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE',
    'BLUE', 'WHITE', 'WHITE', # Wednesday
    'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW',
    'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE',
    'BLUE', 'BLUE', 'GREEN', # Thursday
    'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE',
    'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE',
    'BLUE', 'BLUE', 'WHITE'  # Friday
]

# Step 2: Count occurrences of each color
colour_counts = Counter(colors)

# Step 3: Sort colors by frequency
sorted_colours = sorted(colour_counts.items(), key=lambda x: x[1])

# Step 4: Find the median color
middle_index = len(sorted_colours) // 2
median_colour = sorted_colours[middle_index]

print(f"The median color is = {median_colour}")

#Question 4
"""Variance tells us how much the frequencies of colours spread out from the mean (average frequency).
If the variance is small, it means the frequencies are close to the mean.
If the variance is large, the frequencies are more spread out."""
import statistics

# Step 1: Extract frequencies from the dictionary
frequencies = list(colour_counts.values())

# Step 2: Calculate variance
variance = statistics.variance(frequencies)

# Step 3: Print variance rounded to 2 decimals
print(f"The variance of colours is = {round(variance, 2)}")
#Question 5 > probability of red
# Step 1: Calculate the total number of colours
total_colours = sum(colour_counts.values())

# Step 2: Get the frequency of 'RED' (default to 0 if not found)
red_frequency = colour_counts.get('RED', 0)

# Step 3: Calculate the probability of 'RED'
red_probability = red_frequency / total_colours

# Step 4: Print the rounded probability
print(f"The probability of red is = {round(red_probability, 2)}")

#Question 6 > save to sql
#question 7> using recursive search
def recursive_search(arr, target, index=0):
    """
    Recursive function to search for a number in a list.
    Parameters:
        arr: list of numbers
        target: the number to search for
        index: current position in the list (default is 0)
    Returns:
        Index of the target if found, otherwise -1.
    """
    if index == len(arr):  # Base case: reached the end of the list
        return -1
    if arr[index] == target:  # Found the target number
        return index
    return recursive_search(arr, target, index + 1)  # Recursive call for the next index

# Example usage
numbers = [4, 2, 9, 7, 1, 3]  # List of numbers to search
target = int(input("Enter a number to search: "))  # Ask the user for the target number
result = recursive_search(numbers, target)  # Call the recursive search function

# Display the result
if result != -1:
    print(f"The number {target} is found at index {result}.")
else:
    print(f"The number {target} is not in the list.")    
#Question 8 > binary to base ten
#Question 9 > fibonacci sum 
def fibonacci_sum(n):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers (0 and 1)
    total = a     # Start the total sum with the first Fibonacci number, which is 0
    for _ in range(n - 1):  # Loop for the next (n-1) Fibonacci numbers
        a, b = b, a + b    # Update 'a' to 'b' and 'b' to the sum of 'a' and 'b' (the next Fibonacci number)
        total += a         # Add the new 'a' (current Fibonacci number) to the total sum
    return total  # Return the total sum after the loop

# Sum of first 50 Fibonacci numbers
print("Sum of first 50 Fibonacci numbers:", fibonacci_sum(50))


