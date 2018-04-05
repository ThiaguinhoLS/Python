# -*- coding: utf-8 -*-


import copy

class A(object):

    def __init__(self):
        self.x = 0
        self.message = "Hello"

class B(A):

    def __init__(self):
        A.__init__(self)
        self.y = 1

    def __str__(self):
        return "{0}, {1}, {2}".format(self.x, self.y, self.message)


class C(object):

    def __init__(self):
        self.instance = A()


from collections import OrderedDict

class Book(object):

    def __init__(self, name, authors, price, **kwargs):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(kwargs)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append("{0} : {1}".format(i, ordered[i]))
            if (i == "price"):
                mylist.append("$")
            mylist.append("\n")
        return "".join(mylist)


class Prototype(object):

    def __init__(self):
        self._objects = dict()

    def register(self, identifier, obj):
        self._objects[identifier] = obj

    def unregister(self, identifier):
        del self._objects[identifier]

    def clone(self, identifier, **kwargs):
        found = self._objects.get(identifier, None)
        if (found is None):
            raise ValueError("Incorrect object identifier : {0}".format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(kwargs)
        return obj


def main():

    book_one = Book("Book One", ("T.L", "L.S"), price = 100, publisher = "Editora Érica")
    prototype = Prototype()
    prototype.register("first", book_one)
    book_two = prototype.clone("first", name = "Book Two", edition = 2)
    for book in (book_one, book_two):
        print(book)
    assert book_one != book_two

if __name__ == '__main__':
    main()
