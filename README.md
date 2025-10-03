# comp163-assignment-5 - Loop Mastery

# Overview
This assignment demonstrates mastery of loops in Python through three challenges:
1. Collatz sequence generator (while loop)
2. Prime number checker (for loop)
3. Multiplication table grid (nested loops)

# Challenge 1: Collatz Sequence
- **Problem:** Generate the Collatz sequence for a given positive integer and count the steps until it reaches 1.
- **Loop Choice:** **While loop**  
  - Reason: The number of iterations is unknown beforehand. The loop continues until `current_number` equals 1.
- **How it works:**  
  - Start with user input `current_number`  
  - If the number is even, divide by 2; if odd, multiply by 3 and add 1  
  - Print the sequence on the same line and count steps  

# Challenge 2: Prime Number Checker
- **Problem:** Determine if a positive integer greater than 1 is prime by checking all possible divisors.
- **Loop Choice:** **For loop**  
  - Reason: We know the exact range of numbers to test (`2` to `n-1`). A for loop iterates over this known range efficiently.
- **How it works:**  
  - Loop through possible divisors  
  - If any number divides evenly, the number is not prime  
  - Otherwise, it is prime  
  - Prints testing process for clarity  

# Challenge 3: Multiplication Table Grid
- **Problem:** Print a formatted 10×10 multiplication table with headers for rows and columns.
- **Loop Choice:** **Nested loops**  
  - Reason: Each row contains multiple columns. The outer loop iterates over rows, the inner loop iterates over columns.
- **How it works:**  
  - Print header row (column numbers)  
  - For each row, print row number (header column)  
  - Inner loop calculates and prints each product in that row, properly aligned  

# AI Assistance
- Used AI to clarify loop concepts and debug syntax errors  
- Core algorithms were written and understood by the student  
