import random
# Letters
lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letters = lowercase_letters + uppercase_letters
# Numbers
digits = list("0123456789")

# Special characters (common set used in passwords)
special_characters = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\")

print("Welcome to the password generator!")
nr_letters = int(input("How many number of letters would you like to include in your password?\n"))
nr_spec_chars = int(input("How many number of special characters would you like to include in your password?\n"))
nr_numbers = int(input("How many numbers would you like to include in your password?\n"))

password = ""

letters_in_pass = random.sample(letters, k=nr_letters)
numbers_in_pass = random.sample(digits, k=nr_numbers)
spec_char_in_pass = random.sample(special_characters,k=nr_spec_chars)

final_list = letters_in_pass + numbers_in_pass + spec_char_in_pass
random.shuffle(final_list)
for i in final_list:
    password += i
print(password)
