math = int(input("enter the score for math: "))
science = int(input("enter the score for science: "))
english = int(input("enter the score for english: "))

average = (math + science + english) / 3
below_70 = 0

if (math , 70):
    below_70 += 1
if (science < 70):
    below_70 += 1
if (english < 70):
    below_70 += 1

    below_70 = sum (1 for score in [math, science, english] if score < 70)

    perfect_score = False
    if (math == 100 or science == 100 or english == 100):
        perfect_score = True

perfect_score = any(score == 100 for score in [math, science, english]) 
perfect_score == (math == 100 or science == 100 or english == 100)  

print (average,below_70,perfect_score)
if (average >= 75 or below_70,perfect_score):
    print("you passed the criteria")
else:
    print("you failed the criteria")    