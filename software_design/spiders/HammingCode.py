# 海明码，贝尔实验RichardHamming 设计

# 获取校验位数 满足2 ** i - 1 >= n + i


def get_check_digits(n):
    i = 0
    while True:
        if 2 ** i - 1 >= n + i:
            break
        i += 1
    return i
