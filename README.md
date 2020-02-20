![Holberton school logo](https://www.denverslocksmiths.com/wp-content/uploads/2018/04/airbnblogo.png)
# AirBnB clone Project
## Description
This project intends to create a clone of the airbnb website. This repository contains the files of a command interpreter that is used in the back-end to manipulate user creation and edition.

**The Console**
The console will help us:
* Creating a new object (ex: a new User or a new Place)
* Retrieving an object from a file, a database etc…
* Doing operations on objects (count, compute stats, etc…)
* Updating attributes of an object
* Destroying an object

## Installation
```
$ git clone 
$ cd AirBnB_clone https://github.com/BrianFs04/AirBnB_clone.git
$ ./console.py
```
## Usage
There are two ways to use the console, we have **interactive** mode and no **interactive** mode;
To use the console in interactive mode you just need to execute the console and you are going to see a screen that is ready to receive commands, to exit this mode use the command **quit**.
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) create BaseModel
23vasf1l-2135-451f-87b6-760505c25901
(hbnb)
```
In no-interactive mode you will need to use a pipeline to place the command that you want to execute.
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
```
$ ./console.py echo "create BaseModel" | ./console.py
(hbnb)
s28sdcf1-r7e1-8f29-5092-9a012030e3ga
(hbnb)
```
### Console commands

| Command | Simple Usage             |
| ------- | ------------------------ |
| Quit    | Quit the console          |
| Help    | Display information |
| Create  | Create New object        |
| Show    | Show the object          |
| All     | Display all objects      |
| Update  | Update objects           |
| Destroy | Destroy Objects          |

### Unittest

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory:

   `$ python3 -m unittest discover -v ./tests/`


## Authors
* **Felipe Londoño** - [felipemontes](https://github.com/felipemontes) 

* **Brayan Florez** - [BrianFs04](https://github.com/BrianFs04) 
