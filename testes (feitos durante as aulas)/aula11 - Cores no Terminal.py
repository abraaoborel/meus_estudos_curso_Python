# PADRÃO: ANSI escape sequence, o escape é representado pela contra barra \

# Sempre que você quiser escrever representar uma cor em python você vai:
# escrever \033[m
# entre o "\033[" e o "m"
# você pode colocar alguns códigos
# o primeiro código que agente vai representar é o código do comportamento/stilo/style
# em seguida você vai colocar ;
# o segundo código que vai representar o texto/text
# em seguida ;
# o terceiro cógido vai representar o background/fundo
# e o "m" para fechar depois dos códigos
# depois que fizer os códigos por exemplo:
# \033[7;97;41m Olá Mundo
# eu preciso fechar o código mostrando que até aquele ponto eu não quero aquela cor mais.
# \033[7;97;41m Olá Mundo \033[m
# coloquei entre espaços, mas ficaria tudo junto dessa forma:
# \033[7;97;41mOlá Mundo\033[m

print('\033[7;97;41mOlá Mundo!\033[m')

# ===========================================
# Códigos style:

# 0 - None
# 1 - Bold (negrito)
# 4 - Underline (sublinhado)
# 7 - Negative

# ===========================================
# Códigos text:

# 97 - Branco
# 30 - Preto
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Azul Ciano
# 37 - Cinza (Normal)

# ===========================================
# Códigos Background:

# 107 - Branco
# 40 - Preto
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Azul Ciano
# 47 - Cinza

# ===========================================
print('\033[0;97;41mTESTE\033[m')
print('\033[4;33;44mTESTE\033[m')
print('\033[1;35;43mTESTE\033[m')
print('\033[30;42mTESTE\033[m')
print('\033[mTESTE')
print('\033[7;97mTESTE\033[m')

# ============================================
# Também pode ser feito dessa forma:
nome = 'Abraão'
print(f'Olá, muito prazer tem te conhecer {'\033[4;34m'}{nome}{'\033[m'}!!!')
# Colocar os codigos ANSI, dentro format em colchetes para abrir e fechar o leque de cores
# Achei que assim ficou um pouco mais complicado.

# ============================================
# A última maneira que ele ensinou foi a seguinte:
# Já dizendo que seria uma tecnica um pouco mais avançada,
# voltei nesse exercício só para aprender está tecnica e exercitá-la.

nome = 'Abraão'

cores = {'limpa':'\033[m',
         'letra azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;97m'}

print(f'Olá, muito prazer tem te conhecer {cores['pretoebranco']} {nome} {cores['limpa']} !!!')

# Criamos um dicionário, e nesse dicionário adicionamos uma palheta de cores
# onde vamos colocar dentro do format como no exemplo acima.

# Praticar esse dicionário juntamente com os outros exercícios se possível
# Ao menos para adicionar cores, ja ir praticando isso vai ser muito bom
# Ao ver vídeo de pessoas programando, vi que esse tipo de dicionário é muito usado na vida real, etc...
# Então eu vi uma importância de praticar este exercício.
# Mesmo que não me foi pedido ou solicitado até o momento neste curso.
# Até porque é um exercício mais avançado e será ensinado, nas proximas etapas.
