# Write your solution here

def print_stars(grades: list, n: int) -> str:
    count = 0
    for grade in grades:
        if grade == n:
            count += 1
    return "*" * count

def get_total_points(exam_points: list, exercise_points: list) -> list:
    total_points = []
    for i in range(len(exam_points)):
        total_points.append(exam_points[i]+exercise_points[i])
    return total_points

def get_grades(exam_points: list, exercise_points: list) -> list:
    grades = []
    total_points = get_total_points(exam_points, exercise_points)
    for i in range(len(exam_points)):
        if exam_points[i] >= 10:
            if total_points[i] >= 15 and total_points[i] <= 17:
                grade = 1
            elif total_points[i] >= 18 and total_points[i] <= 20:
                grade = 2
            elif total_points[i] >= 21 and total_points[i] <= 23:
                grade = 3
            elif total_points[i] >= 24 and total_points[i] <= 27:
                grade = 4
            elif total_points[i] >= 28 and total_points[i] <= 30:
                grade = 5
            else:
                grade = 0
        else:
            grade = 0
        grades.append(grade)
    return grades

def get_pass_percentage(exam_points: list, exercise_points: list) -> float:
    passed = 0
    for i in range(len(exam_points)):
        if exam_points[i] >= 10:
            if exam_points[i]+exercise_points[i] >= 15:
                passed += 1
    return (passed/len(exam_points)) * 100

def get_points_average(exam_points: list, exercise_points: list) -> float:
    points = []
    for i in range(len(exam_points)):
        points.append(exam_points[i]+exercise_points[i])
    return sum(points) / len(points)

def get_exercise_points(exercises_completed: list) -> list:
    exercise_points = []
    for exercises in exercises_completed:
        exercise_points.append(exercises//10)
    return exercise_points

def main():
    exam_points = []
    exercises_completed = []

    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        parts = user_input.split(" ")
        exam_points.append(int(parts[0]))
        exercises_completed.append(int(parts[1]))

    exercise_points = get_exercise_points(exercises_completed)

    print("Statistics:")
    print(f"Points average: {get_points_average(exam_points, exercise_points):.1f}")
    print(f"Pass percentage: {get_pass_percentage(exam_points, exercise_points):.1f}")

    grades = get_grades(exam_points, exercise_points)

    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"{i}: {print_stars(grades, i)}")

main()
