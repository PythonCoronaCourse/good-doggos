class Dog:
    dog_counter = 0

    def __init__(self, name, year_of_birth, status, id=None):
        self.name = name
        self.year_of_birth = year_of_birth
        self.status = status
        if id:
            self.id = id
        else:
            self.id = Dog.dog_counter
            Dog.dog_counter += 1

    def save(self):
        DogDBManagerMock.save_dog(self)


class DogDBManager:
    @staticmethod
    def save_dog(dog):
        """ Add the dog object to the database. """
        pass

    @staticmethod
    def get_dog(id):
        """ Acquire the dog with the given ID from the database. """
        pass

    @staticmethod
    def get_dogs():
        """ Return all the dogs from the database as a list. """
        pass


class DogDBManagerMock:
    @staticmethod
    def save_dog(dog):
        return True

    @staticmethod
    def get_dog(id):
        return Dog("Psiulek", 2010, "for adoption")

    @staticmethod
    def get_dogs():
        """ Return all the dogs from the database as a list. """
        return [Dog("Tali", 2009, "adopted"), Dog("Baksiu", 2010, "for adoption")]
