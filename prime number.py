# to find prime number
num = 11
# If number is greater than 1
if num>1:
    for i in range(int(num/2)+1):
        print(num, "is not a prime number")
        break
    else:
        print(num, "is a prime number")
else:
     print(num, "is not a prime number")