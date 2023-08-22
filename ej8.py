def C(total, grupo):
    if total == grupo or grupo == 0:
        return 1
    else:
        return C(total-1,grupo-1)+C(total-1,grupo)


if __name__ == '__main__':
    print(C(5,3))
    print(C(9,4))