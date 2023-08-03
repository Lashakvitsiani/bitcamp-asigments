import random

def first_version() -> None:
    
    name = input("What is your name? ")


    output = "Hello, " + name + ", nice to meet you"

  
    print(output)

def without_variable() -> None:
  
    print("Hello,", input("What is your name? "), "nice to meet you!")

def second_version() -> None:
    name = input("What is your name? ")

    greetings = [
        f"Hello, {name}. Nice to meet you",
        f"Greetings, {name}.",
        f"Nice to see you {name}.",
        f"Hi {name}",
        f"Hello {name}."
    ]

    print(
        greetings[
            random.randint(0, len(greetings)-1)
        ]
    )
