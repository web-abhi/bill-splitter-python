# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x=len(names)
choose = random.randint(0, x-1)
person = names[choose] 
#Here we can also use person= random.choice(names) for getting the same result without using multiple code of lines.
print(person)


