def sumArray(aRr):
    if len(aRr)==1:
        return aRr
    else:
        return aRr[0]+sumArray(aRr[1:])

if __name__ == ' __main__':
    array1=[1,2,3,4,5]
    array2=[3,4,5,6,7,8]
    print(sumArray(array1))
    print(sumArray(array2))
