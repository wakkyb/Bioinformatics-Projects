def Complement(Pattern):
    complement = ""

    for char in Pattern:
        if char == "T":
            complement += "A"
        elif char == "A":
            complement += "T"
        elif char == "G":
            complement += "C"
        elif char == "C":
            complement += "G"
        
    return complement
              
print(Complement("AAAACCCGGT"))