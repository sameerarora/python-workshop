def fibonacci(lower_bound, upper_bound):
    prev, curr = 0, 1
    while prev + curr < upper_bound:
        prev, curr = curr, prev + curr
        if prev + curr >= lower_bound:
            yield prev + curr


f_generator = fibonacci(20, 1000)

# for i in f_generator:
#     print(i)

from math import sqrt


# 1, 3, 5 , 7 , 11, 13
def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime(lb, ub):
    for num in range(lb, ub):
        if is_prime(num):
            yield num


print(",".join([str(i) for i in generate_prime(1, 100)]))
