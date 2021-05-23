a=input("Enter number 1\n")
b=input("Enter number 2\n")
c=input("Enter the number 3\n")
if a>b:
    if a>c:
        print("{0} is greatest".format(a))
    else:
        print("{0} is greatest".format(c))
elif b>a :
    if b>c:
        print("{0} is greatest".format(b))
    else:
        print("{0} is greatest".format(c))