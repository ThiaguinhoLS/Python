# -*- coding: utf-8 -*-

from enum import Enum
import time

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")
STEP_DELAY = 3


class Pizza(object):

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = list()

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print("Preparing the {0} dough of your {1} ...".format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print("Done with the {0} dough".format(self.dough.name))


class MargaritaBuilder(object):

    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("Adding the tomato sauce to your margarita ...")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("Done with the tomato sauce")

    def add_topping(self):
        print("Adding the topping (double mozzarella, oregano) to your margarita")
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("Done with the topping (double mozzarella, oregano)")

    def bake(self):
        self.progress = PizzaProgress.baking
        print("baking your margarita for {0} seconds".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("Your margarita is ready")


class CreamyBaconBuilder(object):

    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("Adding the creme fraiche sauce to your creamy bacon")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print("Done with the creme fraiche sauce")

    def add_topping(self):
        print("Adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon")
        self.pizza.topping.append([t for t in (
            PizzaTopping.mozzarella,
            PizzaTopping.bacon,
            PizzaTopping.ham,
            PizzaTopping.mushrooms,
            PizzaTopping.red_onion,
            PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print("Done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)")

    def bake(self):
        self.progress = PizzaProgress.baking
        print("Baking your creamy bacon for {0} seconds".format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("Your creamy bacon is ready")


class Waiter(object):

    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input("What pizza would you like, [M]argarita or [C]reamy bacon ?: ")
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as error:
        print("Sorry, only margarita (key M) and creamy bacon (key C) are available")
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m = MargaritaBuilder, c = CreamyBaconBuilder)
    valid_input = False
    while (not valid_input):
        valid_input, builder = validate_style(builders)
    print("")
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print("")
    print("Enjoy your {0}!".format(pizza))


if __name__ == '__main__':
    main()
