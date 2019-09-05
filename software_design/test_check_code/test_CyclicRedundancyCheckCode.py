import unittest
from software_design.spiders.check_code import CyclicRedundancyCheckCode


class CyclicRedundancyCheckCodeTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._num = 0B11101
        self._information_code = 0B110

    def test_get_length(self):
        length = CyclicRedundancyCheckCode.get_length(self._num)
        print("0B11110110长度是：" + str(length))

    def test_get_divisor(self):
        _divisor_ = CyclicRedundancyCheckCode.get_divisor(self._num, self._information_code)
        print("获取被除数是：" + str(bin(_divisor_)))

    def test_get_residue(self):
        _residue_ = CyclicRedundancyCheckCode.get_residue(0b1100000, self._num)
        print("获取余数是：" + str(bin(_residue_)))

    def test_verify_data(self):
        _result_ = CyclicRedundancyCheckCode.verify_data(0b1101001, self._num)
        print("数据校验结结果是：" + str(_result_))
