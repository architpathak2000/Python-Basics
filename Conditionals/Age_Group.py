Age = int(input("Enter Age:"))
def Age_Group():
   
    if(Age < 13):
        print("Child")
    elif (Age <= 19 and Age >= 13):
        print("Teenager")
    elif (Age >=20 and Age <=59):
        print("Adult")
    elif(Age >=60):
        print("Senior Citizen")
    return Age
