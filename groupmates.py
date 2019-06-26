#coding:utf-8
groupmates = [
    {
        "name": u"Vasya",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Anna",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"George",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Valentine",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]
def print_students(students):
    print u"Name".ljust(15), \
          u"Group".ljust(8), \
          u"Age".ljust(8), \
          u"Marks".ljust(20)
    for student in students:
        print student["name"].ljust(15), \
              student["group"].ljust(8), \
              str(student["age"]).ljust(8), \
              str(student["marks"]).ljust(20)
    print "\n"
    
print_students(groupmates)
print("\n")
print(u"Студенты с оценкой выше среднего")
print("\n")
def sort_students(students):
    s=0
    k=0
    for student in students:
        for j in student["marks"]:
            s=s+j
            k=k+1
            
        average=s/k
    for student in students:
        s=0
        k=0
        for z in student["marks"]:
            s=s+z
            k=k+1
        averages=s/k
        if averages > average:
            print (student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20))
    print("\n")       
                      
sort_students(groupmates)
