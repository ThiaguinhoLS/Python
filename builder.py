# -*- coding: utf-8 -*-

MINI14 = "1.4GHz Mac mini"

class AppleFactory(object):

    class MacMini14(object):

        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = "Intel HD Graphics 5000"

        def __str__(self):
            info = (
                "Memory : {0} GB".format(self.memory),
                "Hard Disk : {0} GB".format(self.hdd),
                "Graphics Card : {0}".format(self.gpu)
            )
            return "\n".join(info)

    def build_computer(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I don't know how to build {0}".format(model))



class Computer(object):

    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (
            "Memory : {0} GB".format(self.memory),
            "Hard Disk : {0} GB".format(self.hdd),
            "Graphics Card : {0}".format(self.gpu)
        )
        return "\n".join(info)


class ComputerBuilder(object):

    def __init__(self):
        self.computer = Computer("AG23385193")

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer(object):

    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory), self.builder.configure_hdd(hdd), self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


def main():

    engineer = HardwareEngineer()
    engineer.construct_computer(hdd = 500, memory = 8, gpu = "GeForce GTX 650 TI")
    computer = engineer.computer
    print(computer)


if (__name__ == "__main__"):
    factory = AppleFactory()
    mac_mini = factory.build_computer(MINI14)
    print(mac_mini)
    main()
