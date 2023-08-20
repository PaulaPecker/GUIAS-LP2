
#ej5 Escribir una función recursiva, vocales, que devuelva el número de vocales dentro de un string.
def vocales(word:str):

    if len(word)==0:
        return 0
    else:
        word_aux=word[:-1]
        return check_last(word)+vocales(word_aux)
def is_vowel(word:str)->bool:
    return word.lower() in ['a', 'e','i','o','u']
def check_last(word:str)->int:
    if is_vowel(word[-1]):
        return 1
    else:
        return 0

if __name__=='__main__':
    print(vocales("mariposa"))#4
    print(vocales("hola que tul"))#5
    print(vocales("almA hermOsa (tU novia)"))#9
    print (vocales("HolA amiCHIIIII"))#9
