scores = input()
ascore = 0
bscore = 0
cscore = 0
dscore = 0
escore = 0
for x in scores:
    if x == "a":
        ascore += 1
    if x == "b":
        bscore += 1
    if x == "c":
        cscore += 1
    if x == "d":
        dscore += 1
    if x == "e":
        escore += 1

    if x == "A":
        ascore -= 1
    if x == "B":
        bscore -= 1
    if x == "C":
        cscore -= 1
    if x == "D":
        dscore -= 1
    if x == "E":
        escore -= 1

print("a: %s, b: %s, c: %s, d: %s, e: %s" % (ascore, bscore, cscore, dscore, escore))
