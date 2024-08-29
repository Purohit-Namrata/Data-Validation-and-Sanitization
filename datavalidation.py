def stringmanipulation():
    x = []

    while True:
        try:
            l = int(input("Enter the length of the list: "))
            if l < 0:
                print("Length cannot be negative. Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(l):
        while True:
            y = input(f"Enter string {i + 1}: ")
            if y.isalpha():
                y = y.lower()
                x.append(y)
                break
            else:
                print("Invalid input. Please enter only alphabetic strings.")

    print("The sanitized list is:", x)

stringmanipulation()
