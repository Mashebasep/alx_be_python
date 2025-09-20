# prompt the user for weather input
weather = input("what is the weather like today? (sunny/rainy/cold): "). lower()
#recommend clthes
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather =="cold":
    print("Make sure to wear a warm coat ad a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    
