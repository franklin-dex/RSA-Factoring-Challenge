#!/usr/bin/python3
import sys

def factorize(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            for line in file:
                num = int(line.strip())
                factors = factorize(num)
                print(f"{num} = {' * '.join(map(str, factors))}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
