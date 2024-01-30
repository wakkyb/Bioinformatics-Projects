def MinimumSkew(Genome):
    positions = [] # output variable
    oska = SkewArray(Genome)
    min_skew = min(oska)
    for i,skew in enumerate(oska):
        if skew == min_skew:
            positions.append(i)
     
    # your code here
    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    n = len(Genome)
    skew = [0]
    for i in range(n):
        if Genome[i] == "G":
            skew.append( skew[i] + 1)
        elif Genome[i] == "C":
            skew.append( skew[i] - 1)
        else:
            skew.append(skew[i])
    return skew 

    
print(MinimumSkew(Genome))