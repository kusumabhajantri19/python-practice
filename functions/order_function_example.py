

#Order Details Function Using Positional, *args and kwargs

def order_details(customer_name, *items, **info):
    print("Customer Name:", customer_name)
    print("Items Ordered:", items)
    print("Additional Info:", info)

# Function Call
order_details(
    "Kusuma",
    "Pizza",
    "Burger",
    payment="Online",
    city="Bangalore"
)