# operation = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#
# }

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


def processCommand(command):
    opsList = command.split(" ")
    if opsList[0] == 'calc':
        return calc(opsList[1], float(opsList[2]), float(opsList[3]))


with open("step_2_calculations.txt", 'r') as f:
    outputList = [processCommand(x) for x in f]

total = sum(outputList)

print(f"{total}")
