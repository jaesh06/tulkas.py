import json

# with open("out.json") as f:
#      db = json.load(f)
# print(json.dumps(db, indent=4))

# r_exercises = []
# r_exercise_number = int(input("Enter number of recommended exercises: "))
# for i in range(r_exercise_number):
#     r_exercises.append(input("Enter recommended exercise " + str(i+1) + ": "))
# date = input("Enter date in format yymmdd: ")
# completion_time = input("Enter completion time in format mm:ss : ")
# a_exercises = []
# a_exercise_number = int(input("Enter number of actual exercises: "))
# for i in range(a_exercise_number):
#     a_exercises.append(input("Enter recommended exercise " + str(i+1) + ": "))
# note = input("Notes: ")
# current_workout = {new_name: {"recommended": [r_exercises], "dates": {date: {"time": completion_time, "actual": [a_exercises], "note": note}}}}
# db.update(current_workout)
def enter_workout(workout_name):
    r_exercises = []
    r_exercise_number = int(input("Enter number of recommended exercises: "))
    for i in range(r_exercise_number):
        r_exercises.append(input("Enter recommended exercise " + str(i+1) + ": "))
    date = input("Enter date in format yymmdd: ")
    completion_time = input("Enter completion time in format mm:ss : ")
    a_exercises = []
    a_exercise_number = int(input("Enter number of actual exercises: "))
    for i in range(a_exercise_number):
        a_exercises.append(input("Enter recommended exercise " + str(i+1) + ": "))
    note = input("Notes: ")
    current_workout = {workout_name: {"recommended": [r_exercises], "dates": {date: {"time": completion_time, "actual": [a_exercises], "note": note}}}}
    print(json.dumps(current_workout, indent=4))
    write_choice = input("Write to file? (y or n): ")
    if write_choice == "y":
        db.update(current_workout)
        with open("workout_db.json", "w") as outfile:
            json.dump(db, outfile, indent=4)
        print("Data written to file.")
running = True

while(running):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Tulkas the Strong: of no use as a counselor, but a hearty friend.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1) View")
    print("2) Enter")
    print("3) Exit")
    main_menu = input("View or Enter?: ")
    if main_menu == "1":
        with open("workout_db.json") as f:
            data = json.load(f)
        wo_name = input("Workout name: ")
        print(data[wo_name]["dates"])
    if main_menu == "2":
        with open("workout_db.json") as f:
            db = json.load(f)
        new_name = input("Enter workout name: ")
        if db.get(new_name):
            existing_choice = input("Name exists. Would you like to add a new date? (y or n): ")
            if existing_choice == "y":
                enter_workout(new_name)
            else:
                continue
        else:
            choice = input("Name was not found. Would you like to add it? (y or n): ")
            if choice == "y":
                r_exercises = []
                r_exercise_number = int(input("Enter number of recommended exercises: "))
                for i in range(r_exercise_number):
                    r_exercises.append(input("Enter recommended exercise " + str(i+1) + ": "))
                date = input("Enter date in format yymmdd: ")
                completion_time = input("Enter completion time in format mm:ss : ")
                a_exercises = []
                a_exercise_number = int(input("Enter number of actual exercises: "))
                for i in range(a_exercise_number):
                    a_exercises.append(input("Enter recommended exercise " + str(i+1) + ": "))
                note = input("Notes: ")
                current_workout = {new_name: {"recommended": [r_exercises], "dates": {date: {"time": completion_time, "actual": [a_exercises], "note": note}}}}
                print(json.dumps(current_workout, indent=4))
                write_choice = input("Write to file? (y or n): ")
                if write_choice == "y":
                    db.update(current_workout)
                    with open("out.json", "w") as outfile:
                        json.dump(db, outfile)
                    print("Data written to file.")
    if main_menu == "3":
        running = False
            
    
# with open("workout_db.json") as f:
#     data = json.load(f)

# print(data["Jackie"]["recommended"][1])
