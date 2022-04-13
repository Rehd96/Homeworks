import testlib
import random
from ddt import file_data, ddt, data, unpack


# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

@ddt
class Test(testlib.TestCase):

    def do_test(self, g1, g2, g3, g4, hand_size, num_letters, expected):
        """Test implementation
        - g1, g2, g3, g4: words played by each of the 4 players
        - hand_size:      number of tiles in a player’s hand
        - num_letters:    number of initial letters
        - expected:       expected result
        TIMEOUT: 0.5 seconds for each test
        """
        g1 = g1[:]
        g2 = g2[:]
        g3 = g3[:]
        g4 = g4[:]
        if DEBUG:
                import program01 as program
                result = program.ex1(g1, g2, g3, g4, hand_size, num_letters)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.forbidden_function('builtins.open'), \
                    self.check_imports(allowed=['program01','_io']), \
                    self.timeout(0.5), \
                    self.timer(0.5):
                import program01 as program
                result = program.ex1(g1, g2, g3, g4, hand_size, num_letters)
        self.assertEqual(type(result), list,
                         ('The output type should be: list\n'
                          '[Il tipo di dato in output deve essere: list]'))
        self.assertEqual(type(result[0]), int,
                         ('The output type should be: a list of int\n'
                          '[Il tipo di dato in output deve essere: una lista di int]'))
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          '[Il valore di ritorno è errato]'))
        return 1

    def test_example(self):
        hand_size   =  5
        num_letters = 40
        g1 = ['seta','peeks','deter']
        g2 = ['reo','pumas']
        g3 = ['xx','xx']
        g4 = ['frs','bern']
        expected = [21, 3, 23, 9]
        return self.do_test(g1, g2, g3, g4, hand_size, num_letters, expected)

    @file_data("test_01.json")
    def test_json1(self, g1, g2, g3, g4, hand_size, num_letters, expected):
        return self.do_test(g1, g2, g3, g4, hand_size, num_letters, expected)

    @file_data("test_100K.json")
    def test_json2(self, g1, g2, g3, g4, hand_size, num_letters, expected):
        return self.do_test(g1, g2, g3, g4, hand_size, num_letters, expected)

    @file_data("test_500K.json")
    def test_json3(self, g1, g2, g3, g4, hand_size, num_letters, expected):
        return self.do_test(g1, g2, g3, g4, hand_size, num_letters, expected)

    @file_data("test_1M.json")
    def test_json4(self, g1, g2, g3, g4, hand_size, num_letters, expected):
        return self.do_test(g1, g2, g3, g4, hand_size, num_letters, expected)

if __name__ == '__main__':
    Test.main()


