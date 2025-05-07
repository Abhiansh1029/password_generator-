import random
import string
import pyperclip  # <-- new import

# Step 1: Ask user for password length
length = int(input("Enter the desired password length: "))

# Step 2: Ask what character types to include
use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Step 3: Build character pool
character_pool = ''
strength_score = 0

if use_upper:
    character_pool += string.ascii_uppercase
    strength_score += 1
if use_lower:
    character_pool += string.ascii_lowercase
    strength_score += 1
if use_digits:
    character_pool += string.digits
    strength_score += 1
if use_special:
    character_pool += string.punctuation
    strength_score += 1

# Step 4: Strength logic
if length < 6 or strength_score <= 1:
    strength = "Weak"
elif length < 10 or strength_score == 2:
    strength = "Medium"
else:
    strength = "Strong"

# Step 5: Generate and show password
if not character_pool:
    print("Error: You must select at least one character type!")
else:
    password = ''.join(random.choice(character_pool) for _ in range(length))
    print("\nGenerated Password:", password)
    print("Password Strength:", strength)

    # Copy to clipboard
    pyperclip.copy(password)
    print("✅ Password copied to clipboard!")
