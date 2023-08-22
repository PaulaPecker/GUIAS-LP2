def ndigits(num):
    if num<10:
        return 1
    else:
        return 1+ndigits(num/10)


if __name__ == '__main__':
    print(ndigits(56789))
    print(ndigits(4323))
