# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ask user for range


limit = int(input("Enter a number:  "))

print(f"Prime numbers up to {limit}:")
for num in range(2, limit + 1):
    if is_prime(num):
        print(num, end=" ")
