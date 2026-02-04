# Ques : 1

# students = [
#     {"Name": "Abhi", "Age": 22, "Marks": [12, 50, 64]},
#     {"Name": "Shivam", "Age": 22, "Marks": [12, 90, 80]},
#     {"Name": "Nikhil", "Age": 25, "Marks": [72, 20, 60]},
# ]

# for student in students:
#     marks = student["Marks"]
#     avg = sum(marks) / len(marks)
#     print(student["Name"], ":", avg)



# Ques : 2

# students = [
#     {"Name": "Abhi", "Age": 22, "Marks": [12, 50, 64]},
#     {"Name": "Shivam", "Age": 22, "Marks": [12, 00, 00]},
#     {"Name": "Nikhil", "Age": 25, "Marks": [72, 20, 60]},
# ]

# def count_pass_students(students):
#     count = 0

#     for student in students:
#         if sum(student["Marks"]) >= 33:
#             count += 1
#     return count


# result = count_pass_students(students)
# print("Number of Pass students : ", result)


# Ques : 3

# def topper_name(students):
#     max_avg = 0
#     topper = ""

#     for student in students:
#         avg = sum(student["Marks"]) / len(student["Marks"])
        
#         if avg > max_avg:
#             max_avg = avg
#             topper = student["Name"]
    
#     return topper    


# students = [
#     {"Name": "Abhi", "Age": 22, "Marks": [62, 50, 84]},
#     {"Name": "Shivam", "Age": 22, "Marks": [12, 80, 64]},
#     {"Name": "Nikhil", "Age": 25, "Marks": [53, 20, 94]},
# ]

# result = topper_name(students)
# print("The topper is : ", result)




