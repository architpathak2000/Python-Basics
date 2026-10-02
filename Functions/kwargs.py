def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: \n  {value}")

print_kwargs(Name="Ironman",power="Armour")  
print_kwargs(Name="Ironman")  
print_kwargs(Name="Ironman",power="Armour",enemy="Thanos")  