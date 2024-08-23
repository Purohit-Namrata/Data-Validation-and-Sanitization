def stringmanipulation():
    x=[]
    l=int(input("Enter length of list "))

    for i in range(l):
        y=str(input("Enter string {} ".format(i+1)))
        if y.isalpha():
            y=y.lower()
            x.append(y)
        else:
            print("Please enter only character strings")

    print("The sanitized list is ",x)

stringmanipulation()