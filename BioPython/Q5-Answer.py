while True:
    dna = input("Enter a DNA sequence: ").upper()
    if all(base in "ATGC" for base in dna):
        complement = ""
        for base in dna:
            if base == "A":
                complement += "T"
            elif base == "T":
                complement += "A"
            elif base == "G":
                complement += "C"
            elif base == "C":
                complement += "G"
        print("Complementary DNA:", complement)
        break
    else:
        print("Invalid sequence. Please enter only A, T, G, or C.")
