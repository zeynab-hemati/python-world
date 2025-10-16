blood_pressures = []

for i in range(10):
    value = float(input(f"Enter blood pressure for patient {i+1}: "))
    blood_pressures.append(value)

high_bp = [bp for bp in blood_pressures if bp >= 130]
low_bp = [bp for bp in blood_pressures if bp < 130]

print("Blood pressures ≥ 130:", high_bp)
print("Blood pressures < 130:", low_bp)
