# -*- coding: utf-8 -*-

from enum import Enum
from random import randint

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree(object):

    pool = {}

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if obj is None:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('Render a tree of type {0} and age {1} at({2}, {3})'.format(self.tree_type, age, x, y))


def main():
    """Main function"""
    min_age, max_age = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0
    for _ in range(10):
        t_one = Tree(TreeType.apple_tree)
        t_one.render(
            randint(min_age, max_age),
            randint(min_point, max_point),
            randint(min_point, max_point)
        )
        tree_counter += 1
    for _ in range(3):
        t_two = Tree(TreeType.cherry_tree)
        t_two.render(
            randint(min_age, max_age),
            randint(min_point, max_point),
            randint(min_point, max_point)
        )
        tree_counter += 1
    for _ in range(5):
        t_three = Tree(TreeType.peach_tree)
        t_three.render(
            randint(min_age, max_age),
            randint(min_point, max_point),
            randint(min_point, max_point)
        )
        tree_counter += 1
    print('Trees rendered : {0}'.format(tree_counter))
    print('Trees actually created : {0}'.format(len(Tree.pool)))
    t_four = Tree(TreeType.cherry_tree)
    t_five = Tree(TreeType.cherry_tree)
    t_six = Tree(TreeType.apple_tree)

    print('{0} == {1} ? {2}'.format(id(t_four), id(t_five), id(t_four) == id(t_five)))
    print('{0} == {1} ? {2}'.format(id(t_five), id(t_six), id(t_five) == id(t_six)))


if __name__ == '__main__':
    main()
