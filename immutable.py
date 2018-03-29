

class Immutable(tuple):

    def __new__(cls, a, b):
        return super(Immutable, cls).__new__(cls, (a, b))

    @property
    def a(self):
        return self[0]

    @property
    def b(self):
        return self[1]

    def __str__(self):
        return "<Immutable {0}, {1}>".format(self.a, self.b)

    def __setattr__(self, attr, value):
        raise TypeError()

    def __delattr__(self, attr):
        raise TypeError()



from collections import namedtuple


Immutable = namedtuple("Immutable", ["a", "b"])

    
