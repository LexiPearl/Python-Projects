def scoresandgrades():
    arr=[]
    letter= "A"
    for count in range (0,10):
        print "Please provide your score."
        score = input()
        arr.append(score)
    print "Scores and Grades"
    for x in range(0, len(arr)):
        if arr[x] < 70:
            letter="D"
        elif arr[x] > 69 and arr[x] < 80:
            letter= "C"
        elif arr[x] > 79 and arr[x] < 90:
            letter="B"
        else:
            letter= "A"
        print "Score:", arr[x], ";", "Your grade is", letter,"!"
    print "End of the program. Bye!"
scoresandgrades()


# from random import randint
# print "Scores and Grades"
# for count in range(0, 10):
# 	score = randint(70, 100)
# 	if(score <= 70):
# 		grade = "D"
# 	elif(score <= 80):
# 		grade = "C"
# 	elif(score <= 90):
# 		grade = "B"
# 	else:
# 		grade = "A"
# 	print "Score: %d; Your grade is %s" %(score, grade)
# print "End of program. Bye!"
