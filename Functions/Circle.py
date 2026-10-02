import math

def measurements(R):
    area = round(math.pi *(R * R),2)
    circumference = 2 *(math.pi * R)
    return{"Area":area,"Circumference":circumference}

radius = int(input("Enter Radius: "))
Result = measurements(radius)
print(Result)
