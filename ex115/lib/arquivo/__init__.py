from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')    # r = read / t = text
        a.close()
    except FileNotFoundError:       # Se o arquivo não foi encontrado
        return False
    else:       # Se eu tentei abrir o arquivo, e ele abriu e fechou
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')       # (w) = write / (t) = text / (+) = se o arquivo não existir ele cria!
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o Arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')     # a = append / t = text (como vimos acima!)
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')
            a.close()
