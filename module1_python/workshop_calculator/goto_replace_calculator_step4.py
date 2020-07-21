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
    if opsList[0] == 'remove':
        return 
    if opsList[1] == 'calc':
        return calc(opsList[2], float(opsList[3]), float(opsList[4]))
    else:
        return opsList[1]


with open("step_4_goto_replace.txt", 'r') as f:
    outputCommands = [x.strip() for x in f]

outputList = [processCommand(x) for x in outputCommands]

print(outputList)

memory = []

i = 0
while i < len(outputList):
    linenumber = int(outputList[int(i)]) - 1
    statement = outputCommands[int(linenumber)]
    if statement in memory:
        break
    memory.append(statement)
    i = linenumber

print(f"statement: {outputCommands[int(linenumber)]} , linenumber: {linenumber + 1}")