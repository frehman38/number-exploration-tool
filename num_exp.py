def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Step 1: Greet the user and gather their favorite numbers
name = input("Enter your name: ")
print(f"Hello, {name}! Let's explore your favorite numbers.")

# Step 2: Ask for three favorite numbers
favorite_numbers = []
for i in range(1, 4):
    num = int(input(f"Enter your favorite number {i}: "))
    favorite_numbers.append(num)

# Step 3: Determine if the numbers are even or odd
even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in favorite_numbers]

# Step 4: Calculate the square of each number
squares = [(num, num ** 2) for num in favorite_numbers]

# Step 5: Print the information in an engaging format
print("\nLet's explore your numbers, {name}!\n")
for num, parity in even_odd_info:
    print(f"The number {num} is {parity}.")

print("\nNow let's look at the squares of your numbers:")
for num, square in squares:
    print(f"The square of {num} is {square}.")

# Step 6: Calculate the sum of the numbers
sum_of_numbers = sum(favorite_numbers)
print(f"\nThe sum of your favorite numbers is {sum_of_numbers}. Great job!")

# Step 7: Check if the sum is a prime number
if is_prime(sum_of_numbers):
    print(f"Wow, {sum_of_numbers} is a prime number!")
else:
    print(f"{sum_of_numbers} is not a prime number.")

print("\nThanks for playing with numbers, {name}! Hope you had fun!")
