# Ques 1


# def is_even(inputValue):
#     if inputValue % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# inputValue = int(input("Enter the number : "))
# result = is_even(inputValue)
# print(result)


# Ques 2


# def average():
#     numbers = []

#     for i in range(5):
#         inputValue = int(input("Enter the numbers : "))
#         numbers.append(inputValue)

#     return sum(numbers) / len(numbers)


# average_call = average()
# print("Average : " , average_call)


# def multiply(num1, num2):
#     return num1 * num2


# result = multiply(5, 6)
# print(result)


# def check_pass(marks):
#     if marks >= 33:
#         return "Pass"
#     else:
#         return "Fail"


# marks = int(input("Enter your marks : "))
# result = check_pass(marks)
# print(result)


# def country(name, country="India"):
#     return name, country


# result = country("Abhishek")
# print(result)


# def find_max_min(numbers):
#     return max(numbers), min(numbers)


# marks = [50, 36, 94, 64]
# maximum, minimum = find_max_min(marks)
# print("Maximum :", maximum)
# print("Minimum :", minimum)


# def count_even(numbers):
#     evenNumbers = []

#     for number in numbers:
#         if number % 2 == 0:
#             evenNumbers.append(number)

#     return len(evenNumbers)


# allNumbers = [10, 60, 52, 25]
# result = count_even(allNumbers)

# print(result)


def student_result(marks):
    avg = sum(marks) / len(marks)
    if avg >= 33:
        return "Pass"
    else:
        return "Fail"


allMarks = [50, 60, 10, 9]
result = student_result(allMarks)
print(result)