from add_dog import add_dog
from adopt_dog import adopt_dog
from find_dog import find_dog
from list_dogs import list_dogs
from return_dog import return_dog
from report_death import report_death

print("Witaj w systemie Good Doggos.")

menu_options = """
By wybrać opcję z listy, wpisz jej numer.
1. Dodaj pieska do bazy.
2. Adoptuj pieska.
3. Wyszukaj pieska.
4. Zobacz listę piesków.
5. Zgłoś zwrot pieska.
6. Zgłoś śmierć pieska.
7. Zamknij program.

"""

while True:
    try:
        option = int(input(menu_options))
    except ValueError:
        pass
    else:
        if option == 1:
            add_dog()
        elif option == 2:
            adopt_dog()
        elif option == 3:
            find_dog()
        elif option == 4:
            list_dogs()
        elif option == 5:
            return_dog()
        elif option == 6:
            report_death()
        elif option == 7:
            break
