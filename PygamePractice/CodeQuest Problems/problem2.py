input = input()
if len(input) == 10:
    a = input[0]
    b = input[1]
    c = input[2]
    d = input[3]
    e = input[4]
    f = input[5]
    g = input[6]
    h = input[7]
    i = input[8]
    if input[9] == "X":
        j = 10
    else:
        j = input[9]
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    e = int(e)
    f = int(f)
    g = int(g)
    h = int(h)
    i = int(i)
    j = int(j)
    a *= 10
    b *= 9
    c *= 8
    d *= 7
    e *= 6
    f *= 5
    g *= 4
    h *= 3
    i *= 2
    j *= 1
    sum = a+b+c+d+e+f+g+h+i+j
    remainder = sum % 11
    if remainder == 0:
        print("Valid")
    else:
        print("Invalid")