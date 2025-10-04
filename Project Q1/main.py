from pyscript import display

owner = "Miguel Buo" # name
year_founded = "2025" # integer
popular_item_price1 = "Potatonado - ₱150.50" # floating-point
popular_item_price2 = "Fries w/o toppings - ₱100.50" # floating-point
popular_item_price3 = "Fries w toppings - ₱125.50" # floating-point
common_allergens = "Warning for those with allergies - food contains: Gluten, Dairy, and Soy" # list
business_hours = "8:00am - 9:30pm" # tuple
has_delivery=(False) # Boolean

# everything from here on out is display
display(owner,  target= "ownerName")
display(year_founded, target= "yearFounded")
display(popular_item_price1, target= "popularitemPrice")
display(popular_item_price2, target= "popularitemPrice")
display(popular_item_price3, target= "popularitemPrice")
display(common_allergens, target= "common_Allergens")
display(business_hours, target= "businessHours")
display(has_delivery, target= "hasDelivery")