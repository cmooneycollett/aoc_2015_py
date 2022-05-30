import unittest
import solutions.day_01
import solutions.day_02
import solutions.day_03
import solutions.day_04
import solutions.day_05
import solutions.day_06
import solutions.day_07
import solutions.day_08
import solutions.day_09
import solutions.day_10


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

    def test_day_06_p1(self):
        input = solutions.day_06.process_input_file()
        solution = solutions.day_06.solve_part1(input)
        self.assertEqual(377891, solution)

    def test_day_06_p2(self):
        input = solutions.day_06.process_input_file()
        solution = solutions.day_06.solve_part2(input)
        self.assertEqual(14110788, solution)

    def test_day_07_p1(self):
        input = solutions.day_07.process_input_file()
        solution = solutions.day_07.solve_part1(input)
        self.assertEqual(956, solution)

    def test_day_07_p2(self):
        input = solutions.day_07.process_input_file()
        solution = solutions.day_07.solve_part2(input)
        self.assertEqual(40149, solution)

    def test_day_08_p1(self):
        input = solutions.day_08.process_input_file()
        solution = solutions.day_08.solve_part1(input)
        self.assertEqual(1371, solution)

    def test_day_08_p2(self):
        input = solutions.day_08.process_input_file()
        solution = solutions.day_08.solve_part2(input)
        self.assertEqual(2117, solution)

    def test_day_09_p1(self):
        input = solutions.day_09.process_input_file()
        solution = solutions.day_09.solve_part1(input)
        self.assertEqual(141, solution)

    def test_day_09_p2(self):
        input = solutions.day_09.process_input_file()
        solution = solutions.day_09.solve_part2(input)
        self.assertEqual(736, solution)

    def test_day_10_p1(self):
        input = solutions.day_10.process_input_file()
        solution = solutions.day_10.solve_part1(input)
        self.assertEqual(329356, solution)


if __name__ == "__main__":
    unittest.main()
