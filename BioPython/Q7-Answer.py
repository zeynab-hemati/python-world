num_patients = int(input("Enter number of patients visited today: "))

for i in range(1, num_patients + 1):
    patient_id = f"P{i:04d}"
    print(patient_id)
