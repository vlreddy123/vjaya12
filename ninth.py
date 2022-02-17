#sum of even numbers upto given range
n=int(input("Enter a n value:"))
sum=0
for i in range(2,n+2):
    if i%2==0:
        sum=sum+i
 print("sum of even numbers upto",n,'is',sum)

output:
Enter a n value:10
sum of even numbers upto 10 is 30 

#Printing odd numbers sum upto n:
n=int(input('Enter n value:'))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum=sum+i
print("Sum of odd numbers up to",n,'is',sum)

output:
Enter n value:10
Sum of odd numbers up to 10 is 25
