# -*- coding: utf-8 -*-


class Human(object):

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hello my name is {0}".format(self.name)


class Dog(object):

    def __init__(self, name):
        self.name = name

    def bark(self):
        return "{0} : Aow ! Aow".format(self.name)



class Adapter(object):

    def __init__(self, obj, **kwargs):
        self._obj = obj
        self.__dict__.update(kwargs)

    def __getattr__(self, attr):
        return getattr(self._obj, attr)

    def original_dict(self):
        return self._obj.__dict__


def main():
    human = Human("Thiago")
    dog = Dog("Rex")
    objects = []
    objects.append(Adapter(human, method = human.speak))
    objects.append(Adapter(dog, method = dog.bark))

    for obj in objects:
        print(obj.method())


if __name__ == '__main__':
    main()
