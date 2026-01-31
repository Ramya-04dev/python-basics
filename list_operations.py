# List Operations Program

numbers = []

n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nList:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
