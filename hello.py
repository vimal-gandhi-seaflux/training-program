name=input("enter name ")
age =int(input("enter age"))
gender =input("enter gender")
print(f"name={name}\n gender={gender}")
if age<13:
    print("child")
elif (13<= age < 18):
    print("teen")
elif (18 <= age < 60):
    print("adult")
else:
    print(old)
