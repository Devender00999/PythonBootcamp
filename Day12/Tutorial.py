# Scope is something that defines where a declared variable or function can be accessed.

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True