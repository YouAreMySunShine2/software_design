import unittest
from software_design.spiders import HammingCode


class HammingCodeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._number_of_digits = 8

    def test_get_check_digits(self):
        print(HammingCode.get_check_digits(self._number_of_digits))
