def HammingDistance(p , q):
    count = 0
    for a, b in zip(p, q):
        if a != b:
            count += 1
    return count

print(HammingDistance(p, q))