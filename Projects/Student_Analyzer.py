students = [
    {"name": "Abhi", "marks": [100, 100, 100]},
    {"name": "Shivam", "marks": [12, 80, 64]},
    {"name": "Nikhil", "marks": [53, 20, 20]},
    {"name": "Ravi", "marks": [30, 25, 28]},
]


def calculate_average(marks):
    return sum(marks) / len(marks)


def student_status(marks):
    avg = calculate_average(marks)

    if avg >= 33:
        return "Pass"
    else:
        return "Fail"


def student_grade(marks):
    avg = calculate_average(marks)
    status = student_status(marks)

    if avg >= 80:
        return "A"
    elif avg >= 50:
        return "B"
    elif avg >= 33:
        return "C"
    else:
        return "Fail"


def get_failed_students(students):
    failed = []

    for student in students:
        status = student_status(student["marks"])
        if status == "Fail":
            failed.append(student["name"])

    return failed


def analyze_students(students):

    for student in students:
        avg = calculate_average(student["marks"])
        status = student_status(student["marks"])
        grade = student_grade(student["marks"])

        print("Student : ", student["name"])
        print("Average :", avg)
        print("Status :", status)
        print("Grade :", grade)
        print("-------------")


def find_topper(students):
    max_avg = 0
    topper = ""

    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])

        if avg > max_avg:
            max_avg = avg
            topper = student["name"]

    return topper, max_avg


analyze_students(students)


topper, max_avg = find_topper(students)

print("----------------------------")
print("Topper student is:", topper)
print("Topper's marks:", max_avg)
print("----------------------------")

failed = get_failed_students(students)
print("Failed students:", failed)
