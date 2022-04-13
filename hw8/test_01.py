import testlib
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

TIMEOUT=1 * 2

@ddt
class Test(testlib.TestCase):

    def do_test(self, filename, start_city, clues, expected, doRecursionTest=True):
        """Test implementation
        - filename   : the file containing the instructions for the spy
        - start_city : the city the spy starts from (an uppercase string)
        - clues      : the sequence of clues (as a space-separated string)
        - expected   : the expected result (a set of pairs (secret,final city))
        - doRecursionTest: if True the recursion test is applied
        TIMEOUT: 1 seconds for each test
        """
        expected = set([ tuple(e) for e in expected])
        N = len(expected)
        if DEBUG:
                import program01 as program
                result   = program.ex1(filename, start_city, clues)
        else:
            # first check for recursion
            import sys
            if doRecursionTest:
                with    self.assertIsRecursive('program01') as program:
                    program.ex1(filename, start_city, clues)
                del program

            # then test the code
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_open(allowed_filenames_modes={filename: ['r']}), \
                    self.check_imports(allowed=['program01', '_io', 'encodings.utf_8']), \
                    self.imported('program01') as program, \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                result   = program.ex1(filename, start_city, clues)

        self.assertEqual(type(result),  set,
                         "The result should be a set / Il risultato prodotto deve essere un insieme")
        for e in result:
            self.assertEqual( type(e), tuple,
                        "All the set elements should be tuples / Gli elementi dell'insieme devono essere tuple")
            self.assertEqual( len(e), 2,
                        "All the set elements should be tuples of 2 elements / Gli elementi dell'insieme devono essere tuple di 2 elementi")
        self.assertEqual(result, expected,
                         "The returned result is incorrect / Il risultato non è corretto")
        return 1

    @file_data("esempio.json")
    def test_random_1(self, filename, start, clues, expected):
        return self.do_test(filename, start, clues, expected)

    @file_data("empty.json")
    def test_random_2(self, filename, start, clues, expected):
        return self.do_test(filename, start, clues, expected, False)

    @file_data("random-ita-10-3-5-3.json")
    def test_random_3(self, filename, start, clues, expected):
        return self.do_test(filename, start, clues, expected)

    @file_data("random-eng-100-20-50-10.json")
    def test_random_4(self, filename, start, clues, expected):
        return self.do_test(filename, start, clues, expected)

    @file_data("missing.json")
    def test_random_5(self, filename, start, clues, expected):
        return self.do_test(filename, start, clues, expected)

    @file_data("random-eng-5-5-5-5.json")
    def test_random_6(self, filename, start, clues, expected):
        return self.do_test(filename, start, clues, expected)

    def test_random_expo_4(self):
        filename = "exponential.txt"
        clues = ' '.join(['la']*4)
        start = 'ROME'
        TT = [ 'tic', 'tac', 'toc' ]
        BB = [ 'bing', 'bong', 'bang' ]
        expected = { (f"{t1} {b2} {t3} {b4}", 'ROME') for t1 in TT for b2 in BB for t3 in TT for b4 in BB }
        return self.do_test(filename, start, clues, expected)

    def test_random_expo_8(self):
        filename = "exponential.txt"
        clues = ' '.join(['la']*8)
        start = 'ROME'
        TT = [ 'tic', 'tac', 'toc' ]
        BB = [ 'bing', 'bong', 'bang' ]
        expected = { (f"{t1} {b2} {t3} {b4} {t5} {b6} {t7} {b8}", 'ROME') 
                for t1 in TT for b2 in BB for t3 in TT for b4 in BB
                for t5 in TT for b6 in BB for t7 in TT for b8 in BB }
        return self.do_test(filename, start, clues, expected)

    def test_random_expo10(self):
        filename = "exponential.txt"
        clues = ' '.join(['la']*10)
        start = 'ROME'
        TT = [ 'tic', 'tac', 'toc' ]
        BB = [ 'bing', 'bong', 'bang' ]
        expected = { (f"{t1} {b2} {t3} {b4} {t5} {b6} {t7} {b8} {t9} {b10}", 'ROME') 
                for t1 in TT for b2 in BB for t3 in TT for b4 in BB
                for t5 in TT for b6 in BB for t7 in TT for b8 in BB
                for t9 in TT for b10 in BB }
        return self.do_test(filename, start, clues, expected)

if __name__ == '__main__':
    Test.main()

