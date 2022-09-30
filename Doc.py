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
