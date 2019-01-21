# Do this to import mathidentities
import sys
sys.path.append("..") # Adds higher directory to python modules path.

# Built in modules
from math import floor
# My modules
from mathidentities import int_sum_identity

def multiples_of_x_form_1_to_n(n, x):
    return floor(n / x)

def sum_of_all_the_multiples_of_x_or_y_below_z(x, y, z):
    max_num = z - 1
    num_of_mutiples_of_x = multiples_of_x_form_1_to_n(max_num , x)
    num_of_mutiples_of_y = multiples_of_x_form_1_to_n(max_num , y)
    num_of_mutiples_of_x_and_y = multiples_of_x_form_1_to_n(max_num , x * y)
    # Identity: [sum(k = 1, n)]k = (1 / 2) * n * (n + 1)
    # + Principle of Inclusion and Exclusion (PIE) =>
    # sumx + sumy - sumxandy = sum of all the multiples of x or y
    sumx = x * int_sum_identity(num_of_mutiples_of_x)
    sumy = y * int_sum_identity(num_of_mutiples_of_y)
    sumxandy = x * y * int_sum_identity(num_of_mutiples_of_x_and_y)
    return sumx + sumy - sumxandy

def sum_of_all_the_multiples_of_3_or_5(below_me):
    return sum_of_all_the_multiples_of_x_or_y_below_z(3, 5, below_me)

def sum_of_all_the_multiples_of_3_or_5_below_1000():
    return sum_of_all_the_multiples_of_3_or_5(1000)

if __name__ == "__main__":
    print(sum_of_all_the_multiples_of_3_or_5_below_1000())
    input("Press Enter to continue...")
