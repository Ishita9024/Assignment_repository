num= int(input("enter a number:-"))
i=0
print("")
while i<num:
    print(" ---"*num)
    print(f"| {0} "*num+"|")
    i=i+1
if i==num:
    print(" ---"*num)
