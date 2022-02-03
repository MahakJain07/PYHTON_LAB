# palindrome is nothing but any number or a string which remains unaltered when reversed
num = int(input("Enter a number"))
temp = num
rev = 0
while(num>0):
    dig = num%10
    rev = rev*10+dig
    num =num//10
if(temp==rev):
    print("the number is palindrone")
else:
    print("Not a palindrone")