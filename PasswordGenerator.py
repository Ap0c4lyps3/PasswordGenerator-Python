import random
import string

print("Your random password is:")

# Define character sets for lowercase, uppercase, digits, and symbols
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase
digits = string.digits
symbols = '+_)(*&^%$#@!'

# Ensure at least 3 uppercase characters
uppercase_count = 0
password = ""
while uppercase_count < 3:
    password += random.choice(uppercase_chars)
    uppercase_count += 1

# Ensure only 2 symbols
symbol_count = 0
while symbol_count < 2:
    password += random.choice(symbols)
    symbol_count += 1

# Fill the remaining characters with a mix of lowercase, digits, and symbols
remaining_length = 16 - (uppercase_count + symbol_count)
for _ in range(remaining_length):
    password += random.choice(lowercase_chars + digits + symbols)

# Shuffle the password characters to make it more random
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(password)
