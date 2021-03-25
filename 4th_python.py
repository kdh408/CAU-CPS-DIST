import random

total_students = 30
total_teams = 6

students = range(30)

list_students = list(students)

print(list_students)

random.shuffle(list_students)  #shuffle: list 를 섞어 주는 것
print(list_students)

project_team = []
for i in range(6):  #6개의 팀을 만듦
    num = int(total_students/total_teams)
    index = i * num  #각 팀에 들어가는 첫번째 사람의 번호
    # i: 0,1,2,3,4,5 -> 0,5, 10,15,20,25 // (0,1,2,3,4) 한팀 (5,6,7,8,9) 한팀 ...
    project_team.append(list_students[index:index+num])
    #list 타입 변수 a = [1:5] -> 1,2,3,4를 a()에 넣겠다

for i in project_team:
    print(i)
