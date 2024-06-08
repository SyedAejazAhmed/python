# Prime Number Checker
This repository contains a simple Python script that checks whether a given number is prime or not. The script prompts the user to enter a number and then determines if the number is prime by checking its divisibility by integers up to half of the number.

## How to use
### Clone the Repository
```bash
git clone https://github.com/SyedAejazAhmed/python.git
cd PrimeNumber
```

### Run the Script
```bash
python prime.py
```

## How it Works
### The script follows these steps:

1. Input: Prompts the user to enter a number.
2. Initialization:
    -Calculates half of the entered number (`m = int(n/2)`).
    -Initializes a flag variable (`f = 0`) to track whether a divisor is found.
3. Loop: Iterates through all numbers from 2 to `m `(exclusive) and checks if any of these numbers divide the input number `n` without leaving a remainder.
4. Check Divisibility:
    -If a divisor is found (`n % i == 0`), it prints "Not a prime Number" and sets the flag `f` to 1, then breaks out of the loop.
    -If no divisor is found after the loop completes, it prints "prime Number".

## Contribution
Feel free to contribute to this repository by submitting issues or pull requests. Contributions are always welcome.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


