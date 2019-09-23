time = input()
hour, minute = time.split(":")
suffix = "none"
shour = "none"
sminute = "none"
if int(hour) <= 11:
    suffix = "am"
if int(hour) > 11:
    suffix = "pm"

if int(minute) < 20 and int(minute) > 10:
    if minute == "00":
        sminute = ""

    elif minute == "11":
        sminute = "eleven"

    elif minute == "12":
        sminute = "twelve"

    elif minute == "13":
        sminute = "thirteen"

    elif minute == "14":
        sminute = "fourteen"

    elif minute == "15":
        sminute = "fifteen"

    elif minute == "16":
        sminute = "sixteen"

    elif minute == "17":
        sminute = "seventeen"

    elif minute == "18":
        sminute = "eighteen"

    elif minute == "19":
        sminute = "nineteen"

if int(minute) >= 0 and int(minute) < 10:
    if minute[1] == "0":
        sminute = ""
    elif minute[1] == "1":
        sminute ="oh one"
    elif minute[1] == "2":
        sminute = "oh two"
    elif minute[1] == "3":
        sminute ="oh three"
    elif minute[1] == "4":
        sminute = "oh four"
    elif minute[1] == "5":
        sminute ="oh five"
    elif minute[1] == "6":
        sminute = "oh six"
    elif minute[1] == "7":
        sminute ="oh seven"
    elif minute[1] == "8":
        sminute ="oh eight"
    elif minute[1] == "9":
        sminute ="oh nine"

if int(minute) >= 20 and int(minute) <= 59:
    if minute[0] == "2":
        sminute =  "twenty "
    elif minute[0] == "3":
        sminute =  "thirty "
    elif minute[0] == "4":
        sminute = "fourty "
    elif minute[0] == "5":
        sminute = "fifty "
    elif minute[0] == "6":
        sminute = "sixty "
    elif minute[0] == "7":
        sminute = "seventy "
    elif minute[0] == "8":
        sminute = "eighty "
    elif minute[0] == "9":
        sminute ="ninety "

    if minute[1] == "0":
        sminute = ""
    elif minute[1] == "1":
        sminute = sminute + "one"
    elif minute[1] == "2":
        sminute = sminute + "two"
    elif minute[1] == "3":
        sminute = sminute + "three"
    elif minute[1] == "4":
        sminute = sminute + "four"
    elif minute[1] == "5":
        sminute = sminute + "five"
    elif minute[1] == "6":
        sminute = sminute + "six"
    elif minute[1] == "7":
        sminute = sminute + "seven"
    elif minute[1] == "8":
        sminute = sminute + "eight"
    elif minute[1] == "9":
        sminute = sminute + "nine"





if hour == "00":
    shour = "twelve"

elif hour == "01":
    shour = "one"

elif hour == "02":
    shour = "two"

elif hour == "03":
    shour = "three"

elif hour == "04":
    shour = "four"

elif hour == "05":
    shour = "five"

elif hour == "06":
    shour = "six"

elif hour == "07":
    shour = "seven"

elif hour == "08":
    shour = "eight"

elif hour == "09":
    shour = "nine"

elif hour == "10":
    shour = "ten"

elif hour == "11":
    shour = "eleven"

elif hour == "12":
    shour = "twelve"
elif hour == "13":
    shour = "one"
elif hour == "14":
    shour = "two"
elif hour == "15":
    shour = "three"
elif hour == "16":
    shour = "four"
elif hour == "17":
    shour = "five"
elif hour == "18":
    shour = "six"
elif hour == "19":
    shour = "seven"
elif hour == "20":
    shour = "eight"
elif hour == "21":
    shour = "nine"
elif hour == "22":
    shour = "ten"
elif hour == "23":
    shour = "eleven"


print("It's " + shour, sminute, suffix)


