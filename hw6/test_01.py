import testlib
from ddt import file_data, ddt, data, unpack

# change DEBUG to True to disable timeout and checks
DEBUG=True
DEBUG=False

TIMEOUT=2 * 2

import images   # preload

@ddt
class Test(testlib.TestCase):

    def do_test(self, rectangles_filename, encoded_filename, expected_png, expected):
        '''Test implementation:
            - rectangles_filename:  name of the PNG file containing the rectangles
            - encoded_filename:     name of the PNG file to create
            - N:                    number of rectangles to look for
            - expected_png:         name of the PNG file containing the reference result
            - expected:             the expected bounding-box
            TIMEOUT: 2 seconds for each test
        '''
        if DEBUG:
                import program01 as program
                result   = program.ex1(rectangles_filename, encoded_filename)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_open(allowed_filenames_modes={rectangles_filename: ['rb'],
                                                             encoded_filename: ['wb']}), \
                    self.check_imports(allowed=['program01', '_io', 'images']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result   = program.ex1(rectangles_filename, encoded_filename)
        self.assertEqual(type(result),  tuple,     
                f"il risultato prodotto deve essere una tupla / the expected result should be a tuple ({result})")
        self.assertEqual(type(result[0]),  int,     
                f"il risultato prodotto deve essere una tupla di interi / the expected result should be a tuple of int ({result})")
        self.assertEqual(result,        expected, 
                "il valore restituito non e' corretto / the expected result is incorrect")
        self.check_img_file(encoded_filename, expected_png)
        return 1

    #   test_ID,  N, expected
    @data(
            ('circle',              (5, 5, 27, 28)          ),
            ('5-squares',           (5, 5, 44, 44)          ),
            ('6-rectangles',        (100, 50, 350, 300)     ),
            ('random-5',            (46, 162, 726, 1062)    ),
            ('random-10',           (175, 89, 780, 2815)    ),
            ('random-10-381-504',   (10, 10, 361, 484)      ),
            ('random-15',           (94, 156, 1586, 2106)   ),
            ('random-20-989-471',   (53, 54, 310, 417)      ),
            ('random-25-831-643',   (18, 146, 262, 497)     ),
            ('random-30-1574-1334', (645, 430, 929, 904)    ),
            ('random-40-2399-1913', (993, 657, 1406, 1256)  ),
            ('random-50-991-1437',  (244, 31, 747, 533)     ),
            ('random-75-747-1595',  (68, 93, 679, 860)      ),
            ('random-100-945-835',  (10, 10, 925, 815)      ),
            ('random-150-1074-863', (10, 10, 1054, 843)     ),
          )
    @unpack
    def test_data(self, ID, expected):
        rectangles_file = f"{ID}.png"
        encoded_file    = f"test_{ID}.png"
        expected_png    = f"encoded_{ID}.png"
        return self.do_test(rectangles_file, encoded_file, expected_png, expected)

if __name__ == '__main__':
    Test.main()

