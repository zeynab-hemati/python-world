def to_meters(h):
    h = float(h)
    return h / 100 if h > 10 else h  # >10 → assume cm, else meters

try:
    weight = float(input("Enter weight in kg: "))
    height = to_meters(input("Enter height (m or cm): "))

    if weight <= 0 or height <= 0:
        raise ValueError

    bmi = weight / (height ** 2)
    print("BMI:", round(bmi, 2))

    if bmi <= 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Healthy weight")
    elif bmi < 30:
        print("Overweight")
    elif bmi < 35:
        print("Obese (Class I)")
    elif bmi < 40:
        print("Obese (Class II)")
    else:
        print("Obese (Class III)")

except ValueError:
    print("Invalid input")
