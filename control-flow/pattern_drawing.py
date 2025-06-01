size = int(input("Enter the size of the pattern: "))
while i < size:
    for j in range(size):
        print("*", end="")
    print()
    i++
