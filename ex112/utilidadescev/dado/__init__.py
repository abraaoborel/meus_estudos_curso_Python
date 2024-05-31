def leiaDinheiro(msg):
    valido = False      # valido vai começar com False porque não é valido ainda
    while not valido:   # Enquanto ele não for valido
        entrada = str(input(msg)).replace(',','.').strip()    # vamos tratar o param (msg) recebido em str
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True       # Se ele não for alpha númerico, ele é True
            return float(entrada)       # E converte o param(msg) tratado como string em float
