name = input("Enter your name: ")
department = input("Enter your department: ")
age = int(input("Enter your age: "))
career_goal = input("Enter your career goal: ")
all_information =[f"---Student Profile---", f"Name: {name}", f"Department: {department}", f"Age: {age}", f"Career Goal: {career_goal}"]
for information in all_information:
  print(information)
