#12.1 // task 1
# students = [
#     {"name": "aarav", "marks": 135},
#     {"name": "diya", "marks": 112},
#     {"name": "rohan", "marks": 98},
#     {"name": "kavya", "marks": 144},
#     {"name": "vihaan", "marks": 120},
#     {"name": "ananya", "marks": 85},
#     {"name": "kabir", "marks": 148},
#     {"name": "meera", "marks": 115},
#     {"name": "arjun", "marks": 102},
#     {"name": "ishita", "marks": 129}
# ]

# percentages = list(map(lambda s: round((s["marks"] / 150) * 100, 1), students))
# print("Percentages:", percentages)

# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/12.1.py"'
# Percentages: [90.0, 74.7, 65.3, 96.0, 80.0, 56.7, 98.7, 76.7, 68.0, 86.0]
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

#12.2// task 2
# students = [
#     {"name": "amit", "marks": 135},
#     {"name": "neha", "marks": 112},
#     {"name": "raj", "marks": 98},
#     {"name": "priya", "marks": 144},
#     {"name": "rohit", "marks": 120},
#     {"name": "pooja", "marks": 85},
#     {"name": "karan", "marks": 148},
#     {"name": "sneha", "marks": 115},
#     {"name": "vikas", "marks": 102},
#     {"name": "anjali", "marks": 129}
# ]


# above_75 = list(filter(lambda s: (s["marks"] / 150) * 100 > 75, students))

# print("Count above 75%:", len(above_75))

# print("Names above 75%:")
# for s in above_75:
#     print(s["name"])


# top_3 = sorted(students, key=lambda s: s["marks"], reverse=True)[:3]
# print("Top 3 students:", top_3)

# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/12.1.py"'
# Count above 75%: 6
# Names above 75%:
# amit
# priya
# rohit
# karan
# sneha
# anjali
# Top 3 students: [{'name': 'karan', 'marks': 148}, {'name': 'priya', 'marks': 144}, {'name': 'amit', 'marks': 135}]
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

#12.3//task 3
# from functools import reduce

# fees = [4500, 5000, 3500, 6000, 4000, 5500, 3000, 4800, 5200, 5500]

# total = reduce(lambda a, b: a + b, fees)
# highest = reduce(lambda a, b: a if a > b else b, fees)

# print("Total fees:", total)
# print("Highest fee:", highest)
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> & 'C:\Program Files\Python314\python.exe' '"c:/tops/session 1/12.1.py"'
# Total fees: 47000
# Highest fee: 6000

#12.4//task 4
# students = [
#     {"name": "amit", "marks": 135},
#     {"name": "neha", "marks": 112},
#     {"name": "raj", "marks": 98},
#     {"name": "priya", "marks": 144},
#     {"name": "rohit", "marks": 120},
#     {"name": "pooja", "marks": 85},
#     {"name": "karan", "marks": 148},
#     {"name": "sneha", "marks": 115},
#     {"name": "vikas", "marks": 102},
#     {"name": "anjali", "marks": 129}
# ]

# percentages = list(map(lambda s: round(s["marks"] / 150 * 100, 1), students))



# def assign_grade(p):
#     if p >= 90:
#         return "A+"
#     elif p >= 80:
#         return "A"
#     elif p >= 70:
#         return "B"
#     else:
#         return "C"


# def apply_to_all(func, items):
#     result = []
#     for item in items:
#         result.append(func(item))
#     return result


# names = apply_to_all(lambda s: s["name"].title(), students)


# grace_marks = apply_to_all(lambda s: min(s["marks"] + 5, 150), students)


# grades = apply_to_all(lambda p: assign_grade(p), percentages)


# print("Names:", names)
# print("Grace Marks:", grace_marks)
# print("Grades:", grades)

# Names: ['Amit', 'Neha', 'Raj', 'Priya', 'Rohit', 'Pooja', 'Karan', 'Sneha', 'Vikas', 'Anjali']
# Grace Marks: [140, 117, 103, 149, 125, 90, 150, 120, 107, 134]
# Grades: ['A+', 'B', 'C', 'A+', 'A', 'C', 'A+', 'B', 'C', 'A']
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 
