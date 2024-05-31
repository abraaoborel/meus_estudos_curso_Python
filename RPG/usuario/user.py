from dataclasses import dataclass

# Para se cadastrar o usuário precisa de um nome e de um email

@dataclass
class Usuario:
    nome: str
    email: str

cadastro = Usuario(
    nome=str(input('Nome: ')),
    email=str(input('Email: '))
)

print(cadastro)