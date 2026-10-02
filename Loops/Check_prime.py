Number = int(input("Enter the number : "))
count = 0

for x in range(2,Number): 
    if Number % x == 0:
        count +=1
        break
if count == 0:
    print(Number,"is a prime")
else:
    print("Not a prime number")      