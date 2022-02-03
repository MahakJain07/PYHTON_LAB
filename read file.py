f = open("hello.txt","r")
data = f.readlines()
count = 0
for lines in data:
    print(lines)
    count+=1
print("Total number of lines is :", count)
f.close()
