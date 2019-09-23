ustring = input("Input Xs and Ys: ")

def balanced(string):
    x_count = 0
    y_count = 0
    for x in string:
        if x == "x":
            x_count+=1
        if x == "y":
            y_count+=1
    if x_count == y_count:
        print("true")
    else:
        print("false")

balanced(ustring)
