import json


def input_student_data():
    students = []
    n = int(input("Введите количество студентов: "))

    for _ in range(n):
        student = {}
        student["фамилия и инициалы"] = input("Введите фамилию и инициалы: ")
        student["номер группы"] = input("Введите номер группы: ")
        student["успеваемость"] = [float(input(f"Введите оценку {i + 1}: ")) for i in range(5)]
        students.append(student)

    students.sort(key=lambda x: x["номер группы"])
    return students


def display_students(students):
    found_students = False

    for student in students:
        average_grade = sum(student["успеваемость"]) / len(student["успеваемость"])
        if average_grade > 4.0:
            print(f"{student['фамилия и инициалы']}, группа {student['номер группы']}")
            found_students = True

    if not found_students:
        print("Нет студентов с успеваемостью выше 4.0")


def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def load_from_json(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    students_data = input_student_data()
    save_to_json(students_data, 'students.json')

    loaded_data = load_from_json('students.json')
    display_students(loaded_data)
