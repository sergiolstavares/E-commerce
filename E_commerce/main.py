from PyQt5 import uic, QtWidgets
import background
import sqlite3

banco = sqlite3.connect("e_commerce.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text,cpf interger,numero interger,email text,endereco text, senha text)")
cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id interger, nome text, valor interger)")


def voltar_pro_login():  # função para voltar pro login de qualquer tela
    cadastro.close()
    cadastro_produto.close()
    tela_principal.close()
    login.show()


def chamar_cadastro():  # função para chamar a tela de cadastro clicando no botão cadastrar na tela de login
    login.close()
    cadastro.show()


def ja_possuo_cadastro():  # função para chamar a tela de login pelo botão ja possuo cadastro na aba cadastro
    cadastro.close()
    cadastro_produto.close()
    login.show()


def area_vendedor():  # função para entrar na tela do vendedor
    login.close()
    vendedor.show()


def logar():  # função para entrar na tela principal da loja e fechar o login
    login.close()
    tela_principal.show()


def cadastrar_produto():
    id = cadastro_produto.produto_id.text()
    nome = cadastro_produto.produto_nome.text()
    valor = cadastro_produto.produto_valor.text()

    cursor.execute("INSERT INTO produtos VALUES(" + str(id) + ",'" + nome + "'," + str(valor) + ")")
    banco.commit()


def cadastrar_usuario():
    nome = cadastro.cadastro_nome.text()
    cpf = cadastro.cadastro_cpf.text()
    numero = cadastro.cadastro_numero.text()
    email = cadastro.cadastro_email.text()
    endereco = cadastro.cadastro_endereco.text()
    senha = cadastro.cadastro_senha.text()

    cursor.execute("INSERT INTO usuarios VALUES ('" + nome + "'," + str(cpf) + "," + str(numero) + ",'" + email + "','" + endereco + "','"+str(senha)+"')")
    banco.commit()


def verificar_vendedor():
    cod_vendedor = "157"
    cod_digitado = vendedor.vendedor_codigo.text()

    if cod_vendedor == cod_digitado:
        vendedor.close()
        cadastro_produto.show()
        print("Código Correto")
    else:
        print("Código do vendedor incorreto")


app = QtWidgets.QApplication([])

login = uic.loadUi("Login.ui")  # conversão do .ui para .py
cadastro = uic.loadUi("cadastro.ui")
cadastro_produto = uic.loadUi("cadastro_produto.ui")
tela_principal = uic.loadUi("tela_principal.ui")
vendedor = uic.loadUi("vendedor.ui")

login.commandLinkButton_2.clicked.connect(chamar_cadastro)  # conectando os botões as respectivas funções
cadastro.botao_ja_possuo_cadastro.clicked.connect(ja_possuo_cadastro)
login.btn_vendedor.clicked.connect(area_vendedor)
cadastro_produto.botao_voltar_login.clicked.connect(voltar_pro_login)
login.botao_entrar.clicked.connect(logar)
tela_principal.botao_sair.clicked.connect(voltar_pro_login)
cadastro.botao_cadastrar.clicked.connect(cadastrar_usuario)
cadastro_produto.botao_cadastrar_produto.clicked.connect(cadastrar_produto)
vendedor.botao_vendedor.clicked.connect(verificar_vendedor)
login.show()

app.exec()
