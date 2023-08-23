from recursividad.ej1 import ndigits
def invertir_rec(num): #asumo num entero positivo porque un lio

    n = ndigits(num)
    if n == 1:
        return num
    else:
        num_aux=(num-int(num %10)-int(num/pow(10,n-1))*pow(10,n-1))/10
        return int(num %10)*pow(10,n-1)+int(num/pow(10,n-1))+invertir_rec(num_aux)*10

if __name__ =='__main__':
    print(invertir_rec(9876))
    print(invertir_rec(45189))
    print(invertir_rec(2))
