score = int(input())
grade = ''
errMsg = "잘못된 점수입니다"
if(score >= 90): 
    grade = 'A 학점'
    print(grade)
elif 80 <= score and score < 90 : 
    grade = 'B 학점'
    print(grade)
elif 70 <= score and score < 80 : 
    grade = 'C 학점'
    print(grade)
elif 60 <= score and score < 70 : 
    grade = 'D 학점'
    print(grade)
elif 7 <= score and score < 60 :
    grade = "F 학점"
    print(grade)
else : 
    print(errMsg)
    
