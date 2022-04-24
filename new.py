print("hello world")
n=input("Enter your name :")
list = []
list.append(n)
for i in range(len(n)):
    print(list[0][i],end="-")
print("executed!")
