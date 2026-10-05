order_amount = float(input("Enter the order amount: "))
available_stock = int(input("Enter the available stock: "))
requested_quantity = int(input("Enter the requested quantity: "))
member_status = input("Enter the member status (True/False): ").strip().lower()
if requested_quantity <= 0 or requested_quantity > available_stock:
    order_amount = 0
    print("The order cannot be processed due to invalid quantity.")
else:
    if member_status == "true" and order_amount >= 500:
        discount_rate = 0.10
        print("The order is approved with a %10 discount.")
    else:
        discount_rate = 0
        print("The order is approved with no discount.")
    final_price = order_amount * (1 - discount_rate)
    print(f"The final price for the order is: {final_price:.2f} TRY.")




