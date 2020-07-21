with open("something.txt", 'w') as f:
    f.write("hello")

with open("something.txt", 'r') as f:
    textString = f.read()

print(f"{textString}")