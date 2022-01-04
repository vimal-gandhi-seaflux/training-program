w=int(input("enter weight:"))
unit=input("(L)bs or (k)g:")
if unit.upper() == "L":
    c= w*0.45
    print(f"you are {c} kilos")
else:
    c=w/0.45
    print(f"you are {c} pounds")