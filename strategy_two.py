# -*- coding: utf-8 -*-

import pprint
from operator import attrgetter
from collections import namedtuple


if __name__ == '__main__':
	ProgrammingLang = namedtuple('ProgrammingLang', ['name', 'ranking'])
	stats = (('Ruby', 14), ('JavaScript', 8), ('Python', 7), ('Scala', 31), ('Swift', 18), ('Lisp', 23))
	lang_stats = [ProgrammingLang(n, r) for n, r in stats]
	pp = pprint.PrettyPrinter(indent = 5)
	pp.print(sorted(lang_stats, key = attrgetter('name')))
	print()
	pp.print(sorted(lang_stats, key = attrgetter('ranking')))
