# Perfect Number Checker
This repository contains a simple Python script to check whether a given number is a perfect number.

## What is a Perfect Number?
A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. For example, the first perfect number is 6, because 1, 2, and 3 are its divisors, and 1 + 2 + 3 = 6.

## Script Overview
The script reads an integer input from the user and checks if it is a perfect number. If the sum of its proper divisors equals the number itself, it prints "Perfect Number"; otherwise, it prints "Not a Perfect Number".

Clone the repository:
```bash
git clone https://github.com/SyedAejazAhmed/python.git
cd Perfect Number
```
## Code Explanation 

1. **Input the Number:**
    ```python
    n = int(input("NO:"))
    ```
    - Prompts the user to input a number.
    - Converts the input string to an integer and stores it in the variable `n`.

2. **Initialize the Sum:**
    ```python
    sum = 0
    ```
    - Initializes a variable `sum` to 0. This will store the sum of the proper divisors of `n`.

3. **Find Divisors and Calculate Sum:**
    ```python
    for i in range(1, n):
        if n % i == 0:
            sum += i
    ```
    - Loops through all numbers from 1 to `n-1`.
    - Checks if `i` is a divisor of `n` using the modulo operator `%`.
    - If `i` is a divisor, it adds `i` to `sum`.

4. **Check if the Number is Perfect:**
    ```python
    if sum == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")
    ```
    - After the loop, checks if `sum` is equal to `n`.
    - If they are equal, prints "Perfect Number".
    - Otherwise, prints "Not a Perfect Number".

## Contributing
If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
