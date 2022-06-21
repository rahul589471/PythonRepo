x=0;
while True:
    x = int(
        input("Enter 1 to Add Diet/Gym, 2 to Look Diet/Gym , 3 to Exit"))

    if x==3:
        break;

    if x == 1:
        n = int(input("Enter \n 1 for Rahul\n 2 for Ram\n  3 for Shyam\n"))
        choice = int(input("Enter - 1 for Diet, 2 for Gym"))

        if choice == 1:
            if (n == 1):
                with open('rahul_diet.txt', 'w+') as f:
                    f.write(input("Enter Diet for Rahul"))
                    print("Rahul diet Added")
            elif(n == 2):
                with open("ram_diet.txt", "w+") as f:
                    f.write(input("Enter Diet for Ram"))
            elif(n == 3):
                with open("shyam_diet.txt", "w+") as f:
                    f.write(input("Enter Diet for Shyam"))
            else:
                print("please enter correct option")
        elif choice == 2:
            if (n == 1):
                with open('rahul_gym.txt', 'w+') as f:
                    f.write(input("Enter Gym for Rahul"))
            elif n == 2:
                with open("ram_gym.txt", "w+") as f:
                    f.write(input("Enter Gym for Ram"))
            elif n == 3:
                with open("shyam_gym.txt", "w+") as f:
                    f.write(input("Enter Gym for Shyam"))
            else:
                print("please enter correct option")
        else:
            print("please enter correct option")
    # Display results
    elif x == 2:
        o = int(input("Whose diet/gym to see: Rahul -1, Ram-2, Shyam -3"))
        choice2 = int(input("Enter 1 for Diet , 2 for Gym"))

        if choice2 == 1:
            if (o == 1):
                try:
                    with open('rahul_diet.txt', 'r') as f:
                        rahul_diet_data=f.readlines()
                        print(rahul_diet_data)
                except Exception as e:
                    print("Rahul Diet is not yet added. Please add his diet first.")
            elif(o == 2):
                try:
                    with open('ram_diet.txt', 'r') as f:
                        ram_diet_data=f.readlines()
                        print(ram_diet_data)
                except Exception as e:
                    print("Ram Diet is not yet added. Please add his diet first.")
            elif(o == 3):
                try:
                    with open('shyam_diet.txt', 'r') as f:
                        shyam_diet_data = f.readlines()
                        print(shyam_diet_data)
                except Exception as e:
                    print("Shyam Diet is not yet added. Please add his diet first.")
            else:
                print("please enter correct option")
        elif choice2 == 2:
            if (o == 1):
                try:
                    with open('rahul_gym.txt', 'r') as f:
                        rahul_gym_data = f.readlines()
                        print(rahul_gym_data)
                except Exception as e:
                    print("Rahul Gym Data is not yet added. Please add his gym data first.")
            elif o == 2:
                try:
                    with open('ram_gym.txt', 'r') as f:
                        ram_gym_data = f.readlines()
                        print(ram_gym_data)
                except Exception as e:
                    print("Ram Gym Data is not yet added. Please add his gym data first.")
            elif o == 3:
                try:
                    with open('shyam_gym.txt', 'r') as f:
                        shyam_gym_data = f.readlines()
                        print(shyam_gym_data)
                except Exception as e:
                    print("Shyam Gym Data is not yet added. Please add his gym data first.")
            else:
                print("please enter correct option")
        else:
            print("please enter correct option")
    else:
        print("please enter correct option")

if x==3:
    print("Thanks fot the visit !")