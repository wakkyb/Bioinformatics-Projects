Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
Pattern = "ATTCTGGA"
d = 3
def HammingDistance(Text , Pattern):
    count = 0
    for a, b in zip(Text , Pattern):
        if a != b:
            count += 1
    return count

def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    n = len(Text)
    k = len(Pattern)
    for i in range(n-k+1):
        if HammingDistance(Text[i:i+k], Pattern) <= d:
            positions.append(i)
    return positions

Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
Pattern = "ATTCTGGA"
d = 3

print(ApproximatePatternMatching(Text, Pattern, d))
