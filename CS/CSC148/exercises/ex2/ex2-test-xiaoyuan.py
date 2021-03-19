"""CSC148 Exercise 2: Inheritance and Introduction to Stacks

=== CSC148 Fall 2016 ===
Diane Horton, David Liu, and Danny Heap
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 2.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""


import unittest
from hypothesis import given
from hypothesis.strategies import integers, text
from math import sqrt

from ex2 import SuperDuperManager, reverse_top_two
from obfuscated_stack import Stack


class SuperDuperManagerTest(unittest.TestCase):

    @given(text(min_size=1), integers(min_value=1))
    def test_new_car_attributes(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_vehicle('Car', id_, fuel)
        self.assertEqual(manager.get_vehicle_fuel(id_), fuel)
        self.assertEqual(manager.get_vehicle_position(id_), (0, 0))

    @given(text(min_size=1), integers(min_value=1))
    def test_new_helicopter_attributes(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_vehicle('Helicopter', id_, fuel)
        self.assertEqual(manager.get_vehicle_fuel(id_), fuel)
        self.assertEqual(manager.get_vehicle_position(id_), (3, 5))

    @given(text(min_size=1), integers(min_value=1))
    def test_new_carpet_attributes(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_vehicle('UnreliableMagicCarpet', id_, fuel)
        self.assertEqual(manager.get_vehicle_fuel(id_), fuel)
        self.assertLessEqual(abs(manager.get_vehicle_position(id_)[0]), 10)
        self.assertLessEqual(abs(manager.get_vehicle_position(id_)[1]), 10)

    @given(text(min_size=1),
           integers(min_value=24),
           integers(min_value=-12, max_value=12),
           integers(min_value=-12, max_value=12))
    def test_car_fuel_needed(self, id_, fuel, new_x, new_y):
        manager = SuperDuperManager()
        manager.add_vehicle('Car', id_, fuel)
        x, y = manager.get_vehicle_position(id_)
        fuel_needed = abs(new_x - x) + abs(new_y - y)
        manager.move_vehicle(id_, new_x, new_y)
        self.assertEquals(fuel - fuel_needed, manager.get_vehicle_fuel(id_))

    @given(text(min_size=1),
           integers(min_value=24),
           integers(min_value=-12, max_value=12),
           integers(min_value=-12, max_value=12))
    def test_helicopter_fuel_needed(self, id_, fuel, new_x, new_y):
        manager = SuperDuperManager()
        manager.add_vehicle('Helicopter', id_, fuel)
        x, y = manager.get_vehicle_position(id_)
        fuel_needed = sqrt(abs(new_x - x)**2 + abs(new_y - y)**2)
        manager.move_vehicle(id_, new_x, new_y)
        self.assertEquals(int(fuel - fuel_needed),
                          manager.get_vehicle_fuel(id_))

    @given(text(min_size=1),
           integers(min_value=24),
           integers(min_value=-12, max_value=12),
           integers(min_value=-12, max_value=12))
    def test_carpet_fuel_needed(self, id_, fuel, new_x, new_y):
        manager = SuperDuperManager()
        manager.add_vehicle('UnreliableMagicCarpet', id_, fuel)
        manager.move_vehicle(id_, new_x, new_y)
        self.assertEqual(fuel, manager.get_vehicle_fuel(id_))

    @given(text(min_size=1),
           integers(min_value=24),
           integers(min_value=-12, max_value=12),
           integers(min_value=-12, max_value=12))
    def test_car_move(self, id_, fuel, new_x, new_y):
        manager = SuperDuperManager()
        manager.add_vehicle('Car', id_, fuel)
        manager.move_vehicle(id_, new_x, new_y)
        self.assertEqual((new_x, new_y), manager.get_vehicle_position(id_))

    @given(text(min_size=1),
           integers(min_value=24),
           integers(min_value=-12, max_value=12),
           integers(min_value=-12, max_value=12))
    def test_helicopiter_move(self, id_, fuel, new_x, new_y):
        manager = SuperDuperManager()
        manager.add_vehicle('Helicopter', id_, fuel)
        manager.move_vehicle(id_, new_x, new_y)
        self.assertEqual((new_x, new_y), manager.get_vehicle_position(id_))

    @given(text(min_size=1),
           integers(min_value=24),
           integers(min_value=-12, max_value=12),
           integers(min_value=-12, max_value=12))
    def test_carpet_move(self, id_, fuel, new_x, new_y):
        manager = SuperDuperManager()
        manager.add_vehicle('UnreliableMagicCarpet', id_, fuel)
        manager.move_vehicle(id_, new_x, new_y)
        x, y = manager.get_vehicle_position(id_)
        delta_x = abs(new_x - x)
        delta_y = abs(new_y - y)
        self.assertLessEqual(delta_x, 2)
        self.assertLessEqual(delta_y, 2)


class ReverseTopTwoTest(unittest.TestCase):
    def test_simple_reverse_top_two(self):
        stack = Stack()
        stack.add(1)
        stack.add(2)
        reverse_top_two(stack)
        self.assertEqual(stack.remove(), 1)
        self.assertEqual(stack.remove(), 2)
        self.assertTrue(stack.is_empty())

    def test_more_than_two_number(self):
        stack = Stack()
        stack.add(1)
        stack.add(2)
        stack.add(3)
        stack.add(4)
        stack.add(5)
        reverse_top_two(stack)
        self.assertEqual(stack.remove(), 4)
        self.assertEqual(stack.remove(), 5)
        self.assertFalse(stack.is_empty())

    def test_more_than_two_char(self):
        stack = Stack()
        stack.add('a')
        stack.add('b')
        stack.add('c')
        stack.add('d')
        stack.add('e')
        reverse_top_two(stack)
        self.assertEqual(stack.remove(), 'd')
        self.assertEqual(stack.remove(), 'e')
        self.assertEqual(stack.remove(), 'c')
        self.assertEqual(stack.remove(), 'b')
        self.assertEqual(stack.remove(), 'a')
        self.assertTrue(stack.is_empty())




if __name__ == '__main__':
    unittest.main()
