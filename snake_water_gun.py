import random
import time

print("Hello user ! Let's play game - Snake, Water and Gun !")
print("You have 10 chances and after that winner will be announced.")

n = 0;
cpu_points = 0;
user_points = 0;

while (n < 10):
    game_list = ["Snake", "Water", "Gun"]
    cpu_choice = random.choice(game_list)


    time.sleep(2)
    user_choice = input("Enter your Input - s for Snake, w for water , g for gun ")
    print("User choice is :" + user_choice)

    time.sleep(1)
    print("Cpu choice is :" + cpu_choice)

    if cpu_choice == 'Snake' and user_choice == 'w':
        cpu_points += 1;
        print("I won")
    elif cpu_choice == 'Snake' and user_choice == 'g':
        user_points += 1;
        print("You won")
    elif cpu_choice == 'Water' and user_choice == 's':
        user_points += 1;
        print("You won")
    elif cpu_choice == 'Water' and user_choice == 'g':
        cpu_points += 1;
        print("I won")
    elif cpu_choice == 'Gun' and user_choice == 's':
        cpu_points += 1;
        print("I won")
    elif cpu_choice == 'Gun' and user_choice == 'w':
        user_points += 1;
        print("You won")

    n += 1;

print("Time to declare Winner")
print("Ready ?")

time.sleep(3)
print("And the Winner is :")

if user_points > cpu_points:
    print("******************   You    ********************************************")
    print(f"You have  {str(user_points)}  points")
    print(f"I have  {str(cpu_points)}    points")
else:
    print("******************    Me    ***********************************")
    print(f"I have  {str(cpu_points)}   points")
    print(f"You have  {str(user_points)}  points")

print("Bye...Please come later !")
