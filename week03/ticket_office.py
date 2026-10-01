total_ticket = 0
free_ticket = 0
total_price = 0
while True:
    customer_name = input("Customer name (or q to quit): ")
    if customer_name == "q" or customer_name == "Q":
      break
    customer_age = int(input("Age: "))
    if customer_age < 0 or customer_age > 120:   
        print("Invalid age.")
        continue
    day = input("Day (weekday/weekend): ").strip().lower()
    if day != "weekend" and day != "weekday":
        print("Invalid day.")
        continue
    if day == "weekend":
        ticket_price = 250
    elif day == "weekday":
        ticket_price = 200
    student = input("Student (yes/no): ").strip().lower()
    if student != "yes" and student != "no":
        print("Please answer yes or no.")
        continue
    if customer_age < 6:
        free_ticket += 1
        ticket_price = 0
        category = "Free"
    elif customer_age >= 65:
        ticket_price = ticket_price*0.5
        category = "Senior"
    elif 6 <= customer_age <= 12:
        ticket_price = ticket_price*0.6
        category = "Child"
    elif customer_age <= 25 and student == "yes":
        ticket_price = ticket_price*0.7
        category = "Student"
    else:
        category = "Standard"
    total_ticket += 1
    total_price += ticket_price
    print(f"{customer_name}: {ticket_price:.2f} TRY ({category})")
if total_ticket == 0:
    print("No tickets sold.")
else:
    print(f"Tickets sold: {total_ticket}")
    print(f"Total revenue: {total_price:.2f} TRY")
    print(f"Average price: {(total_price / total_ticket):.2f} TRY")
    print(f"Free tickets: {free_ticket}") 