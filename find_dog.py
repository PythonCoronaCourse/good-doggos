from dog_db_manager import Dog
from dog_db_manager import DogDBManagerMock


def find_dog():
    """ Take the id or the name of the dog from the user, find the dog in the database and
    print the dog's details or info about absence of given dog in the database. If the name
    is given and there's more than one dog with that name, print info about all of them. """
    id_name = int(input("Wpisz 0 - ID, 1 - imię: "))
    if id_name == 0:
        your_dogo = int(input("Podaj id pieska: "))
        dog = DogDBManagerMock.get_dog(your_dogo)
        if DogDBManagerMock.get_dog(your_dogo):
            print(f"{dog.id}. {dog.name}, {dog.status}")
        else:
            print("Nie ma takiego pieska")
    elif id_name == 1:
        your_dogo = input("Podaj imię pieska: ")
        dogs = DogDBManagerMock.get_dogs()
        for dog in dogs:
            if dog.name == your_dogo:
                print(f"{dog.id}. {dog.name}, {dog.status}")
    else:
        print("Liczba rózna od 0 i rózna od 1")