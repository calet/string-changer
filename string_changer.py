import string
import random

alphabet = string.ascii_letters

numbers = string.digits

choice = [alphabet, numbers]

random_choice = random.choice(choice)

specific = random.choice(random_choice)

my_message = "hello world, how are you?"

index = random.randint(0, len(my_message))

new_message = list(my_message[:])
new_message[index] = specific

print(''.join(new_message))

