n=int(input('enter n:'))
n1=0
n2=1
sum=0
for i in range(0,n):
print(n1,end'  ')
sum=sum+n1
Next=n1+n2
n1=n2
n2=Next
print('the sum of fibonacci series:',sum)

Output:
enter n:8
0 1 1 2 3 5 8 13
the sum of fibonacci series:33
