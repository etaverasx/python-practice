print("Hello from inside test.py!")
name = input("Who are you? ")
if name.strip() == "Emmanuel":
    print("Access granted")
else:
    print(f"Nice to meet you, {name}!")
    print("Access denied.")
