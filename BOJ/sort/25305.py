a=[int(z) for z in input().split(" ")]
scores=list()
for x in input().split(" "):
    scores.append(int(x))

scores.sort()
scores.reverse()

print(scores[a[1]-1])

