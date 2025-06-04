import random

random_number = random.randint(0, 1)

# Heads and Tails
# if (random_number == 0):
#    print('Heads')
# else:
#    print('Tails')


# who will pay the bill
friends = ["Alice", "Bob", "Charlie", 'David', "Emanuel"]

# print(friends[random.randint(0, 4)])
print(random.choice(friends))