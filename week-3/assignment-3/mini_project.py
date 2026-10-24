day = input("What day is it?").strip().lower()
time_of_day = input("What time of day? ").strip().lower()

if day == "Tuesday":
    if time_of_day == "morning":
        print("Suggestion: Morning Python class — great time to focus!")
    elif time_of_day == "afternoon":
        print("Suggestion: coding with practice!")
    elif time_of_day == "evening":
        print("Suggestion: Take a walk for some fresh air!")
    else:
        print("Sorry, I don't recognize that time. Try morning, afternoon, or evening.")
elif day == "Thursday":
     if time_of_day == "morning":
            print("Suggestion: Enjoy a relaxing breakfast!")
     elif time_of_day == "afternoon":
            print("Suggestion: Afternoon Python class — great time to focus!")
     elif time_of_day == "evening":
            print("Suggestion: Take a walk for some fresh air!")
     else:
            print("Sorry, I don't recognize that time. Try morning, afternoon, or evening.")
elif day == "saturday":
    if time_of_day == "morning":
        print("Suggestion: Enjoy a relaxing breakfast.")
    elif time_of_day == "afternoon":
        print("Suggestion: Go shopping or explore somewhere new with family.")
    elif time_of_day == "evening":
        print("Suggestion: Family time a movie night or try a new recipe.")
    else:
        print("Sorry, I don't recognize that time. Try morning, afternoon, or evening.")

else:
    print("Sorry, I don't recognize that day. Try Tuesday, Thursday or Saturday.")





