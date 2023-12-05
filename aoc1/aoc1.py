inp = [lines for lines in open("aoc1/agherjiolghyhny.txt", "r").read().split("\n")]
finalnb = 0
dic = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}

def p1(inp):
    for line in inp:
        tempnb = []
        for num in line:
            if(num.isnumeric()):
                tempnb.append(int(num))

def p2(inp):
    for char in inp:
        tempnb = []
        stri += char
        if(stri.isnumeric()):
            stri = ""
        if(dic.get(stri) is not None):
            tempnb.append(dic.get(stri))
            stri = ""


    finalnb += (tempnb[0] * 10) + tempnb[-1]
print(finalnb)