# input from user
# number of guesses left
# total guesses - 9
# correct answer in number of guesses5



print("Hello user. Let's play a game now. I have one number in my mind. You have to guess it in max 9 guessses.\n"
      "Let's start now !")
number_of_guesses = 9
user_number = int(input("Enter your number"))
number_of_guesses_used =0;
number_of_guesses_left =number_of_guesses;
my_number = 10


while number_of_guesses>0:
    if number_of_guesses_left !=9:
        user_number = int(input("Enter your number again!"))
    if user_number == my_number:
        print("Congratulations. Your guess is right!")
        if number_of_guesses_used!=1:
            number_of_guesses_used =number_of_guesses_used+1;
        print("You have guessed it correctly in total ", number_of_guesses_used, " guesses")
        break;
    else:
        print("Bad luck!")
        number_of_guesses_left = number_of_guesses_left - 1;
        number_of_guesses_used =number_of_guesses_used+1;
        print(number_of_guesses_left, "  guesses left")
        if user_number < my_number:
            print(" Think about number greater than ", user_number)
        else:
            print(" Think about number less than ", user_number)


if number_of_guesses == 0:
    print("Game over !")
