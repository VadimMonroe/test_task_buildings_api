from django.test import TestCase
from ..logic import plus


class LogicTest(TestCase):
    def plus1(self):
        result = plus(2, 2)
        self.assertEqual(4, result)

    def plus2(self):
        result = plus(3, 2)
        self.assertEqual(5, result)
