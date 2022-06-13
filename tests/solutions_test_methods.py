import unittest

import solutions


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

    def test_day_10_p2(self):
        input = solutions.day_10.process_input_file()
        solution = solutions.day_10.solve_part2(input)
        self.assertEqual(4666278, solution)

    def test_day_11_p1(self):
        input = solutions.day_11.process_input_file()
        solution = solutions.day_11.solve_part1(input)
        self.assertEqual("hepxxyzz", solution)

    def test_day_11_p2(self):
        input = solutions.day_11.process_input_file()
        solution = solutions.day_11.solve_part2(input)
        self.assertEqual("heqaabcc", solution)

    def test_day_12_p1(self):
        input = solutions.day_12.process_input_file()
        solution = solutions.day_12.solve_part1(input)
        self.assertEqual(156366, solution)

    def test_day_12_p2(self):
        input = solutions.day_12.process_input_file()
        solution = solutions.day_12.solve_part2(input)
        self.assertEqual(96852, solution)

    def test_day_13_p1(self):
        input = solutions.day_13.process_input_file()
        solution = solutions.day_13.solve_part1(input)
        self.assertEqual(664, solution)

    def test_day_13_p2(self):
        input = solutions.day_13.process_input_file()
        solution = solutions.day_13.solve_part2(input)
        self.assertEqual(640, solution)

    def test_day_14_p1(self):
        input = solutions.day_14.process_input_file()
        solution = solutions.day_14.solve_part1(input)
        self.assertEqual(2640, solution)

    def test_day_14_p2(self):
        input = solutions.day_14.process_input_file()
        solution = solutions.day_14.solve_part2(input)
        self.assertEqual(1102, solution)
    
    def test_day_15_p1(self):
        input = solutions.day_15.process_input_file()
        solution = solutions.day_15.solve_part1(input)
        self.assertEqual(13882464, solution)
    
    def test_day_15_p2(self):
        input = solutions.day_15.process_input_file()
        solution = solutions.day_15.solve_part2(input)
        self.assertEqual(11171160, solution)

    def test_day_16_p1(self):
        input = solutions.day_16.process_input_file()
        solution = solutions.day_16.solve_part1(input)
        self.assertEqual(373, solution)

    def test_day_16_p2(self):
        input = solutions.day_16.process_input_file()
        solution = solutions.day_16.solve_part2(input)
        self.assertEqual(260, solution)
    
    def test_day_17_p1(self):
        input = solutions.day_17.process_input_file()
        solution = solutions.day_17.solve_part1(input)
        self.assertEqual(1638, solution)

    def test_day_17_p2(self):
        input = solutions.day_17.process_input_file()
        solution = solutions.day_17.solve_part2(input)
        self.assertEqual(17, solution)

    def test_day_18_p1(self):
        input = solutions.day_18.process_input_file()
        solution = solutions.day_18.solve_part1(input)
        self.assertEqual(821, solution)

    def test_day_18_p2(self):
        input = solutions.day_18.process_input_file()
        solution = solutions.day_18.solve_part2(input)
        self.assertEqual(886, solution)
    
    def test_day_19_p1(self):
        input = solutions.day_19.process_input_file()
        solution = solutions.day_19.solve_part1(input)
        self.assertEqual(518, solution)
    
    def test_day_19_p2(self):
        input = solutions.day_19.process_input_file()
        solution = solutions.day_19.solve_part2(input)
        self.assertEqual(200, solution)
    
    def test_day_20_p1(self):
        input = solutions.day_20.process_input_file()
        solution = solutions.day_20.solve_part1(input)
        self.assertEqual(831600, solution)
    
    def test_day_20_p2(self):
        input = solutions.day_20.process_input_file()
        solution = solutions.day_20.solve_part2(input)
        self.assertEqual(884520, solution)

    def test_day_21_p1(self):
        input = solutions.day_21.process_input_file()
        solution = solutions.day_21.solve_part1(input)
        self.assertEqual(78, solution)

    def test_day_21_p2(self):
        input = solutions.day_21.process_input_file()
        solution = solutions.day_21.solve_part2(input)
        self.assertEqual(148, solution)


if __name__ == "__main__":
    unittest.main()
