#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutComprehension(Koan):


    def test_creating_lists_with_list_comprehensions(self):
        meal = ['rice','dal','aaloo-matar','matar-paneer','mix-veg']

        comprehension = [delicacy.capitalize() for delicacy in meal]

        self.assertEqual(__, comprehension[0])
        self.assertEqual(__, comprehension[2])

    def test_filtering_lists_with_list_comprehensions(self):
        meal = ['sandwich','burger','dhuska','malpua','jalebi']

        comprehension = [delicacy for delicacy in meal if len(delicacy) > 6]

        self.assertEqual(__, len(meal))
        self.assertEqual(__, len(comprehension))

    def test_unpacking_tuples_in_list_comprehensions(self):
        list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
        comprehension = [ skit * number for number, skit in list_of_tuples ]

        self.assertEqual(__, comprehension[0])
        self.assertEqual(__, len(comprehension[2]))

    def test_double_list_comprehension(self):
        list_of_parantha = ['aaloo-parantha', 'gobhi-parantha','methi-parantha']
        list_of_rice = ['fried rice','saada rice', 'veg biryani']


        comprehension = [ '{0} and {1}'.format(parantha, meal) for parantha in list_of_paranthas for meal in list_of_meals]


        self.assertEqual(__, len(comprehension))
        self.assertEqual(__, comprehension[0])

    def test_creating_a_set_with_set_comprehension(self):
        comprehension = { x for x in 'aabbbcccc'}

        self.assertEqual(__, comprehension)  # rememeber that set members are unique

    def test_creating_a_dictionary_with_dictionary_comprehension(self):
        dict_of_weapons = {'first': 'fear', 'second': 'surprise',
                           'third':'ruthless efficiency', 'forth':'fanatical devotion',
                           'fifth': None}

        dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

        self.assertEqual(__, 'first' in dict_comprehension)
        self.assertEqual(__, 'FIRST' in dict_comprehension)
        self.assertEqual(__, len(dict_of_weapons))
        self.assertEqual(__, len(dict_comprehension))
