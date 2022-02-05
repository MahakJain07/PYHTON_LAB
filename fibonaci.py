#  0 1 1 2 3 5 8 13 21............fibonaci series
def fibonaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

num = int(input("Enter the number "))
print("Fibonaci series :", fibonaci(num))