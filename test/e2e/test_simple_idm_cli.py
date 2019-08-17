# Test that a simple infectious disease model can be run from the command line
# and print a trace

import unittest
import subprocess

class SimpleIDMTestCase(unittest.TestCase):

    def test_simple_idm_model_converges(self):
        beta = 10
        sigma = 1
        points = 1000
        out = subprocess.run([
            'python',
            '-m',
            'contrib.models.simple_idm',
            str(points),
            str(beta),
            str(sigma)
        ], stdout=subprocess.PIPE).stdout.decode('utf-8')

        lines = [l for l in out.split('\n') if l != '']

        #check that the trace was 50 points long + header
        self.assertEqual(len(lines), points + 1)
        
        #check that the initial state is correct
        self.assertEqual(
            lines[0],
            '\t'.join(['t', 'susceptable', 'infected', 'recovered'])
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

        for point, line in enumerate(lines[2:-1], 1):
            t, s, i, r = line.split('\t')
            assert_valid_population(int(s), int(i), int(r))
            self.assertAlmostEqual(float(t), .1 * point)

        #check that the model converges by the end
        final_state = lines[-1].split('\t')[1:]
        for end_state in lines[-100:-1]:
            self.assertEqual(
                final_state,
                end_state.split('\t')[1:]
            )
