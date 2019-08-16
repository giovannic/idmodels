from core.expressions import Variable, Constant
import unittest

class ExpressionsTest(unittest.TestCase):

    def test_expressions_evaluate_correctly(self):
        self.assertEqual((Variable(4) * Constant(2)).evaluate(), 8)

    def test_expressions_update_with_variables(self):
        x = Variable(4)
        self.assertEqual((x * Constant(2)).evaluate(), 8)
        x.value = 8
        self.assertEqual((x * Constant(2) / Constant(4)).evaluate(), 4)
