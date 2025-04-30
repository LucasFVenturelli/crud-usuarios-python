import unittest
from src import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.usuarios.clear()

    def test_criar_usuario_valido(self):
        resultado = app.criar_usuario("João", "joao@email.com", "1234", "12345678900")
        self.assertEqual(resultado, "Usuário criado com sucesso")
        self.assertEqual(len(app.usuarios), 1)

    def test_criar_usuario_cpf_existente(self):
        app.criar_usuario("João", "joao@email.com", "1234", "12345678900")
        resultado = app.criar_usuario("Maria", "maria@email.com", "5678", "12345678900")
        self.assertEqual(resultado, "Usuário com este CPF já existe")
        self.assertEqual(len(app.usuarios), 1)

    def test_listar_todos_usuarios(self):
        app.criar_usuario("João", "joao@email.com", "1234", "12345678900")
        app.criar_usuario("Maria", "maria@email.com", "5678", "98765432100")
        usuarios = app.listar_todos_usuarios()
        self.assertEqual(len(usuarios), 2)

    def test_listar_usuario_por_cpf(self):
        app.criar_usuario("João", "joao@email.com", "1234", "12345678900")
        usuario = app.listar_usuario_por_cpf("12345678900")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario["nome"], "João")

    def test_listar_usuario_cpf_nao_encontrado(self):
        usuario = app.listar_usuario_por_cpf("00000000000")
        self.assertIsNone(usuario)

    def test_deletar_usuario(self):
        app.criar_usuario("João", "joao@email.com", "1234", "12345678900")
        resultado = app.deletar_usuario("12345678900")
        self.assertEqual(resultado, "Usuário deletado com sucesso")
        self.assertEqual(len(app.usuarios), 0)

    def test_deletar_usuario_nao_encontrado(self):
        resultado = app.deletar_usuario("00000000000")
        self.assertEqual(resultado, "Usuário não encontrado")

#teste
if __name__ == "_main_":
    unittest.main()