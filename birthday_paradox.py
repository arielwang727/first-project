import random

people = 23
birthdays = [random.randint(1, 365) for _ in range(people)]

print(birthdays)
