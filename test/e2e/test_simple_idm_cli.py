# Test that a simple infectious disease model can be run from the command line
# and print a trace

import unittest
import subprocess

class SimpleIDMTestCase(unittest.TestCase):

    def test_simple_idm_model_converges(self):
        beta = 10
        sigma = 1
        out = subprocess.Popen([
            'python',
            'contrib.models.simple_idm',
            beta,
            sigma
        ])
        stdout, stderr  = out.communicate()

        lines = stdout.split('\n')

        #check that the trace was 50 points long + header
        self.assertEqual(len(lines), 50 + 1)
        
        #check that the initial state is correct
        self.assertEqual(
            lines[0],
            '\t'.join(['t', 'S', 'I', 'R'])
        )

        self.assertEqual(
            lines[1],
            '\t'.join(['0', '1000', '1', '0'])
        )

        #check that the intermediate values are sensible
        def assert_valid_population(s, i, r):
            self.assertEqual(s + i + r, 1001, 'population has changed')
            for v in [s, i, r]:
                self.assertTrue(
                    v >= 0 and v <= 1001,
                    'variable has exceeded bounds'
                )

        for point, line in enumerate(lines[2:-1], 2):
            t, s, i, r = line.split('\t')
            assert_valid_population(int(s), int(i), int(r))
            self.assertAlmostEqual(float(t), 10. / point)

        #check that the model converges by the end
        self.assertEqual(
            lines[-1],
            '\t'.join(['10', '0', '0', '1001'])
        )
