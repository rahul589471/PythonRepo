print("Now enter your login info...")
name = input("Enter your name here\n")
Mobile_number = input("Enter your mobile number\n")
State = input("Enter the state in which you live\n")
father_name = input("Enter your Father's name\n")
data = f"Your login info is\nName-{name}\nMobile number-{Mobile_number}\nState-{State}\nFather's name-{father_name}"
print(data)
with open("Login Info.txt","a") as a:
    a.write(data + "\n")
print("Login Successful..")