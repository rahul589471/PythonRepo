from datetime import datetime, timedelta
import time

from Exercises.sample_music_program import play_music

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

water_time = (datetime.now()).strftime("%H:%M:%S")
eyes_time = (datetime.now() + timedelta(minutes=5)).strftime("%H:%M:%S")
exercise_time = (datetime.now() + timedelta(minutes=5)).strftime("%H:%M:%S")


print(f"water_time:  {water_time}")
print(f"eyes_time  : {eyes_time}")
print(f"exercise_time   : {exercise_time}")
print(datetime.now().strftime("%H:%M:%S"))

while datetime.now().strftime("%H:%M:%S") < "00:59:00":
    print("Program Running")

    if water_time == datetime.now().strftime("%H:%M:%S"):
        print("Time to Drink 1 glass water")
        play_music();
        w = input("Drank or Not")

        with open('rahul_water.txt', 'a') as f:
            f.write("Drank water at ")
            f.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
            f.write("\n")


        time.sleep(60)
        water_time = (datetime.now() + timedelta(minutes=4)).strftime("%H:%M:%S")

    elif eyes_time == datetime.now().strftime("%H:%M:%S") or datetime.now().strftime("%M") == "42":
        print("Time to Blink your eyes")
        play_music();
        e = input("Blank or Not")

        with open('rahul_eyes.txt', 'a') as f:
            f.write("Blink eyes at ")
            f.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
            f.write("\n")
        time.sleep(60)
        eyes_time = (datetime.now() + timedelta(minutes=4)).strftime("%H:%M:%S")

    elif exercise_time == datetime.now().strftime("%H:%M:%S") or datetime.now().strftime("%M") == "43":
        print("Time to exercise for 5 minutes")
        play_music();
        ex = input("Exercise Done or Not")

        with open('rahul_exercise.txt', 'a') as f:
            f.write("Exercise done at ")
            f.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S"))
            f.write("\n")
        time.sleep(60)
        exercise_time = (datetime.now() + timedelta(minutes=4)).strftime("%H:%M:%S")

