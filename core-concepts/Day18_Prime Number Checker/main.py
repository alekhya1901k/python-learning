def is_prime(num):
    # numbers less than or equal to 1 are not prime
    if num <= 1:
        return False

    # check divisors from 2 up to square root of num
    for i in range(2, int(num ** 0.5) + 1):
        # if num is divisible by i, it is not prime
        if num % i == 0:
            return False

    # if no divisors found, it is prime
    return True
n = int(input("Enter a number: "))
print(is_prime(n))




