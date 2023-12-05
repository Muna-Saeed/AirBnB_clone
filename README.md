# AirBnB Clone Project

## Project Description

This project is an AirBnB clone, aiming to replicate some of the functionalities of the popular AirBnB website. The focus is on building a web application with features such as a command interpreter, HTML/CSS templating, database storage, API integration, and more.

## Command Interpreter Description

The command interpreter is a crucial component of the project. It allows users to manage objects within the AirBnB application. With the command interpreter, you can perform operations such as creating new objects, retrieving objects from files or databases, executing operations on objects, updating object attributes, and destroying objects.

1. Clone the repository:

   ```shell
   git clone https://github.com/Muna-Saeed/AirBnB_clone.git
   ```
2. Navigate to the project directory:

```shell
cd AirBnB_clone
```
### How to Start the Command Interpreter

To start the command interpreter, run the `console.py` script.

```bash
$ ./console.py
```

### How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands:

- `create`: Create a new object (e.g., User, Place).
- `show`: Show details of a specific object.
- `destroy`: Destroy an object.
- `all`: Display all objects.
- `update`: Update attributes of an object.
- `quit`: Exit the command interpreter.

### Examples

```bash
$ ./console.py
(hbnb) create User
9d0ae187-197e-42cd-b5d7-33c5f2a8f1a3
(hbnb) show User 9d0ae187-197e-42cd-b5d7-33c5f2a8f1a3
[User] (9d0ae187-197e-42cd-b5d7-33c5f2a8f1a3) {'id': '9d0ae187-197e-42cd-b5d7-33c5f2a8f1a3', 'created_at': '2023-01-01T12:00:00', 'updated_at': '2023-01-01T12:00:00'}
(hbnb) quit
$
```
