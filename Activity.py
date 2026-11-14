num=input("Enter a number: ")
result=0
for i in num:
    result+=int(i)**len(num)

if result==int(num):
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")


n=input("Enter a number: ")
result=0
a=int(n[0])**3
b=int(n[1])**3
c=int(n[2])**3
result+=a+b+c

if result==int(n):
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")


main=int(input("Enter a number: "))
lis=[]
for i in range(1, main+1):
    if main%i==0:
        lis.append(i)

print(f"Factors of {main} are {lis}")


roman=input("Enter a roman numeral: ")
result=0
for i in roman:
    if i=="I":
        result+=1
    if i=="V":
        result+=5
    if i=="X":
        result+=10
    if i=="L":
        result+=50
    if i=="C":
        result+=100
    if i=="D":
        result+=500
    if i=="M":
        result+=1000

print(result)
