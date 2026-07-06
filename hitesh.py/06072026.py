# Step 1: Create a customer dictionary with name, age, and city
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}
print(customer)
# Step 2: Add email and phone
customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"
print(customer)
# Step 3: Print customer's name and city
print(customer["name"])
print(customer["city"])
# Step 4: Check if "email" exists
get_email = "email" in customer
print(get_email)
# Step 5: Delete the "age" field
del customer["age"]
print(customer)
# Step 6: Print all keys, values, and items
print(customer.keys())
print(customer.values())
print(customer.items())
# Step 7: Remove and print the last inserted item
inserted_item = customer.popitem()
print(inserted_item)
# Step 8: Use .get() to access "membership"
result = customer.get("membership")
print(result)
# Step 9: Update dictionary with "address"
customer["address"] = "221B Baker Street"
print(customer)
# Step 10: Print final dictionary
print(customer)