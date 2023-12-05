ins = [lines for lines in open("aoc1/agherjiolghyhny.txt", "r").read().split("\n")]
fnb = 0
dick = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
for l in ins:
    tnb = ()
    s = ""
    for c in l:
        if(c.isnumeric()):
            tnb.append(int(c))
            s = ""
        else:
            s += c
            if(dick.get(s) is not None):
                tnb.append(dick.get(s))
                s = ""
    fnb += (tnb[0] * 10) + tnb[-1]
print(fnb)