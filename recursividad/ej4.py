def es_palindromo(word) ->bool:
    cont=0
    if len(word)<=1:
        return True #porque no me molesta
    else:
        return (word[0]==word[-1] and es_palindromo(word[1:-1]))

if __name__ == '__main__':
    print(es_palindromo("neuquen"))
    print(es_palindromo("hola"))