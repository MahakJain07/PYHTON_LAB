def swap():
    a = int(input("Enter value:"))
    b = int(input("Enter value: "))
    print("Before swapping a:", a)
    print("Before swapping b:", b)
    a,b = b, a
    print("After swapping a becomes:",a)
    print("After swapping b becomes:", b)

swap()