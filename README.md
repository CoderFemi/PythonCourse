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

## Data Types
- Primitive Types: Primitive types are String, Integer, Float and Boolean. Indexing of strings is known as `subscripting`.

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

## Modules
Python has built-in modules which are imported with the `import` keyword. An example is the random module. It has the `randint(int1, int2)` method which generates a random integer between two numbers. Also the `random()` method which generates a float between 0 and 1. random.shuffle() shuffles items in a list, and random.choice() randomly selects an item from a list or string.
Custom modules are defined by importing user-defined files in the same manner.

## Data Structures
* Lists: These are the equivalent of JS arrays. An item's index is also called an `offset`. A positive index accesses items from the beginning of the list. A negative index accesses items from the end of the list. A lot of methods are available for manipulating list items.