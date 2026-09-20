# mis203-basic-programming
**Name:** *Gülce*
<br>
**Student Number:** *2404109058*
<br>
**Department:** *Management Information Systems*
<br>
**Course Name:** *Basic Programming*
<br>
**AI Tool Used:** *Gemini*
<br>
**Prompt Used:** *Python programlama diline göre name, department, age ve career goal kavramlarını değişken olarak kullanarak kullanıcıdan girdi  isteyen ve bu girdilerin çıktılarını ekrana tek bir satırda f-string içinde çıktının başına ---Student Profile---  metnini ekleyerek yazdıran bir Python kodu yazmanı istiyorum. Kullanıcıdan girdi değişkeninin kendisinin yazıldığı dilde istenmeli ve girdi kullanıcıdan istenirken soru cümlelerinden kaçınılmalıdır; onun yerine   emir cümleleri kullanılmalıdır ve emir cümlelerinde kullanıcının kendisinden girdi istendiği belirtilmelidir.*
<br>
**What did you change ?:** *The input type in the age variable was converted from string to integer, and the outputs were adjusted to sort line by line.*

## First Version
```python
# Kullanıcıdan istenen 4 bilgiyi alıyoruz
name = input("Enter your name: ")
department = input("Enter your department: ")
age = input("Enter your age: ")
career_goal = input("Enter your career goal: ")

# Bilgileri istenilen formatta ekrana yazdırıyoruz
print(f"--- Student Profile --- Name: {name} Department: {department} Age: {age} Career Goal: {career_goal}")
```

## Final Version
```python
name = input("Enter your name: ")
department = input("Enter your department: ")
age = int(input("Enter your age: "))
career_goal = input("Enter your career goal: ")
all_information =[f"---Student Profile---", f"Name: {name}", f"Department: {department}", f"Age: {age}", f"Career Goal: {career_goal}"]
for information in all_information:
  print(information)
```
