print("Band Name Generator")
city = input("\nWhat is the name of the city you grew up in?\n")
animal = input("\nWhat is your favorite animal?\n")

if animal.lower()[-1] != "s":
    animal = animal + "s"

print("\nYour band name could be called The " + city.capitalize() + " " + animal.capitalize() + ".")