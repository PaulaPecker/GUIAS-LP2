def sumSquares(N):
    if N==0:
        return 0
    else:
        return pow(N,2)+sumSquares(N-1)

if __name__ == '__main__':
    print(sumSquares(9))
    print(sumSquares(5))

