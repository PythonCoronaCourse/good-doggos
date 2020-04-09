from dog_db_manager import Dog


def add_dog():
    """ Get the dog data, create new Dog object and save it. """
    print('~~Dodaj nowego pieska do bazy~~')
    name = input('nazwa pieska: ')
    is_adopted = bool(int(input('status pieska: 0 - do adopcji, 1 - adoptowany ')))
    year = input('podaj rok urodzenia pieska: ')
    if is_adopted:
        status = 'adopted'
    else:
        status = 'for adoption'


    dog = Dog(name, status, year)
    dog.save()

    print('~~piesek dodany do bazy~~')
    print(f"{dog.id}. {dog.name}, {dog.status}")
