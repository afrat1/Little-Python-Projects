#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

strr = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for i in range(nr_letters):
      random_number = random.randint(0, len(letters) - 1)
      strr = strr + letters[random_number-1]
  
for i in range(nr_symbols):
      random_number = random.randint(0, len(symbols) - 1)
      strr = strr + symbols[random_number]

for i in range(nr_numbers):
      random_number = random.randint(0, len(numbers) - 1)
      strr = strr + symbols[random_number-1]

print(strr)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

strr2 = ""

while nr_letters != 0 or nr_symbols != 0 or nr_numbers != 0:

    ranndum = random.randint(1,4)

    if ranndum == 1 and nr_letters > 0:
        random_number = random.randint(0, len(letters) - 1)
        strr2 = strr2 + letters[random_number-1]
        nr_letters += -1
            
    elif ranndum == 2 and nr_symbols > 0:
        random_number = random.randint(0, len(symbols) - 1)
        strr2 = strr2 + symbols[random_number]
        nr_symbols += -1

    elif ranndum == 3 and nr_numbers > 0:
        random_number = random.randint(0, len(numbers) - 1)
        strr2 = strr2 + symbols[random_number-1]
        nr_numbers += -1

print(strr2)
