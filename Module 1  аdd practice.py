grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=len(grades[0])
b=len(grades[1])
c=len(grades[2])
d=len(grades[3])
f=len(grades[4])
students_list = list(students)
students_list_sort = sorted(students_list)
average_grades = {students_list_sort[0] : sum(grades[0])/a, students_list_sort[1] : sum(grades[1])/b,
                  students_list_sort[2] : sum(grades[2])/c, students_list_sort[3] : sum(grades[3])/d,
                  students_list_sort[4] : sum(grades[4])/f}
print(average_grades)