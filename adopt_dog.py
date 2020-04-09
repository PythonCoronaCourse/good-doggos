from dog_db_manager import DogDBManagerMock

def adopt_dog():
    """ Take the id of the dog from the user (deal with the incorrect id), change the
    status of the correlating dog to 'adopted', save it and display it's details. """
    adoptowany = int(input("Podaj nr ID, aby zgłosić adopcję pjemska: " ))
    dog = DogDBManagerMock.get_dog(adoptowany)
    dog.status = "adopted"
    dog.save()
    print(dog.name, "adoptowanyy!!!!!!")
    print(f"{dog.id}. {dog.name}, {dog.status}")


