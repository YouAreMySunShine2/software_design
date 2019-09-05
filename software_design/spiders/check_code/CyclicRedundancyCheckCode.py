# coding=utf-8
"""
循环冗余码
根据给定多项式，得到数据总长度k+r-1,
将信息码左移r-1位对给定的生成多项式进行模2除运算得到r-1位校验码，
信息码和校验码组合得到最终数据
"""


# 获取数据二进制位数
def get_length(_num):
    _length_ = 0
    while _num != 0:
        _length_ += 1
        _num >>= 1
    return _length_


# 获取被除数
def get_divisor(_polynomial, _information_code):
    _length_ = get_length(_polynomial)
    _information_code <<= (_length_ - 1)
    return _information_code


# 求模2除运算
def get_residue(_divisor, _polynomial):
    _divisor_length_ = get_length(_divisor)
    _polynomial_length_ = get_length(_polynomial)
    _reference_number_ = 0B1 << (_polynomial_length_-1)
    _divisor_str_ = str(bin(_divisor))[2:]
    while _divisor_length_ >= _polynomial_length_:
        _current_dividend_ = int(_divisor_str_[:_polynomial_length_], 2)
        if (_current_dividend_ & _reference_number_) > 0:
            _current_dividend_ = _current_dividend_ ^ _polynomial
            _divisor_str_ = str(bin(_current_dividend_))[2:] + _divisor_str_[_polynomial_length_:]
        else:
            _divisor_str_ = _divisor_str_[1:]
        _divisor_length_ = len(_divisor_str_)
    return int(_divisor_str_, 2)


# 验证数据是否正确
def verify_data(_data, _polynomial):
    _residue_ = get_residue(_data, _polynomial)
    if _residue_ == 0:
        return True
    else:
        return False

