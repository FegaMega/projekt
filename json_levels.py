from Object import objects
level = [[372, 153, 60, 60, [126, 196, 90], "object"], [53, 386, 100, 60, [77, 135, 201], "object"]]
nlev = []
lev = []
i = 0
for n in level:
    lev += level[i]
    if lev[len(lev) - 1] == "object":
        level[i] = (lev[0], lev[1], lev[2], lev[3], (lev[4]))
    i += 1
