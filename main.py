n=17
print("The Table of 17:")
for i in range(1,11):
    m=n*i
    print(m)


num=1
sum=0
while (num<=10):
    sum=sum+num
    num=num+1
    print(sum)

 number=29
flag=False
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            flag=True
            break
        if flag:
            print(number,"is not a prime number")
            else:
            print(number,"is a prime number")