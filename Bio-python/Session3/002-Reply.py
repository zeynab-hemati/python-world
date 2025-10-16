bmi_values = []

for i in range(5):
    value = float(input(f"Enter BMI for patient {i+1}: "))
    bmi_values.append(value)

max_bmi = max(bmi_values)
min_bmi = min(bmi_values)

max_index = bmi_values.index(max_bmi)
min_index = bmi_values.index(min_bmi)

print(f"Highest BMI: {max_bmi} at index {max_index}")
print(f"Lowest BMI: {min_bmi} at index {min_index}")
