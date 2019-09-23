#Riley Underwood
#3/19/2019

def Write_scores():
    all_scoreslist1 = [("1:0:"), ("2:0:"), ("3:0:"), ("4:0:"), ("5:0:"), ("6:0:"), ("7:0:"), ("8:0:"), ("9:0:"), ("10:0:")]
    scorecheck = open("Star_Battles_HScores.txt", "w")
    for x in all_scoreslist1:
        scorecheck.write(str(x)) #Shows what was tryed, when, and if it was successful, with spacing inbetween.
        scorecheck.write("\n") #This is so that the .txt file does not just have one big line of entrys.
    scorecheck.close()
    print ("Rewrite Complete!")
    
Write_scores()
