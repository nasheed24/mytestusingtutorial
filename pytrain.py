input("1 prints fibonacci series using loop"
      "2 prints fibonacci series using recursion")
select=int(input("select the option"))
if select == 1 :
    print("running the program using loop")
    num=int(input("enter a number:")) #take the value of print and assighn to num
    i=0
    fib0=0
    fib1=1
    while i<num :
        if i <= 1 :
            fibnext =i
        else:
            fibnext=fib0+fib1
            fib0=fib1
            fib1=fibnext
        i=i+1
        print(fibnext)
else:
    def recur_fibo(n):
        if n <= 1:
            return n
        else:
            return(recur_fibo(n-1)+recur_fibo(n-2))
    print("running the program using recursion")
    num = int(input("enter a number:"))  # take the value of print and assighn to num
    if num <=0:
        print("please enter a positive integer")
    else:
        print("fibonacci sequence:")
        for i in range(num):
            print(recur_fibo(i))