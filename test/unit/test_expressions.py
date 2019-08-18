from core.expressions import Variable, Constant
import unittest

class ExpressionsTest(unittest.TestCase):

    def test_expressions_evaluate_correctly(self):
        exp = (Variable(4) * Constant(2))
        exp.initialise(1)
        self.assertEqual(exp.evaluate(), 8)

    def test_expressions_update_with_variables(self):
        x = Variable(4)
        exp = (x * Constant(2))
        exp.initialise(1)
        self.assertEqual(exp.evaluate(), 8)
        x.value *= 2
        self.assertEqual(exp.evaluate(), 16)
