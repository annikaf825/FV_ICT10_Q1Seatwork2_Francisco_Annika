restaurant_name = "Fayette"              
owner_name = "Annika Francisco"           
year_established = 2025                   
popular_item_price = 100.0               
has_delivery = True                     
product_names = ["Carbonara", "French Toast", "Barbecue"]  
business_hours = {"open": "9:00 AM", "close": "9:00 PM"}   
menu_prices = {                           
    "Carbonara": 100,
    "French Toast": 130,
    "Barbecue": 99,
    "Braised Chicken": 210,
    "Beef Stew": 230
}
common_allergens = ["Peanuts", "Dairy", "Gluten"]  
tax_rate = 0.12                         

from js import document


document.querySelector("#restaurant_name").innerHTML = restaurant_name
document.querySelector("#owner_name").innerHTML = f"Owner: {owner_name} (Since {year_established})"


menu_list = document.querySelector("#menu_list")
menu_list.innerHTML = ""  # clear
for item, price in menu_prices.items():
    li = document.createElement("li")
    li.textContent = f"{item} - ₱{price}"
    menu_list.appendChild(li)

document.querySelector("#hours").innerHTML = f"Opening Hours: {business_hours['open']} to {business_hours['close']}"
document.querySelector("#delivery").innerHTML = "Delivery Available" if has_delivery else "No Delivery"
document.querySelector("#allergens").innerHTML = "Allergens: " + ", ".join(common_allergens)
document.querySelector("#tax").innerHTML = f"Tax Rate: {tax_rate*100:.0f}%"