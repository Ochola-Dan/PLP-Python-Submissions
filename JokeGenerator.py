import random

def joke_generator():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🪲",
        "Why was the JavaScript developer sad? Because he didn't 'null' his problems. 😢",
        "Why do Python developers wear glasses? Because they can’t C. 👓",
        "How many programmers does it take to change a light bulb? None, it's a hardware problem! 💡"
    ]

    print(random.choice(jokes))

# Generate a joke
joke_generator()
