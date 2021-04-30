# Import random below:
import random_module

# Create random_list below:
random_list = []

# Create randomer_number below:
random_hundred = random_module.randint(1, 100)
random_list = [random_hundred for i in range(101)]
randomer_number = random_module.choice(random_list)

# Print randomer_number below:
print(randomer_number)
