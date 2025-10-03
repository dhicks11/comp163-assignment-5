print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: "))
step_count = 0

print("Sequence:", current_number, end=" ")

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = 3 * current_number + 1

    print(current_number, end=" ")
    step_count += 1  # counts steps

print("\nSteps:", step_count)


print("\n=== Challenge 2: Prime Number Checker ===")
n = int(input("Enter a number: "))

print(f"Testing divisors from 2 to {n-1}...")

is_prime = True

for divisor in range(2, n):
    if n % divisor == 0:
        print(f"{n} is not prime (divisible by {divisor})")
        is_prime = False
        break

if is_prime:
    print(f"{n} is prime!")

print("\n=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")


print("   ", end="")  
for col in range(1, 11):
    print(f"{col:4}", end="")
print()  # move to next line


for row in range(1, 11):
    print(f"{row:2} ", end="")  
    for col in range(1, 11): #nested loop
        product = row * col
        print(f"{product:4}", end="")
    print()
