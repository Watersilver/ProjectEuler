# Do this to import mathidentities
import sys
sys.path.append("..") # Adds higher directory to python modules path.

# Built in modules
from math import floor
# My modules
from myMath import is_divisible

# Every even-digit palindrome number is divisible by 11
def problem4_solution():
    a = 9
    b = 9
    c = 9
    while True:
        k = a * 100000 + b * 10000 + c * 1000 + c * 100 + b * 10 + a
        kdiv11 = k / 11
        # We assume that the number has six digits (not five)
        # 10 * 11 == 110 and 11 * 91 == 1001
        for i in range(10, 91):
            if is_divisible(kdiv11, i):
                if floor((kdiv11 / i) / 1000) == 0:
                    return k
        c -= 1
        if c < 0:
            c = 9
            b -= 1
            if b < 0:
                b = 9
                a -=1
                if a <= 0:
                    return "poulos"

if __name__ == "__main__":
    # print(problem4_solution())
    print(problem4_solution())
    input("Press Enter to continue...")
