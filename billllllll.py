import random
names=input("enter the names:")
names_split=names.split(",")
print(names_split)
length=len(names_split)
choice=random.randint(0,length-1)
print(f"pay the bill is:{names_split[choice]}")
