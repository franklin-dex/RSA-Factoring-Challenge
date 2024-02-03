#!/usr/bin/python3

import sys
from math import gcd

def pollard_rho(n):
    x, y, d = 2, 2, 1
    while d == 1:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        d = gcd(abs(x - y), n)
    return d

def main():
    if len(sys.argv) != 2:
        print("Usage: python rsa_factors.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n <= 1:
            print("Please provide a positive integer greater than 1.")
            sys.exit(1)

        factor1 = pollard_rho(n)
        factor2 = n // factor1

        print(f"{n} = {factor1} * {factor2}")

    except ValueError:
        print("Invalid input. Please provide a valid positive integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
