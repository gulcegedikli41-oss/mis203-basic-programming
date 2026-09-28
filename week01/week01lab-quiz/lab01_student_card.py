name = input("Enter your name:")
student_ID = int(input("Enter your student ID:"))
department = input("Enter your department:")
github_username = input("Enter your GitHub username:")
programming_goal = input("Enter your programming goal:")
student_information = [f"---Student Card---", f"{name}", f"{student_ID}", f"{department}", f"{github_username}", f"{programming_goal}"]
for student_card in student_information:
    print(student_card)
