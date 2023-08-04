import random

n = int (input ("enter number of numbers: "))
random_numbers = []

while (len(random_numbers)) < n:
    
    x = random.randint(0, 20)

    if x in random_numbers:
        random_numbers.remove(x)
        random_numbers.append(x)
    else:
        random_numbers.append(x)

print ("non-repeating random numbers are:")    
print (random_numbers)