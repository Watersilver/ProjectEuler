from math import sqrt, floor

def int_sum_identity(n):
    return int((1.0 / 2.0) * n * (n + 1))

def int_squared_sum_identity(n):
    return int((n * (n + 1) * (2 * n + 1)) / 6)

def is_prime(num):
    sqrnum = floor(sqrt(num))
    num_is_prime = True
    for i in range(2, sqrnum+1):
        quotient = num/i
        if quotient == floor(quotient):
            num_is_prime = False
            break
    return num_is_prime

def is_divisible(divor, divee):
    division = divor / divee
    return division == floor(division)
