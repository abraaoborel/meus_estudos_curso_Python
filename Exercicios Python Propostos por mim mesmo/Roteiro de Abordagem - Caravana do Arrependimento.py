# Estou fazendo este programa para testar e treinar alguns códigos
# antes de fazer a prova do mundo 1 de python
#----------------------//-------------------
# Este programa tem que reproduzir o Roteiro de Abordagem,
# da Caravana do Arrependimento
#----------------------//-------------------

from time import sleep

def testebondade():
    print('''
Você realmente me parece uma pessoa boa, mas será que segundo os
mandamentos de Deus você seria considerado por Ele uma pessoa boa?

Vamos para os 10 Mandamentos, você irá entender melhor!

[P] Prossiga...
[S] Sair
    ''')
    resp1 = ' '
    while resp1 not in 'PS':
        resp1 = str(input('Digite [P/S]: ')).strip().upper()[0]
        if resp1 == 'P':
            continue
        elif resp1 == 'S':
            break
        else:
            print('Opção Inválida. Tente Novamente.')
    print('''
    Nessa Etapa os 10 Mandamentos, serão como um espelho!
    Meu objetivo não é te julgar, mas apenas fazer você olhar pra este espelho.
    
    Para que você mesmo possa se avaliar, de acordo com os Mandamentos de Deus.
    Se você pode ser considerado(a) por ele uma pessoa boa.
    
[P] Prossiga...
[S] Sair
    ''')
    resp2 = ' '
    while resp2 not in 'PS':
        resp2 = str(input('Digite [P/S]: ')).strip().upper()[0]
        if resp2 == 'P':
            continue
        elif resp2 == 'S':
            break
        else:
            print('Opção Inválida. Tente Novamente.')
    print('''
    Você já mentiu alguma vez na vida?... 
    
    [S] = Sim, quem é que nunca mentiu?
    [N] = Eu nunca menti
    ''')
    resp3 = ' '
    while resp3 not in 'SN':
        resp3 = str(input('Digite [S/N]: ')).strip().upper()[0]
        if resp3 == 'S':    # Sim, quem é que nunca mentiu?
            print('''
    Quem mente é chamado de Mentiroso, não é verdade?!
    
    Você acha que mentiroso é uma característica de uma pessoa boa?
    
    [A] = Mas, eu só falo mentirinhas brancas. (Que não trazem "grandes prejuizos")
    [B] Não, um mentiroso não é uma característica de uma pessoa boa.
            ''')
            resp4 = ' '
            while resp4 not in 'AB':
                resp4 = str(input('Digite uma opção [A/B]: ')).strip().upper()[0]
                if resp4 == 'A':
                    print('''
    Todas as mentiras que você contou foram dessa categoria?...
                    
    Jesus em certo momento, dizia à multidão:
    Vós tendes por pai ao diabo, e quereis satisfazer os desejos de vosso pai. 
    Ele foi homicida desde o princípio, e não se firmou na verdade, porque não há verdade nele. 
    Quando ele profere mentira, fala do que lhe é próprio, porque é mentiroso, e pai da mentira.
                                                                                João 8.44
    Jesus diz que o diabo é o pai da mentira!
    Ou seja, toda mentira procede do diabo, seja ela branca ou não.
    Quando você mente, você está imitando o diabo.
    
    Você acha que uma pessoa que está imitando o diabo, pode ser considerado por Deus uma pessoa boa?
    
    Você concorda comigo que, uma mentiroso(a) não é uma característica de uma boa pessoa?
    
    [S] = Continuar
    [N] = Sair
                    ''')
                    resp5 = ' '
                    while resp5 not in 'SN':
                        resp5 = str(input('Digite [S/N]: ')).strip().upper()[0]
                        if resp5 == 'S':
                            continue
                        elif resp5 == 'N':
                            break
                        else:
                            print('Opção Inválida! Tente novamente.')
                elif resp4 == 'B':
                    continue
                else:
                    print('Opção Inválida. Tente Novamente.')
        elif resp3 == 'N':      # Eu nunca menti
            print('''
    A Bíblia diz: 
    Se dissermos que não temos pecado, enganamo-nos a nós mesmos, e não há verdade em nós.
    Se dissermos que não pecamos, fazemo-lo mentiroso, e a sua palavra não está em nós.
                                                                                1 João 1.8,10
    Jesus em certo momento, dizia à multidão:
    Vós tendes por pai ao diabo, e quereis satisfazer os desejos de vosso pai. 
    Ele foi homicida desde o princípio, e não se firmou na verdade, porque não há verdade nele. 
    Quando ele profere mentira, fala do que lhe é próprio, porque é mentiroso, e pai da mentira.
                                                                                João 8.44
    Jesus diz que o diabo é o pai da mentira!
    Quando você mente, você está imitando o diabo.
    
    Você acha que uma pessoa que está imitando o diabo, 
    pode ser considerado por Deus uma pessoa boa?
    
    [N] = Não de maneira nenhuma!
            ''')
        else:
            print('Opção Inválida. Tente Novamente.')
