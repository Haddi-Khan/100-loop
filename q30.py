# 30.	Check if a number is a palindrome.
n = int(input("Enter a number: "))
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if original == rev:
    print("Palindrome")
else:
    print("Not a palindrome")