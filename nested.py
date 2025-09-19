rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")
symbol = input("Enter the symbol to use: ")
for i in range(int(rows)):
    for j in range(int(columns)):
        print(symbol, end=" ")
    print()