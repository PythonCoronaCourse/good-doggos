# Good Doggos
Good Doggos is a terminal-based application created for a group excercise in Python programming. 

# How to work

1. Choose one feature from the list below and declare you're going to do it.
2. Create new branch named after the task with `feature/` prefix, e.g. `git checkout -b feature/save-dog`.
3. On that branch create feature according to specification.
4. When you're finished commit changes and push the changes.
5. On github in [repository of the project](https://github.com/PythonCoronaCourse/good-doggos) open [pull request](https://github.com/PythonCoronaCourse/good-doggos/pulls) section. 
6. Choose `New Pull Request` and choose your branch as `compare`, leave master branch as `base`.
7. Inform other participants that you're waiting for code review.
8. After **at least two other participants and the teacher** accept your changes you can merge your branch to the master.

# Features

### DogDBManager

It's the most vital part of the system. It saves and loads the dogs from the
"database", which is the `dogs.txt` file.

It implements three static methods:
- save_dog(dog : Dog)

this method should load all the dogs from the `dogs.txt` file into a list, 
check if the dog with that id already exists, if it does replace it or append
a new dog to that list and save it to the file again. If everything went okay
`True` should be returned.
 
- get_dog(id : int)

this method should return the Dog that has provided id, or None, if such dog doesn't exist.

- get_dogs()

this method should return a list of all the dogs in the database.


**All the other functions should use DogDBManager to acquire the 
data from the database. They should never open `dogs.txt` file themselves.
All the details of implementation are in the docstrings of the functions.**

### add_dog

### adopt_dog

### find_dog

### list_dogs

### report_death

### return_dog