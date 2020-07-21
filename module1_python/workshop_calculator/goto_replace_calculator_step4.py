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
    if opsList[1] == 'calc':
        return calc(opsList[2], float(opsList[3]), float(opsList[4]))
    else:
        return opsList[1]


with open("step_3_goto_calculations.txt", 'r') as f:
    outputCommands = [x for x in f]

outputList = [processCommand(x) for x in outputCommands]

memory = []

for i in outputList:
    linenumber = outputList[i]
    statement = outputCommands[int(linenumber)]
    if statement in memory:
        break
    memory.append(statement)

print(f"statement: {outputCommands[int(linenumber)]} , linenumber: {linenumber}")