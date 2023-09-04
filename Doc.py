with function :
**************
In Python, the `with` statement is used for handling context managers, which are objects that define a `__enter__()` and `__exit__()` method. These methods are used to set up and tear down a context for a block of code, respectively. The `with` statement allows you to easily work with resources that need to be acquired and released around a block of code, such as file handles, sockets, or database connections. It helps to simplify the code, reduce the chance of bugs, and improve the readability.

The main usage of the `with` statement is to ensure that the resource is properly acquired and released, while handling exceptions correctly.

Here is an example of how to use `with` when working with a file:

```python
with open('file.txt', 'r') as file:
    data = file.read()
    # Do something with data

# file is automatically closed after this block, even if an exception occurs
```

In this example, the `open()` function returns a file object, which is a context manager. When the `with` statement is executed, the `__enter__()` method is called, which opens the file. After the block of code indented under the `with` statement is executed, the `__exit__()` method is called, which closes the file. The file will be closed even if an exception occurs within the block, ensuring that resources are not leaked and the file is closed properly.

You can also use multiple context managers in one `with` statement:

```python
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    # Do operations with input_file and output_file
    # Both files will be properly closed after the block.

Continuing with another example, let's use `with` in conjunction with a database connection to commit or rollback transactions:

Suppose we have a method `get_database_connection()` returning a connection object (which is a context manager) to interact with a database. We can use the `with` statement to make sure the connection is properly closed and the transaction is either committed or rolled back, depending on whether an exception occurs.

```python
def add_record_to_database(record):
    with get_database_connection() as connection:
        cursor = connection.cursor()
        try:
            # Perform database operations using cursor
            cursor.execute("INSERT INTO my_table (field1, field2) VALUES (?, ?)", (record.field1, record.field2))
            # commit() will be called when exiting the 'with' block if no exception was raised. 
        except Exception as e:
            # rollback() will be called when exiting the 'with' block if an exception was raised.
            print("Error inserting record:", e)
            raise
```

In this example, `get_database_connection()` provides a connection object which has `__enter__()` and `__exit__()` methods for managing database transactions. The `__enter__()` method starts a new transaction, and the `__exit__()` method either commits the transaction if the block of code executed successfully or rolls back the transaction if an exception occurred.

By using the `with` statement, we can ensure that the database connection is properly handled, and the correct transaction management is applied, without having to manually call commit() or rollback() in every possible code path. This simplifies the code, reduces the chance of bugs, and improves readability.





Composition:
***********
# Classes that contain objects of other classes are usually referred to as composites, where classes that are used to create more 
# complex types are referred to as components.


class DirectoryTree:
    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)



# The leading underscore character (_) in the name _TreeGenerator is a commonly used Python convention. It implies that the class is 
# nonpublic, which means that you don’t expect this class to be used from outside its containing module, rptree.py.

# This same convention applies to nonpublic methods and attributes, which you don’t want to be used from outside the containing class. 
# Typically, you start defining attributes as nonpublic and make them public when needed. See PEP 8 for further details on this convention.



>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'


Lambda :
*******

>>> def identity(x):
...     return x

identity() takes an argument x and returns it upon invocation.

In contrast, if you use a Python lambda construction, you get the following:

>>> lambda x: x

In the example above, the expression is composed of:

    The keyword: lambda
    A bound variable: x
    A body: x


sorted() With a key Argument :
*****************************
# One of the most powerful components of sorted() is the keyword argument called key. This argument expects a function to be passed to it,
# and that function will be used on each value in the list being sorted to determine the resulting order.
# To demonstrate a basic example, let’s assume the requirement for ordering a specific list is the length of the strings in the list,
# shortest to longest. The function to return the length of a string, len(), will be used with the key argument:

>>> word = 'paper'
>>> len(word)
5
>>> words = ['banana', 'pie', 'Washington', 'book']
>>> sorted(words, key=len)
['pie', 'book', 'banana', 'Washington']

# The resulting order is a list with a string order of shortest to longest. The length of each element in the list is determined by len() and then returned in ascending order.

# Let’s return to the earlier example of sorting by first letter when the case is different. key can be used to solve that problem by converting the entire string to lowercase:

>>> names_with_case = ['harry', 'Suzy', 'al', 'Mark']
>>> sorted(names_with_case)
['Mark', 'Suzy', 'al', 'harry']
>>> sorted(names_with_case, key=str.lower)
['al', 'harry', 'Mark', 'Suzy']

# The output values have not been converted to lowercase because key does not manipulate the data in the original list. 
# During sorting, the function passed to key is being called on each element to determine sort order, but the original values 
# will be in the output.
# There are two main limitations when you’re using functions with the key argument.
# First, the number of required arguments in the function passed to key must be one. 

# The example below shows the definition of an addition function that takes two arguments. When that function is used in key on a list 
# of numbers, it fails because it is missing a second argument. Each time add() is called during the sort, it is only receiving one 
# element from the list at a time:

>>> def add(x, y):
...     return x + y
... 
>>> values_to_add = [1, 2, 3]
>>> sorted(values_to_add, key=add)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 1 required positional argument: 'y'

# The second limitation is that the function used with key must be able to handle all the values in the iterable. For example, y
# ou have a list of numbers represented as strings to be used in sorted(), and key is going to attempt to convert them to numbers using int. 
# If a value in the iterable can’t be cast to an integer, then the function will fail:

>>> values_to_cast = ['1', '2', '3', 'four']
>>> sorted(values_to_cast, key=int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'four'

# Each numeric value as a str can be converted to int, but four can’t. This causes a ValueError to be raised and explain that four can’t 
# be converted to int because it is invalid.


Using Python’s enumerate() :
**************************
# You can use enumerate() in a loop in almost the same way that you use the original iterable object. 
# Instead of putting the iterable directly after in in the for loop, you put it inside the parentheses of enumerate(). 
# You also have to change the loop variable a little bit, as shown in this example:

>>> for count, value in enumerate(values):
...     print(count, value)
...
0 a
1 b
2 c

# When you use enumerate(), the function gives you back two loop variables:
    # The count of the current iteration
    # The value of the item at the current iteration

# Just like with a normal for loop, the loop variables can be named whatever you want them to be named. You use count and value in this example, 
# but they could be named i and v or any other valid Python names.
# With enumerate(), you don’t need to remember to access the item from the iterable, and you don’t need to remember to advance the index
# at the end of the loop. Everything is automatically handled for you by the magic of Python!
# Technical Details: The use of the two loop variables, count and value, separated by a comma is an example of argument unpacking.
# This powerful Python feature will be discussed further a little later in this article.
# Python’s enumerate() has one additional argument that you can use to control the starting value of the count. By default,
# the starting value is 0 because Python sequence types are indexed starting with zero. In other words, when you want to retrieve the
# first element of a list, you use index 0:

>>> print(values[0])
a

# You can see in this example that accessing values with the index 0 gives the first element, a. However, there are many times when you 
# might not want the count from enumerate() to start at 0. For instance, you might want to print a natural counting number as an output 
# for the user. In this case, you can use the start argument for enumerate() to change the starting count:

>>> for count, value in enumerate(values, start=1):
...     print(count, value)
...
1 a
2 b
3 c

# In this example, you pass start=1, which starts count with the value 1 on the first loop iteration. Compare this with the previous 
# examples, in which start had the default value of 0, and see whether you can spot the difference.




virtaalenv :
***********

virtualenv -p python3 .venv
source .venv/bin/activate
deactivate