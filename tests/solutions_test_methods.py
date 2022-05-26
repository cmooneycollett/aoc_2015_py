import unittest
import solutions.day_01
import solutions.day_02
import solutions.day_03
import solutions.day_04
import solutions.day_05


class SolutionsTestMethods(unittest.TestCase):

    def test_day_01_p1(self):
        input = solutions.day_01.process_input_file()
        solution = solutions.day_01.solve_part1(input)
        self.assertEqual(232, solution)

    def test_day_01_p2(self):
        input = solutions.day_01.process_input_file()
        solution = solutions.day_01.solve_part2(input)
        self.assertEqual(1783, solution)

    def test_day_02_p1(self):
        input = solutions.day_02.process_input_file()
        solution = solutions.day_02.solve_part1(input)
        self.assertEqual(1588178, solution)

    def test_day_02_p2(self):
        input = solutions.day_02.process_input_file()
        solution = solutions.day_02.solve_part2(input)
        self.assertEqual(3783758, solution)

    def test_day_03_p1(self):
        input = solutions.day_03.process_input_file()
        solution = solutions.day_03.solve_part1(input)
        self.assertEqual(2572, solution)

    def test_day_03_p2(self):
        input = solutions.day_03.process_input_file()
        solution = solutions.day_03.solve_part2(input)
        self.assertEqual(2631, solution)

    def test_day_04_p1(self):
        input = solutions.day_04.process_input_file()
        solution = solutions.day_04.solve_part1(input)
        self.assertEqual(254575, solution)

    def test_day_04_p2(self):
        input = solutions.day_04.process_input_file()
        solution = solutions.day_04.solve_part2(input)
        self.assertEqual(1038736, solution)

    def test_day_05_p1(self):
        input = solutions.day_05.process_input_file()
        solution = solutions.day_05.solve_part1(input)
        self.assertEqual(255, solution)

    def test_day_05_p2(self):
        input = solutions.day_05.process_input_file()
        solution = solutions.day_05.solve_part2(input)
        self.assertEqual(55, solution)


if __name__ == "__main__":
    unittest.main()
