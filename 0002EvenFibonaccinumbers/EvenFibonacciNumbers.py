def even_fibnacci_sum(max_value):
    fib1 = 0
    fib2 = 2
    sum = 2
    while True:
        fib3 = 4*fib2 + fib1
        if fib3 > max_value:
            break
        sum = sum + fib3
        fib1 = fib2
        fib2 = fib3
    return sum

if __name__ == "__main__":
    print(even_fibnacci_sum(4000000))
    input("Press Enter to continue...")
