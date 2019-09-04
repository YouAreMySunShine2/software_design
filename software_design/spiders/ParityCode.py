# coding=utf-8
"""
奇偶码
在传过来的数据末位增加一位校验码用来表示1的奇偶性，如果有偶个数据位错误则结果也是正确，比较简单高效，校验结果不太靠谱
"""


# 获取二进制数据中1的个数
def get_num_of_one(_data):
    num = 0
    while _data != 0:
        num += 1
        _data = _data & (_data - 1)
    return num


# 二进制数据中1的个数是否为偶数
def is_one_of_data_even(_data):
    num = get_num_of_one(_data)
    if num % 2 == 0:
        return 0B1
    else:
        return 0B0


def verify_data(_data):
    # 取二进制最后一位数值
    last_one = _data & 1
    # 移除数据校验位
    num = _data >> 1
    return (is_one_of_data_even(num) ^ last_one) == 0
