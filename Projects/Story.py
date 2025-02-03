# Story creater based on user input

def create_story():
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    noun = input("Enter a noun: ")

    story = f"{name} is a {age} year old person from {place}. They are {adjective} and they love to {verb} with their {noun}."
    return story

print(create_story())

