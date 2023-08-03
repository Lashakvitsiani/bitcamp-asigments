camel_case = input("camelCase: ")
snake_case = ""


for char in camel_case:
 
    if char == char.upper():
        snake_case += "_"

    snake_case += char.lower()


print(f"snake_case: {snake_case}")
