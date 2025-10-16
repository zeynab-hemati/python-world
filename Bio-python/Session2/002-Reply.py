while True:
    try:
        age = int(input("Enter patient's age: "))
        if 0 <= age <= 120:
            print(f"Age accepted: {age} years")
            break
        else:
            print("Invalid age. Please enter a value between 0 and 120.")
    except ValueError:
        print("Invalid input. Please enter a number.")
