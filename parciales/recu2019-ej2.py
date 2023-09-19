

def encontrar_vocales(frase):
    pila=[]
    if len(frase)==0:
        return pila
    else:
        if is_vowel(frase[0]):
            pila.append(frase[0])
        pila.append(encontrar_vocales(frase[1:]))
        return pila

def is_vowel(word: str) -> bool:
    return word.lower() in ['a', 'e', 'i', 'o', 'u']


if __name__=='__main__':
    print(encontrar_vocales("mariposa"))
    print(encontrar_vocales("hola que tul"))
    print(encontrar_vocales("almA hermOsa (tU novia)"))
    print(encontrar_vocales("HolA amiCHIIIII"))
