
pizzas = {
    "S" : 15,
    "M" : 20,
    "L" : 25
}

toppings = {
    "pepperoni_S" : 2,
    "pepperoni_M" : 3,
    "pepperoni_L" : 3,
    "extra_cheese" : 1
}

class InvalidError(BaseException):
    print("Invalid input. Please try again.")


valid_choice = ["Y", "N"]

print("Welcome to python pizza deliveries")
size = input("What size pizza do you want? S, M or L?")
if size not in pizzas.keys():
    raise InvalidError
pepperoni = input("Do you want pepperoni on your pizza? Y or N?")
if pepperoni not in valid_choice:
    raise InvalidError
extra_cheese = input("Do you want extra cheese? Y or N?")
if extra_cheese not in valid_choice:
    raise InvalidError

if pepperoni == "N":
    if extra_cheese == "N":
        price = pizzas[size]
    else:
        price = pizzas[size] + toppings["extra_cheese"]

else:
    if extra_cheese == "N":
        price = pizzas[size] + toppings[f"pepperoni_{size}"]
    else:
        price = pizzas[size] + toppings[f"pepperoni_{size}"] + toppings["extra_cheese"]

print(price)




