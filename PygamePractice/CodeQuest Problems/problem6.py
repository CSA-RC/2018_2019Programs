def SimpleSymbols(str):
    yup = True
    for x in range(len(str)):
        if str[0] == "+" and not str[0]=="=":
            if str[x] != "+" and str[x] != "=":
                try:
                    if str[x-1] == "+" and str[x+1] == "+":
                        pass
                    else:
                        yup = False
                except:
                    pass
            else:
                yup = False
        else:
            yup = False

    print(yup)
sequence = input()
SimpleSymbols(sequence)
