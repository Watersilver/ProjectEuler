# Do this to import mathidentities
import sys
sys.path.append("..") # Adds higher directory to python modules path.

# My modules
from myMath import is_prime

def problem7_solution():
    num = 1
    prime_nums = 0
    while True:
        num += 1
        if is_prime(num):
            prime_nums += 1
            print(prime_nums)
        if prime_nums == 10001:
            return num

if __name__ == "__main__":
    print(problem7_solution())
    input("Press Enter to continue...")
