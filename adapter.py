# -*- coding: utf-8 -*-

class Computer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "The {0} computer".format(self.name)

    def execute(self):
        return "executes a program"

    

class Synthesizer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "The {0} synthesizer".format(self.name)

    def play(self):
        return "is playing an electronic song"



class Human(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{0} the human".format(self.name)

    def speak(self):
        return "says hello"


class Adapter(object):

    def __init__(self, obj, adapted_method):
        self.obj = obj
        self.__dict__.update(adapted_method)

    def __str__(self):
        return str(self.obj)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


def main():
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    objects.append(Adapter(synth, dict(execute = synth.play)))
    human = Human("Bob")
    objects.append(Adapter(human, dict(execute = human.speak)))
    for i in objects:
        print("{0} {1} {2}".format(str(i), i.execute(), i.name))


if (__name__ == "__main__"):
    main()
        
