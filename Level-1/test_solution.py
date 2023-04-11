import unittest

def solution(area):
    res = []
    while area > 0:
        biggest_square_side = int(area ** 0.5)
        biggest_square_area = biggest_square_side ** 2
        area -= biggest_square_area
        res.append(biggest_square_area)
    return res

class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(12), [9,1,1,1], "Should be [9,1,1,1]")
        self.assertEqual(solution(15324), [15129,169,25,1], "Should be [15129,169,25,1]")
        

if __name__ == '__main__':
    unittest.main()