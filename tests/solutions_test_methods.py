import unittest
import solutions.day_01
import solutions.day_02


class SolutionsTestMethods(unittest.TestCase):

    def test_day_01_p1(self):
        input = solutions.day_01.generate_input()
        solution = solutions.day_01.solve_part1(input)
        self.assertEqual(232, solution)

    def test_day_01_p2(self):
        input = solutions.day_01.generate_input()
        solution = solutions.day_01.solve_part2(input)
        self.assertEqual(1783, solution)

    def test_day_02_p1(self):
        input = solutions.day_02.generate_input()
        solution = solutions.day_02.solve_part1(input)
        self.assertEqual(1588178, solution)

    def test_day_02_p2(self):
        input = solutions.day_02.generate_input()
        solution = solutions.day_02.solve_part2(input)
        self.assertEqual(3783758, solution)


if __name__ == "__main__":
    unittest.main()
