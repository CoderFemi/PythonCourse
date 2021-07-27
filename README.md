# PYTHON COURSE

## Python Built-in Functions
- The print() function is the equivalent to console.log() for JS. It prints output to the console. Using \n prints output on a new line. Using `'''` three single quotes at the beginning and end of a string will make it a multi-line string.
- The input() function prompts a user to enter some data. It is used in conjunction with the print function to perform I/O tasks.
- len() returns the length of a string.
- type() returns the type of the data.
- str() typecasts other data types to a string.
- int() typecasts other data types to an integer.
- float() typecasts other data types to a float.
- round() rounds down a float to a specified number of decimal places. It takes the number, and the desired number of decimal places as arguments. E.g. `round(2.5636222, 2)` returns 2.56.
- The range() function in particular is very useful for creating lists of numbers within a range. It takes in three arguments: the start, the stop, and the step (increment value).

## Variables
The naming convention for python variables uses lowercase separated by underscores, in contrast with JS which uses camel casing.

## Scopes
Python has the same principles for Local and Global scoping as Javascript. However, variables are not block scoped i.e. if statements, for and while loops do not create a separate local scope. Variables are only function scoped. JS on the other hand provides block scoping with the let and const keywords.
*Global variables cannot (should not) be modified within a local scope*. To bypass this, the variable is redeclared as global within the local scope before it can be modified.

## Data Types
- Primitive Types: Primitive types are String, Integer, Float and Boolean. Indexing of strings is known as `subscripting`. `Docstrings` are multiline comments used for documenting code blocks esp. functions.

## Python Operators
- Mathematical operations are basically the same as in JS. A unique operator is the floor division operator `//` which gives the quotient of a division operation. E.g. `4.5 // 2` returns 4 as the quotient.
- f-Strings provide the same functionality as string literals in Javascript. A string can contain variables by simply prepending an f to the string.
- Comparism operators are also the same. `if-else` statements use almost the same syntax. `if-in` statements are used to check for items in a list or string (JS includes() equivalent).
- Logical operators are `and`, `or` and `not`.
- Spacing and indentation have their significance in Python. Indented code below a statement signifies that the block of code is a child of that statement.

## Loops
The while loop and the for-in loop are the two loops used in python. The range() function is used together with the for-in loop to specify iteration limits.

## Functions
Functions are defined in Python with the keyword `def`, a function name, a pair of parentheses followed by a colon. The code to be executed by the function is indented on subsequent lines as a code block.
Python improves on `positional arguments` available in JS. It also has `keyword arguments`. When calling a function, arguments can be assigned values, in any order that is desired.
A function with no return statement returns the value `None` (just like Javascript returns `undefined`.).
* Unlimited Positional Arguments: An unlimited number of arguments can be passed into a function using an asterisk followed by a variable, which is usually args `*args`. When the function is called with arguments, they are outputted in a tuple.
* Unlimited Keyword Arguments: To pass in unlimited keyword arguments, a double asterisk is used as the function parameter followed by a variable, usually denoted as kwargs (short for keyword arguments) `**kwargs`. The arguments are outputted in a dictionary. When kwargs are being assigned to class attributes, it is best to use a get() method to access kwargs dictionary values instead of indexing or the dot notation. Because the latter two will raise an error when a passed-in argument does not exist, but using a getter will simply return `None`.

## Modules
Python has built-in modules which are imported with the `import` keyword. An example is the random module. It has the `randint(int1, int2)` method which generates a random integer between two numbers. Also the `random()` method which generates a float between 0 and 1. random.shuffle() shuffles items in a list, and random.choice() randomly selects an item from a list or string.
Custom modules are defined by importing user-defined files in the same manner.

## Data Structures
* Lists: These are the equivalent of JS arrays. An item's index is also called an `offset`. A positive index accesses items from the beginning of the list. A negative index accesses items from the end of the list. A lot of methods are available for manipulating list items. Slicing is done by simply indexing with a start and end index separated by a colon. A third index argument specifies the increment value for slicing.
* Tuples: These are similar to lists, but are immutable. They are more efficient for time and space complexity. Tuples are sliced the same way as lists.
* Dictionaries are same as in JS, but more flexible in that keys can be any immutable, primitive data type such as a string, integer, boolean. Mutable types such as lists and dictionaries cannot be keys.
  * Sequences are any iterable, ordered data type. This could be a string, list, range or tuple.
* The equivalent of mapping in JS is done with `list comprehensions`. To conditionally create mapped values from another list, the syntax is `new_list = [<new_value> for <value> in list if <condition>]`. This works not only with lists but also with other data types such as strings, dictionaries, tuples. The syntax for dictionaries is `new_dict = [<new_key>:<new_value> for (key, value) in dict.items() if <condition>]` It is modified to return only keys or values depending on the operation desired.

## OOP
OOP provides a lot of improvement over Procedural Programming. Real-life objects are modelled using Classes. In python, classes are named with `PascalCase`, properties are called `attributes`, and methods are the same name, `methods`. To create a new instance of a class, the class is simply called i.e. `new_car = Car()`.
The equivalent of the JS `this` keyword in Python is `self`. The class constructor is defined with a name of `__init__()` taking 'self' as the first argument, followed by other required attributes.
Class methods also have to be defined with a 'self' argument, to always refer to the instance that is calling the method. 
The values of an instance's attributes are called it's `state`.
Class inheritance in Python is done by passing the parent class (super class) as an argument to the child class and in the constructor function, calling `super().__init__()`. Calling the super function is recommended but not strictly required.

## File System
the `open()` method is used to access system files. It takes the file name as the first argument, and the mode as the second, which can be set to either readonly mode - 'r', write mode - 'w' or append mode 'a'. If the specified file doesn't exist a new one is created. `read()` reads from the file. `write()` writes to the file. This normally overwrites what is already in the file. To append to the file instead, `\n` a new line is specified at the beginning of the string. `close()` closes the file. A simpler way to access the file is by using the `with open('<filepath>', <mode>) as <new_file_name>` statement to open the file. Then there is no need to call the `close()` method.
JSON strings are also available in Python by importing the in-built json module. `json.dump(<dict_data>, <file_path.json>, <indent>)` is used to write to a json file. `json.load(<file_path.json)` reads the json file. `json_data.update(<new_data>)` updates the json data.

## Error Handling
The syntax for error handling in Python is as below:
```
try:
    <statement>
except <ErrorType>: # Multiple except clauses are possible.
    <do something>
else:
    <do something if no error>
finally:
    <do something no matter what happens>
```
Throwing an error is done with the `raise` keyword followed by the <ErrorType> or a more general `Exception`.
Golden Nugget: **Only use exception handling when an if-else statement does not suffice**.