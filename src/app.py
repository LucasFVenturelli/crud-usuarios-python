usuarios = []

def criar_usuario(nome, email, senha, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return "Usuário com este CPF já existe"
    novo_usuario = {"nome": nome, "email": email, "senha": senha, "cpf": cpf}
    usuarios.append(novo_usuario)
    return "Usuário criado com sucesso"

def listar_todos_usuarios():
    return usuarios

def listar_usuario_por_cpf(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def deletar_usuario(cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuarios.remove(usuario)
            return "Usuário deletado com sucesso"
    return "Usuário não encontrado"