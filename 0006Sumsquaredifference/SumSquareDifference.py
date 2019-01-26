# Do this to import mathidentities
import sys
sys.path.append("..") # Adds higher directory to python modules path.

# My modules
from myMath import int_sum_identity, int_squared_sum_identity

def problem6_solution():
    return int_sum_identity(100)**2 - int_squared_sum_identity(100)

if __name__ == "__main__":
    print(problem6_solution())
    input("Press Enter to continue...")
