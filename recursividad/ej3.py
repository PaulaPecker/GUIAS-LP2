def invertir_palabra(word):
    if len(word)<=1:
        return word
    else:
        aux_beg=word[-1]
        aux_end=word[0]
        word_aux=word[1:-1]
        return aux_beg+invertir_palabra(word_aux)+aux_end


if __name__==('__main__'):
    print(invertir_palabra("hola"))
    print(invertir_palabra("paula"))