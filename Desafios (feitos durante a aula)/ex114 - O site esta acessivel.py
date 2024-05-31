#  Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# Não consegui acessar o site pudim, mas pelo navegador sim.
# Porem consegui acessar outros sites por aqui também.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.earlychristianwritings.com/')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso')
#    print(site.read())
#    para ler o script do site
