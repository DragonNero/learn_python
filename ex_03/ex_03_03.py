scoreInput = input("Enter score: ")
try:
    floatScoreInput = float(scoreInput)
except:
    print("Error, please enter numerical input")
    quit()

print("Grade: ", floatScoreInput)
    #Grades
if floatScoreInput > 1.0:
    print("Error, please enter numeric score between 0.00 and 1.00")
elif floatScoreInput >= 0.9:
    print("A")
elif floatScoreInput >= 0.8:
    print("B")
elif floatScoreInput >= 0.7:
    print("C")
elif floatScoreInput >= 0.6:
    print("D")
elif floatScoreInput < 0.00:
    print("Error, please enter numeric score between 0.00 and 1.00")
elif floatScoreInput < 0.6:
    print("F")
