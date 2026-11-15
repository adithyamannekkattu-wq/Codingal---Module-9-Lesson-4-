binary=input("Enter a binary number: ")

result=0
decrement=-1
for i in range(0, len(binary)):
    result+=int(binary[decrement])*2**i
    decrement-=1

print(result)