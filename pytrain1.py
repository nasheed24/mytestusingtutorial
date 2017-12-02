start_value=1
n=int(input("enter the number:"))
print("prime numbers between",start_value,"and",n,"are :")
for num in range(start_value,n+1):
    prime= True
    for i in range(2,num):
        if (num%i==0):
            prime= False
    if prime == True:
        print(num)
print("done.......")

'''if num >1:
        for i in range(2,num):
            if num >1:
                for i in range(2,num):
                    if (num % i)==0:
                        break
                    else:
                        print(num)
                        break'''