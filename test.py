import random
import string

print("Hello from inside test.py!")

name = input("Who are you? ")

if name.strip() == "Emmanuel":
    print("Access granted")
    print(f"Welcome back, {name}!")
    action = input("How can I help you today? ")

    # Make the action lowercase for easy comparison
    if action.strip().lower() == "password change":
        # Generate a random password (e.g., 12 characters)
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(12))
        print(f"Your new password is: {new_password}")
    else:
        print(f"Got it, {name}. I will help you with: {action}")

else:
    print(f"Nice to meet you, {name}!")
    print("Access denied.")
