def C(total, grupo):
    if total == grupo or grupo == 0:
        return 1
    else:
        return C(total-1,grupo-1)+C(total-1,grupo)

def C_fact(total,grupo):
    return fact(total)/(fact(grupo)*fact(total-grupo))

def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    print(C(5,3))
    print(C(9,4))
    print(C(15,6))
    print(C(36,5))
    print(C_fact(5, 3))
    print(C_fact(9, 4))
    print(C_fact(15, 6))
    print(C_fact(36, 5))