# Scope is something that defines where a declared variable or function can be accessed.

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

enemies = 1

def increase_enemies():
    global enemies
    enemies = 10
    print(f'enemies inside function: {enemies}')
    
increase_enemies()
print(f'enemies outside function: {enemies}')
