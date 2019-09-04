import unittest
from software_design.spiders import ParityCode


class ParityCodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._number_ = 0B10101011011001101100

    def test_get_num_of_one(self):
        ParityCode.get_num_of_one(self._number_)

    def test_is_one_of_data_even(self):
        num = ParityCode.is_one_of_data_even(self._number_)
        print(num)

    def test_verify_data(self):
        num = ParityCode.verify_data(self._number_)
        print("数据校验是否通过：" + str(num))
