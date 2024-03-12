N = int(input())
grades = []
for i in range(N):
    grade = int(input())
    grades.append(grade)

demon_list = grades
demon_list = list(set(demon_list))
demon_list.sort()
bronze_grade = demon_list[-3]
print(bronze_grade, grades.count(bronze_grade))