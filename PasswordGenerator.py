import random
import string

print("Your random password is:")

# Define character sets for lowercase, uppercase, digits, and symbols
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
digits = string.digits
symbols = '+_)(*&^%$#@!'
password = ""

# Ensure at least 3 uppercase characters
uppercase_count = 0
while uppercase_count < 2:
    password += random.choice(uppercase_chars)
    uppercase_count += 1

# Ensure only 2 symbols
symbol_count = 0
while symbol_count < 2:
    password += random.choice(symbols)
    symbol_count += 1

# Fill the remaining characters with a mix of lowercase, digits, and symbols
remaining_length = 16 - (uppercase_count + symbol_count)
for i in range(remaining_length):
    password += random.choice(lowercase_chars)

# shuffle the password
password_list = list(password)
random.shuffle(password_list)

print(*password_list)
