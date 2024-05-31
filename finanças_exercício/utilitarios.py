from categoria import Categoria
from transacao import Transaçao
LISTA_CATEGORIAS = []
LISTA_TRANSACOES = []

def cadastrar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    LISTA_CATEGORIAS.append(nova_categoria)

    return nova_categoria

def cadastrar_transacao(descricao, valor, categoria):
    nova_transacao = Transaçao(
        descricao=descricao,
        valor=valor,
        categoria=categoria
    )

    LISTA_TRANSACOES.append(nova_transacao)

    return nova_transacao

def saldo_total():
    total = 0

    for t in LISTA_TRANSACOES:
        total += t.valor

    return total
