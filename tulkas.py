import json
import re

def enter_workout(workout_name):
    r_exercises = []
    custom = input("Is this a custom workout? (y or n): ")
    r_exercise_number = int(input("Enter number of recommended exercises: "))
    for i in range(r_exercise_number+1):
        if i > r_exercise_number-1:
            r_exercises.append(input("Recommended weight in lbs. (type 0 if no weight): "))
        else:
            r_exercises.append(input("Enter recommend exercise " + str(i+1) + ": "))
    date = input("Enter date in format yymmdd: ")
    completion_time = input("Enter completion time in format mm:ss : ")
    a_exercises = []
    a_exercise_number = int(input("Enter number of actual exercises: "))
    for i in range(a_exercise_number+1):
        if i > a_exercise_number-1:
            a_exercises.append(input("Actual weight in lbs. (type 0 if no weight): "))
        else:
            a_exercises.append(input("Enter actual exercise " + str(i+1) + ": "))
    note = input("Notes: ")
    current_workout = {workout_name: {"recommended": [r_exercises], "dates": {date: {"time": completion_time, "actual": [a_exercises], "note": note}}, "custom": custom}}
    print(json.dumps(current_workout, indent=4))
    write_choice = input("Write to file? (y or n): ")
    if write_choice == "y":
        db.update(current_workout)
        with open("workout_db.json", "w") as outfile:
            json.dump(db, outfile, indent=4)
        print("Data written to file.")
        input("Press Enter to continue...")
    else:
        return

def update_workout(workout_name):
    date = input("Enter date in format yymmdd: ")
    completion_time = input("Enter completion time in format mm:ss : ")
    a_exercises = []
    a_exercise_number = int(input("Enter number of actual exercises: "))
    for i in range(a_exercise_number+1):
        if i > a_exercise_number-1:
            a_exercises.append(input("Actual weight in lbs. (type 0 if no weight): "))
        else:
            a_exercises.append(input("Enter actual exercise " + str(i+1) + ": "))
    note = input("Notes: ")
    current_workout = {date: {"time": completion_time, "actual": [a_exercises], "note": note}}
    print(json.dumps(current_workout, indent=4))
    write_choice = input("Write to file? (y or n): ")
    if write_choice == "y":
        db[workout_name]["dates"].update(current_workout)
        with open("workout_db.json", "w") as outfile:
            json.dump(db, outfile, indent=4)
        print("Data written to file.")
        input("Press Enter to continue...")
    else:
        return

while(True):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Tulkas the Strong: of no use as a counselor, but a hearty friend.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1) View")
    print("2) Enter")
    print("3) Exit")
    main_menu = input("What would you like to do?: ")
    if main_menu == "1":
        try:
            with open("workout_db.json") as f:
                data = json.load(f)
        except:
            print("Oh no! workout_db.json is empty. There is nothing to view.")
            input("Press Enter to continue...")
            continue
        print("Search database by: ")
        print("1) Workout Name")
        print("2) Date")
        print("3) Recommended Exercise Keyword")
        search_choice = input("Selection: ")
        if search_choice == "1":
            wo_name = input("Workout name: ")
            if data.get(wo_name):
                print(json.dumps(data[wo_name]["dates"], indent=4))
                input("Press Enter to continue...")
            else:
                print("Workout not found.")
                input("Press Enter to continue...")
        if search_choice == "2":
            search_date = input("Date (yymmdd): ")
            for wo in data:
                for date in data[wo]["dates"]:
                    if date == search_date:
                        print("Workout Name: " + wo)
                        print(json.dumps(data[wo]["dates"][date]))
                        input("Press Enter to continue...")
                        break
        if search_choice == "3":
            keyword = input("Exercise keyword (this searches in the recommended exercise list): ")
            regex_string = "^.*" + keyword + ".*$"
            for wo in data:
                for rec in data[wo]["recommended"]:
                    for ex in rec:
                        result = re.search(regex_string, ex)
                        if result:
                            print(wo + " : " + str(data[wo]["recommended"]))
    if main_menu == "2":
        try:
            with open("workout_db.json") as f:
                db = json.load(f)
        except:
            with open("workout_db.json", "w") as f:
                json.dump({}, f, indent=4)
            with open("workout_db.json") as f:
                db = json.load(f)
        new_name = input("Enter workout name: ")
        if db.get(new_name):
            existing_choice = input("Workout exists. Would you like to add a new date? (y or n): ")
            if existing_choice == "y":
                update_workout(new_name)
            else:
                continue
        else:
            choice = input("Workout was not found. Would you like to add it? (y or n): ")
            if choice == "y":
                enter_workout(new_name)
            else:
                continue
    if main_menu == "3":
        break
