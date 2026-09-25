total_student = 0
total_score = 0
while True:
    name = input("Enter student name (or q to quit):")
    if name == "q":
        break
    else:
        score = float(input("Enter score:"))
        if score < 0 or score > 100:
            print("Invalid score. Please enter a number between 0 and 100.")
            continue
        else:
            if 90 <= score <= 100:
                letter_grade = "A"
            if 80 <= score <= 89:
                letter_grade = "B"
            if 70 <= score <= 79:
                letter_grade = "C"
            if 60 <= score <= 69:
                letter_grade = "D"
            if 0 <= score <= 59:
                letter_grade = "F"
            print(f"{name}: {score} -> {letter_grade}")
    total_student = total_student + 1
    total_score = total_score + score 
if total_student == 0:
    print("No students entered.")
else:
    print(f"Total students: {total_student}")
    print(f"Average score: {total_score/total_student:.2f}")
