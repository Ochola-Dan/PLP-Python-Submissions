def greet_user():
    name = input("What's your name: ")
    color = input("What's your favorite color: ")

    if name and color:
        print(f"Hello {name}! Your favorite color, {color}, is awsome!.")
    else:
        print("Please provide your name and favorite color.")

greet_user()