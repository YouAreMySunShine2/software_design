# coding=utf-8
"""
海明码(汉明码)，贝尔实验RichardHamming 设计
1.数据位的位置序号中索引二进制中只有一个1的位（编号1，2，4，8，等，即数据位位置序号的二进制表示中只有一个1）是校验位
2.所有其它位置的数据位（数据位位置序号的二进制表示中至少2个是1）是数据位
3.每一位的数据包含在特定的两个或两个以上的校验位中，这些校验位取决于这些数据位的位置数值的二进制表示
3.1如：校验位1覆盖了所有数据位位置序号的二进制表示倒数第一位是1的数据，校验位2覆盖了所有数据位位置序号的二进制表示倒数第二位是1的数据等
3.2所有校验位覆盖了数据位置和该校验位位置的二进制与的值不为0的数
"""


# 获取校验位数 满足2 ** i - 1 >= n + i
def get_check_digits(n):
    i = 0
    while True:
        if 2 ** i - 1 >= n + i:
            break
        i += 1
    return i


def get_check_location(n):
    i = 0
    while True:
        if 2 ** n - n == 1 + i:
            break
        i += 1
    return i + n


# 将二进制数据转成数组
def get_data_array(_data):
    _array_ = []
    for i in str(bin(_data))[2:]:
        _array_.append(i)
    return _array_


# 索引二进制中只有一个1的位是海明码校验位
def is_hamming_code(_index_):
    _power_ = 0B1
    while _power_ <= _index_:
        if _power_ == _index_:
            return True
        else:
            _power_ <<= 1
    return False


# 将数据拆分为校验码和信息码
def split_data_and_code(_data):
    _array_ = get_data_array(_data)
    _hamming_code_ = {}
    _information_code_ = {}
    _array_.reverse()
    for index, value in enumerate(_array_):
        if is_hamming_code(index+1):
            _hamming_code_[index+1] = value
        else:
            _information_code_[index+1] = value
    return _hamming_code_, _information_code_


# 获得校验码
def get_check_code(_data):
    _hamming_code_, _information_code_ = split_data_and_code(_data)
    _check_code_ = {}
    for _code_ in _hamming_code_:
        _check_code_[_code_] = [_hamming_code_.get(_code_)]
        for _index_ in _information_code_:
            if _code_ == _code_ & _index_:
                _check_code_.get(_code_).append(_information_code_.get(_index_))
    return _check_code_


# 校验数据
def verify_data(_data):
    _check_code_ = get_check_code(_data)
    for _index_ in _check_code_:
        _code_ = _check_code_.get(_index_)
        _result_ = 0
        for p in _code_:
            _result_ += int(p, 2)
        if _result_ & 0B1 != 0:
            return False
    return True
