# Vamos criar uma classe para clientes da NetFlix:
class Cliente:
    # Ao criar uma classe a primeira coisa a se fazer é chamar a função init, dessa forma
    def __init__(self, nome, email, plano):     # Os parâmetros, solicitados em self são obrigatórios
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:      # se o plano estiver na lista_planos
            self.plano = plano      # então o plano do cliente recebe o plano
        else:           # caso o plano não esteja na lista_plano
            print('Plano inválido')     # plano invalido

    def mudar_plano(self, novo_plano):      # função de mudar_plano, altera o plano do cliente
        if novo_plano in self.lista_planos:     # se o novo_plano, estiver dentro da lista_planos
            self.plano = novo_plano         # então o plano do cliente recebe (upgrade/downgrade) para o novo_plano
        else:           # se o novo_plano não estiver dentro da _lista_planos
            print('Plano inválido')     # plano inválido



    def ver_filme(self, filme, plano_filme):         # cliente quer ver o filme
           if self.plano == plano_filme:        # se o (plano do cliente) for igual ao (plano do filme)
               print(f'Ver Filme {filme}')      # cliente pode ver o filme
           elif self.plano == 'premium':        # se o (plano do cliente) for o (plano premium)
               print(f'Ver Filme {filme}')      # cliente pode ver o filme
        # se o (plano do cliente) for igual ao (plano basic) e o (plano do filme) for igual ao (plano premium)
           elif self.plano == 'basic' and plano_filme == 'premium':
               print('Faça o upgrade para o premium, para ver esse filme')      # vou solicitar um upgrade de plano
           else:        # se o plano do filme não estiver registrado no sistema
               print('Plano inválido')      # plano inválido



cliente = Cliente('Abraão', 'abraaoborel@gmail.com', 'basic')       # preencho os param do cliente
print(cliente.plano)        # agora eu chamo esse cliente para ver os dados
cliente.ver_filme('Ong Bak III', 'premium')

# no botão de upgrade, essa função!
cliente.mudar_plano('premium')      # aqui eu mudo o plano do cliente
print(cliente.plano)        # plano do cliente alterado de basic para premium
cliente.ver_filme('Ong Bak III', 'basic')

# Assisti essa aula acima com o Lira do Canal Hashtag Programação
# ===================================//========================