def objeçoes():
    objeçao1 = ' '
    while objeçao1 not in 'SN':
        print('-' * 60)
        objeçao1 = str(input('Digite Sim ou Não: ')).strip().upper()[0]
        if objeçao1 == 'S':
            return testebondade()
        elif objeçao1 == 'N':  # Esse bloco como tem uma pergunta! Vai tratar outra objeção!
            print('''
    Tudo bem. Não quero ser inconveniente. Mas eu poderia então, em 30 segundos, 
    deixar um versículo e uma pergunta, apenas para sua meditação?
            ''')
            print('-' * 60)
            objeçao2 = ' '
            while objeçao2 not in 'SN':
                objeçao2 = str(input('Digite Sim ou Não: ')).strip().upper()[0]
                if objeçao2 == 'N':
                    print('''
            “Tem certeza de que não quer conversar sobre isso por alguns minutos?
                    ''')
                    resp_objeçao2_nao = ' '
                    while resp_objeçao2_nao not in 'SN':
                        resp_objeçao2_nao = str(input('Digite [S/N]: ')).strip().upper()[0]
                        if resp_objeçao2_nao == 'S':
                            return testebondade()
                        elif resp_objeçao2_nao == 'N':
                            print('Ok. Tenha um ótimo dia!')
                            break
                    break
                elif objeçao2 == 'S':
                    print('''
                        A Bíblia diz em Hebreus 9.27: 
                        “Ao homem está ordenado morrer uma só vez e depois disso enfrentar o juízo”. 
                        Você estaria preparado hoje para passar por este juízo e ter um final bom?... Por quê?
                    ''')
                    print('-' * 60)
                    objeçao3 = ' '
                    while objeçao3 not in 'ABCDE':
                        print('''
        a) Acho que sim. Porque sou uma pessoa boa.
        b) Sim. Eu tenho certeza da minha Salvação!
        c) Acho que não. Talvez eu não estaria preparado(a) hoje.
        d) Eu não acredito em Deus, e nem da Bíblia.
        e) Sair do programa.
                        ''')
                        objeçao3 = str(input('Digite a opção correspondente: ')).strip().upper()[0]
                        if objeçao3 == 'A':  # Acho que sim
                            return testebondade()
                        if objeçao3 == 'B':  # Tenho certeza da minha Salvação! Agora temos que ver o porque disso!
                            print('-' * 60)
                            print('''
            Porque você tem certeza da sua Salvação?

            a) Por causa das minhas boas obras!
            b) Porque eu sou uma pessoa boa, e Deus não vai me mandar pro inferno.
            c) Porque vou a Igreja, faço a obra de Deus, e sigo todos os mandamentos.
            d) Não por que eu mereça, nem por qualquer coisa que eu tenha feito de bom. 
               Mas somente pela Graça e pela Fé no Filho de Deus, Jesus Cristo.
                            ''')
                            resp_ctz = ' '
                            while resp_ctz not in 'ABCD':
                                resp_ctz = str(input('Digite uma das opções acima: ')).strip().upper()[0]
                                if resp_ctz == 'A':
                                    return testebondade()
                                elif resp_ctz == 'B':
                                    return testebondade()
                                elif resp_ctz == 'C':
                                    return testebondade()
                                elif resp_ctz == 'D':
                                    print('O que você tem feito para a salvação de seus amigos e parentes?')
                                    break
                                else:
                                    print('Opção Inválida! Tente novamente.')
                        elif objeçao3 == 'C':  # Acho que não
                            print('''
        Já que você disse que não está preparado para ir para o céu, isso quer dizer que, 
        pelo seu comportamento, o que você merece mesmo é o inferno?''')
                            objeçao6 = ' '
                            while objeçao6 not in 'SN':
                                print('''
        [N] = Não! Aí pegou pesado. Não sou um pecador tão mal assim...
        [S] = Sim, é isso mesmo! Pelo meu comportamento eu mereço o inferno.
        ''')
                                objeçao6 = str(input('Digite uma opção: ')).strip().upper()[0]
                                if objeçao6 == 'N':
                                    return testebondade()
                                elif objeçao6 == 'S':
                                    continue  # boasnovas()!
                        elif objeçao3 == 'D':  # Deus não, Bíblia não
                            print('-' * 60)
                            print('''
    Ok. Não quero desrespeitar a sua crença, mas vamos pensar o seguinte: 
    Se o que eu estiver falando for verdade, você estaria preparado?
                            ''')
                            objeçao4 = ' '
                            while objeçao4 not in 'SNQ':
                                print('''
        Digite:

        [S] = Sim, se o que você disse for verdade eu estaria preparado.
        [N] = Não, acho que não estaria preparado(a).
        [Q] = Como eu já disse anteriormente, não acredito em Deus e nem na Bíblia.
                                ''')
                                objeçao4 = str(input('Digite [S/N]: ')).strip().upper()[0]
                                if objeçao4 == 'S':
                                    return testebondade()
                                elif objeçao4 == 'N':
                                    print('''
        Já que você disse que não está preparado para ir para o céu, isso quer dizer que, 
        pelo seu comportamento, o que você merece mesmo é o inferno?''')
                                    objeçao5 = ' '
                                    while objeçao5 not in 'SN':
                                        print('''
        [N] = Não! Aí pegou pesado. Não sou um pecador tão mal assim...
        [S] = Sim, é isso mesmo! Pelo meu comportamento eu mereço o inferno.
                                        ''')
                                        objeçao5 = str(input('Digite uma opção: ')).strip().upper()[0]
                                        if objeçao5 == 'N':
                                            return testebondade()
                                        elif objeçao5 == 'S':
                                            continue  # boasnovas()
                                elif objeçao4 == 'Q':
                                    print('''
    Se não é em Deus e na Bíblia, então em que você acredita? 
    E como você sabe que isso é a verdade? Isso não seria apenas um palpite? 

    Você não acha que é perigoso demais você apoiar a sua eternidade em uma simples especulação? 

    E se você estiver errado? 

    Bíblia alerta: ‘O tolo diz em seu coração: ‘Deus não existe’ (Sl 14:1) 

    E mais: ‘Confie no Senhor de todo o seu coração e não se apoie em seu próprio entendimento’ (Pv 3:5).

    A Bíblia é a única fonte segura de revelação sobre quem é Deus e sobre o que acontecerá com a sua alma depois da morte. 
    Lamento dizer, mas você está correndo um grave risco ao se apoiar em meros palpites e especulações!
                                    ''')
                                    print('<<< FIM DO PROGRAMA >>>')
                                    break
                                else:
                                    print('Erro! Opção inválida!')
                        elif objeçao3 == 'E':  # Sair do Programa
                            print('<<< FIM DO PROGRAMA >>>')
                        else:
                            print('ERRO! Opção inválida!')
            break
        else:
            print('ERRO! Por favor digite apenas Sin ou Não. [S/N]')


