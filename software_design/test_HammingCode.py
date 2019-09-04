import unittest
from software_design.spiders import HammingCode


class HammingCodeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._number_of_digits = 2

    def test_get_check_digits(self):
        print(HammingCode.get_check_digits(self._number_of_digits))

    def test_get_check_location(self):
        print(HammingCode.get_check_location(self._number_of_digits))
