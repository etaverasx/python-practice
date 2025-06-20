import random
import string

print("Hello from inside test.py!")

name = input("Who are you? ")

if name.strip() == "Emmanuel":
    print("Access granted")
    print(f"Welcome back, {name}!")

    action = input("How can I help you today? ")

    # Log the request to a file
    with open("requests.log", "a") as log_file:
        log_file.write(f"{name} requested: {action}\n")

    if action.strip().lower() == "password change":
        characters = string.ascii_letters + string.digits + string.punctuation
        new_password = ''.join(random.choice(characters) for _ in range(12))
        print(f"Your new password is: {new_password}")
    else:
        print(f"Got it, {name}. I will help you with: {action}")

else:
    print(f"Nice to meet you, {name}!")
    print("Access denied.")
