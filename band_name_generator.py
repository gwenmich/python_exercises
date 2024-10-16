def band_name_generator():
    print("Welcome to the band name generator!")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet name?\n")
    print(f"Your band's name is: {city.capitalize()} {pet.capitalize()}")


band_name_generator()