import sys
print("enter the dimensions of first matrix A")
m=int(input("m value is"))
n=int(input("n value is"))
print("enter th dimensions of second matrix B")
p=int(input("p value is"))
q=int(input("q value is"))

if n == p:
    print("matrix multiplicaton is possible")
    print("enter the values in first matrix")
    A=[]
    for i in range (m):
        atem=[]
        for j in range (n):
            x=int(input())
            atem.append(x)
    A.append(atem)
    print("matrix A is")
    #print('\n'.join([' '.join(['{:4}'.format(atem) for atem in row])for row in A]))
    for i in range(A):
        for j in range(len(i)):
            print(A[i][j],end='')
        print()
    print("enter the values in second matrix")
    B=[]
    for i in range (p):
        btem=[]
        for j in range (q):
            x=int(input())
            btem.append(x)
    B.append(btem)
    print("matrix B is")
    for i in range(len(B)):
        for j in range(len(i)):
            print(B[i][j],end=' ')
        print()
    print("multiplication of the two matrix")
    C=[]
    for i in range (m):
        e=[]
        for j in range (q):
            r=0
            for k in range(q):
                r += A[i][k]*B[k][j]
            e.append(r)
        C.append(e)
    print("displaying resultant matrix c")
    for i in range(len(C)):
        for j in range(len(i)):
            print(C[i][j],end='')
        print()
else:
    print("matrix multiplication not possible")