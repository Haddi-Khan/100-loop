# 6.	Find the sum of numbers from 1 to N.
# n=int(input("Enter any number for the sum "))
# sum = n* (n+1) //2
# print (sum)
n=int(input("Enter any number for the sum " ))
total =0
for i in range (1,n+1):
    total +=i
print (total)