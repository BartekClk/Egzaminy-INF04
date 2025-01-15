a,b=int(input("A:")),int(input("B:"))
while a!=b:a,b=a-b,b if a>b else a,b-a
print(a)