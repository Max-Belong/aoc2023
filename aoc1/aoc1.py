inp = [lines for lines in open("aoc1/agherjiolghyhny.txt", "r").read().split("\n")]
finalnb = 0
dic = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
for line in inp:
    tempnb = ()
    stri = ""
    for char in line:
        if(char.isnumeric()):
            tempnb.append(int(char))
            stri = ""
        else:
            stri += char
            if(dic.get(stri) is not None):
                tempnb.append(dic.get(stri))
                stri = ""
    finalnb += (tempnb[0] * 10) + tempnb[-1]
print(finalnb)