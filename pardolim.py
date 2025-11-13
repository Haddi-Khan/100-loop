n= "madam"
rev = ""
i = len(n) - 1
while i >= 0:
    rev = rev + n[i]
    i -= 1
if rev==n:
    print ("pal")
else :
    print("not")