# Do this to import mathidentities
import sys
sys.path.append("..") # Adds higher directory to python modules path.

# Built in modules
from math import floor
# My modules
from myMath import int_sum_identity, is_prime

def prime_divisors(num):
    for i in range(2, num+1):
        division = num/i
        if division == floor(division):
            if is_prime(division):
                return floor(division)

if __name__ == "__main__":
    print(prime_divisors(600851475143))
    input("Press Enter to continue...")
