import random

BANNER = '''
                     /.\
                 (_.--'  |
                  |  ==  |
             o-._ .--..--. _.-o
                 |   ||   |
                  ;--|`--:
                  |. |   |
                  |  ;_ .|
                  |_____ |
                 /|     '|\
                 //`----'\\
                ////|  |  \\
                /   |  |    \
                   /|  |\
                  / \  / \
                 /   \/   \
                /          \
                |          |
               ||    /\    ||
               ||   ,  .   || 

'''

# Data:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(BANNER)
print("Welcome to the PyPassword Generator!")

# User Inputs 
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

random_selected_letters = random.choices(letters, k=nr_letters)
random_selected_symbols = random.choices(numbers, k=nr_symbols)
random_selected_numbers = random.choices(symbols, k=nr_numbers)

# print(random_selected_letters)
# print(random_selected_symbols)
# print(random_selected_numbers)

# Combine all the lists and extend the password list:
password.extend(random_selected_letters + random_selected_symbols + random_selected_numbers)
# print(password)

# Shuffling the random password 
random.shuffle(password)
print(password)
print(f"final chosen password is {''.join(password)}")
