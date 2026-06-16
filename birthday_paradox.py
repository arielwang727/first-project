import random

people = 23 

birthdays = []

for i in range(people):
  birthday = random.randint(1,365)
  birthdays.append(birthday)

print(birthdays)
