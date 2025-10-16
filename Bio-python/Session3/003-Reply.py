blood_sugar = []

for i in range(10):
    value = float(input(f"Enter blood sugar for patient {i+1}: "))
    blood_sugar.append(value)

average = sum(blood_sugar) / len(blood_sugar)
print(f"Average blood sugar: {average}")

print("Patients with blood sugar higher than average:")
for i, value in enumerate(blood_sugar):
    if value > average:
        print(f"Index {i}: {value}")

