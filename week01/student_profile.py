# Kullanıcıdan istenen 4 bilgiyi alıyoruz
name = input("Enter your name: ")
department = input("Enter your department: ")
age = int(input("Enter your age: "))
career_goal = input("Enter your career goal: ")

# Bilgileri istenilen formatta ekrana yazdırıyoruz
print(f"--- Student Profile --- Name: {name} Department: {department} Age: {age} Career Goal: {career_goal}")
