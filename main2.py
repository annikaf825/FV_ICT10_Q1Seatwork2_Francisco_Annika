from pyscript import display

# String
restaurant_name = "Fayette"

# String
owner_name = "Annika Francisco"

# Integer (year)
year_established = 2025

# String (peso with symbol)
popular_item_price = "₱100"

# Boolean
has_delivery = True

# List of Strings
product_names = ["Carbonara", "French Toast", "Barbecue"]

# String
business_hours = "9:00 AM to 9:00 PM"

# Dictionary
menu_prices = {
    "Carbonara": "₱100",
    "French Toast": "₱130",
    "Barbecue": "₱99",
    "Braised Chicken": "₱210",
    "Beef Stew": "₱230"
}

# List of Strings
common_allergens = ["Peanuts", "Dairy", "Gluten"]

# Float
tax_rate = 0.12

# Display at least 5 data
display("<h2>Welcome to " + restaurant_name + "!</h2>")
display("<p><b>Owner:</b> " + owner_name + "</p>")
display("<p><b>Established:</b> " + str(year_established) + "</p>")
display("<p><b>Popular Item Price:</b> " + popular_item_price + "</p>")
display("<p><b>Business Hours:</b> " + business_hours + "</p>")
display("<p><b>Has Delivery?</b> " + str(has_delivery) + "</p>")
display("<p><b>Common Allergens:</b> " + ", ".join(common_allergens) + "</p>")