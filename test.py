print("Hello from inside test.py!")

name = input("Who are you? ")

if name.strip() == "Emmanuel":
    print("Access granted")
    print(f"Welcome back, {name}!")
    action = input("How can I help you today? ")
    print(f"Got it, {name}. I will help you with: {action}")
else:
    print(f"Nice to meet you, {name}!")
    print("Access denied.")