def abordagem():
    print('-' * 60)
    print('Você ouviria sobre a Palavra de Deus por alguns minutos?')
    objeçoes()
    print('''
A Bíblia diz em Hebreus 9.27: 
“Ao homem está ordenado morrer uma só vez e depois disso enfrentar o juízo”. 
Você estaria preparado hoje para passar por este juízo e ter um final bom?... Por quê?

[S] = Sim, não tenho feito nada de errado.
[N] = Não. Porque eu sou pecador.
    ''')
    resp1 = ' '
    while resp1 not in 'SN':
        resp1 = str(input('Digite [S/N]: ')).strip().upper()[0]
        if resp1 == 'S':
            return testebondade()
        elif resp1 == 'N':
            print('''
Então quer dizer que, se Deus considerasse apenas o seu comportamento, 
o justo seria Ele te mandar para o inferno?

[S] = Sim.
[N] = Mas também não é pra tanto, eu não sou tão ruim assim.
            ''')
            resp2 = ' '
            while resp2 not in 'SN':
                resp2 = str(input('Digite [S/N]: ')).strip().upper()[0]
                if resp2 == 'S':
                    continue
                    # boasnovas()
                elif resp2 == 'N':
                    return testebondade()
                else:
                    print('Opção Inválida. Digite somente S ou N.')
            break
        else:
            print('Opção Inválida! Tente novamente.')
abordagem()




#def boasnovas():