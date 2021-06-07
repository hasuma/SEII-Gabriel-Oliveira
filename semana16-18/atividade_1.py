def sequencia_a(tamanho):
    sequencia = []
    i = 1
    r = 1 
    while i <= tamanho:
        sequencia.append(r)
        r += 2
        i += 1
    return sequencia

def sequencia_b(tamanho):
    sequencia = []
    i = 1
    r = 0
    while i <= tamanho:
        r = r + i
        sequencia.append(r)
        i +=1
    return sequencia

def sequencia_c(tamanho):
    sequencia = []
    i = 1
    while i <= tamanho:
        r = i*i
        sequencia.append(r)
        i +=1
    return sequencia 

if __name__ == '__main__':
    tamanho = 20        # Numero de elemento na lista
    print(sequencia_a(tamanho))
    print(sequencia_b(tamanho))
    print(sequencia_c(tamanho))