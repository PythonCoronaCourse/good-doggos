# It's the most vital part of the system. It saves and loads the dogs from the "database", which is the dogs.txt file.
#
# It implements three static methods:
#
# save_dog(dog : Dog)
# this method should load all the dogs from the dogs.txt file into a list, check if the dog with that id already exists, if it does replace it or append a new dog to that list and save it to the file again. If everything went okay True should be returned.
#
# get_dog(id : int)
# this method should return the Dog that has provided id, or None, if such dog doesn't exist.
#
# get_dogs()
# this method should return a list of all the dogs in the database.


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
        DogDBManager.save_dog(self)


class DogDBManager:

    @staticmethod
    def __read_db():
        return open("dogs.txt", "r")

    @staticmethod
    def __append_db():
        return open("dogs.txt", "a")

    @classmethod
    def save_dog(cls, dog): # dodaje nowego psa
        cls.__append_db().write("\n" + f"{dog.name},{dog.year_of_birth},{dog.status}")

    @classmethod
    def get_dog(cls, id): # wyciaga z bazy pieska za pomoca jego id; id to nr linijki w DB
        line = cls.__read_db().readlines()[id - 1]
        return cls._serialize_dog(line)

    @classmethod
    def get_dogs(cls):
        dogs = []
        for line in cls.__read_db().readlines():
            dogs.append(cls._serialize_dog(line))
        return dogs

    @staticmethod
    def _serialize_dog(dog_line):
        params = dog_line.split(",")
        return Dog(*params) # *params to to samo co params[0], params[1], params[2]


