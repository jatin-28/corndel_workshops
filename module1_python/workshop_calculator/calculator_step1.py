def calc(operation, a, b):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == 'x':
        return a * b
    elif operation == '/':
        return a / b
    else:
        raise Exception(f"Sorry, invalid operation: {operation}")


operationStr = input("Enter command (<operation> <num> <num>):")
opsList = operationStr.split(" ")

print(opsList)

output = calc(opsList[0], int(opsList[1]), int(opsList[2]))

print(f"{output}")