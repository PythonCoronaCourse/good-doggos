from dog_db_manager import DogDBManagerMock


def list_dogs():
    """ Get all the dogs from the database (use DogDBManager) and print their details. """
    dogs = DogDBManagerMock.get_dogs()
    for dog in dogs:
        print(f"{dog.id}. {dog.name}, {dog.status}")
