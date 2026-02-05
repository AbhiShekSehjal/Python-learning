import json

students = [
    {"name": "Abhi", "marks": [100, 100, 100]},
    {"name": "Shivam", "marks": [12, 80, 64]},
    {"name": "Nikhil", "marks": [53, 20, 20]},
    {"name": "Ravi", "marks": [30, 25, 28]},
]


def calculate_average(marks):
    try:
        if not marks:
            return 0
        return sum(marks) / len(marks)
    except TypeError:
        print("Marks must be numbers only")
        return 0


def student_status(marks):
    avg = calculate_average(marks)

    if avg >= 33:
        return "Pass"
    else:
        return "Fail"


def student_grade(marks):
    avg = calculate_average(marks)

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


def analyze_single_student(student):
    marks = student["marks"]
    avg = calculate_average(marks)

    return {
        "Average": avg,
        "Status": "Pass" if avg >= 33 else "Fail",
        "Grade": student_grade(marks),
    }


def find_topper(students):
    max_avg = 0
    topper = ""

    for student in students:
        avg = calculate_average(student["marks"])

        if avg > max_avg:
            max_avg = avg
            topper = student["name"]

    return topper, max_avg


def validate_student(student):
    if "name" not in student or "marks" not in student:
        return False

    if not isinstance(student["marks"], list):
        return False

    return True


def build_result_dict(students):
    result = {}

    for student in students:
        if not validate_student(student):
            print("Invalid student data:", student)
            continue

        result[student["name"]] = analyze_single_student(student)

    return result


def save_result_to_json(data, filename="result.json"):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Successfuly saved data into:", filename)

    except IOError:
        print("File error occurred while saving JSON")


def show_menu():
    print("\n===== STUDENT RESULT SYSTEM =====")
    print("1. Show All Students Result")
    print("2. Show Topper")
    print("3. Show Failed Students")
    print("4. Save Result to JSON")
    print("5. Exit")


def show_all_results(students):
    print("\n-------------------")
    print("All Students")
    print("-------------------")

    for student in students:
        result = analyze_single_student(student)

        print("\nStudent:", student["name"])
        print("Average:", result["Average"])
        print("Status:", result["Status"])
        print("Grade:", result["Grade"])


while True:
    show_menu()
    request = input("Enter your choice (1-5): ")

    if request == "1":
        show_all_results(students)

    elif request == "2":
        topper, max_avg = find_topper(students)
        print("\n-------------------")
        print("Topper:", topper)
        print("Average:", max_avg)
        print("-------------------")

    elif request == "3":
        failed = get_failed_students(students)
        print("\n-------------------")
        print("Failed student : ", failed)
        print("-------------------")

    elif request == "4":
        student_list = build_result_dict(students)
        save_result_to_json(student_list)

    elif request == "5":
        print("Exiting program. Bye")
        break

    else:
        print("Invalid choice. Try again.")
