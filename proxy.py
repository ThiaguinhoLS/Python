# -*- coding: utf-8 -*-


class LazyProperty(object):

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        print('__get__')
        if not obj:
            return None
        value = self.method(obj)
        print(id(value))
        setattr(obj, self.method_name, value)
        return value


class Test(object):

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('Initializing self._resource is : {0}'.format(self._resource))
        self._resource = tuple(range(5))
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
