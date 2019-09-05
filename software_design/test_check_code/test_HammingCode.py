import unittest
from software_design.spiders.check_code import HammingCode


class HammingCodeTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self._number_of_digits = 2
        self._data_ = 0B011001001101

    def test_get_check_digits(self):
        print(HammingCode.get_check_digits(self._number_of_digits))

    def test_get_check_location(self):
        print(HammingCode.get_check_location(self._number_of_digits))

    def test_get_data_array(self):
        print(HammingCode.get_data_array(self._data_))

    def test_split_data_and_code(self):
        print(HammingCode.split_data_and_code(self._data_))

    def test_verify_data(self):
        print(HammingCode.verify_data(self._data_))

    def test_get_check_code(self):
        print(HammingCode.get_check_code(self._data_))

    def test_is_hamming_code(self):
        print(HammingCode.is_hamming_code(self._data_))
