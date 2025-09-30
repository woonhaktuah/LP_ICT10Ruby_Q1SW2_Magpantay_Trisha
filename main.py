from pyscript import display 
#Shop Ordering System Using Python Data Types 

#String Data Type
shop_name = "CartNextDoor"
owner_name = "Anika Magpantay"

#Integer Data Type
year_since = 2025

#FLoat Data Type
tax_rate = 0.08 

#Boolean Data Type 
has_delivery = True
has_pickup = False
has_cash_on_delivery = False 

#List Data Types
product_names = ["WHO!", "WHY..", "HOW?", "19.99", "No Genre"]

#Tuple Data Types 
business_hours = ("7:00 AM", "10:00 PM")

#Dictionary Data Typesalbums 
albums = {
    "WHO!": 399.00,
    "WHY..": 599.00,
    "HOW?": 699.00,
    "19.99": 499.00,
    "No Genre": 499.00,
}

#Set Data Types
common_inclusions = {"photocards", "postcards", "posters"}

#Display the shop information
display(shop_name, target="name1")
display(f"Owned by: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Album Pricelist:", target="heading1")

#Display album items
display(product_names[0], target="item1")
display(f"₱{albums['WHO!']:.2f}", target="price1")
display(product_names[1], target="item2")
display(f"₱{albums['WHY..']:.2f}", target="price2")
display(product_names[2], target="item3")
display(f"₱{albums['HOW?']:.2f}", target="price3")
display(product_names[3], target="item4")
display(f"₱{albums['19.99']:.2f}", target="price4")
display(product_names[4], target="item5")
display(f"₱{albums['No Genre']:.2f}", target="price5")

#Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="opening_hours")
display(f"Delivery Available", target="orderType")