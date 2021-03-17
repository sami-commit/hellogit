result = 0
a = float(input("number 1: "))
while True:
    op = input("Operator: ")
    b = float(input("number 2: "))
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Not allowed to divide with 0")
        else:
            result = a / b
    else:
        print("Unknown operator")
    print(result)
    if input("Clear all (y/n)?") == 'y':
        result = 0
        import os 
        os.system('cls')
        a = float(input("number 1: "))
        continue
    elif input("Exit (y/n)?") == 'y':
        break
    a = result
