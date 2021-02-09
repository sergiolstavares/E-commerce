from PyQt5 import uic, QtWidgets
import background
import sqlite3

banco = sqlite3.connect("e_commerce.db")
cursor = banco.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS usuarios(nome text,cpf interger,numero interger,email text,endereco text, senha text)")
cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id interger, nome text, valor interger)")
cursor.execute("CREATE TABLE IF NOT EXISTS carrinho (cpf interger, produto text)")


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
    login_digitado = login.login_input.text()
    senha_digitado = login.senha_input.text()

    puxar_dados = 'SELECT * FROM usuarios WHERE email =? and senha= ?'

    for usuario in cursor.execute(puxar_dados, (login_digitado, senha_digitado)):
        print(f"Usúario:{usuario[0]}\n"
              f"Cpf:{usuario[1]}\n"
              f"Telefone:{usuario[2]}\n"
              f"Email:{usuario[3]}\n"
              f"Endereço:{usuario[4]}\n"
              f"Senha:{usuario[5]}")

        if usuario[3] == login_digitado and usuario[5] == senha_digitado:
            login.close()
            tela_principal.show()
        else:
            print("Usúario ou senha incorreta")
            login.msg_error.setText("Usúario ou senha incorreta")




def cadastrar_produto():
    id = cadastro_produto.produto_id.text()
    nome = cadastro_produto.produto_nome.text()
    valor = cadastro_produto.produto_valor.text()

    cursor.execute("INSERT INTO produtos VALUES(" + str(id) + ",'" + nome + "'," + str(valor) + ")")
    banco.commit()
    cadastro_produto.produto_id.setText("")
    cadastro_produto.produto_nome.setText("")
    cadastro_produto.produto_valor.setText("")
    print("Produto cadastrado")


def cadastrar_usuario():
    nome = cadastro.cadastro_nome.text()
    cpf = cadastro.cadastro_cpf.text()
    numero = cadastro.cadastro_numero.text()
    email = cadastro.cadastro_email.text()
    endereco = cadastro.cadastro_endereco.text()
    senha = cadastro.cadastro_senha.text()

    cursor.execute("INSERT INTO usuarios VALUES ('" + nome + "'," + str(cpf) + "," + str(
        numero) + ",'" + email + "','" + endereco + "','" + str(senha) + "')")
    banco.commit()

    cadastro.cadastro_nome.setText("")
    cadastro.cadastro_cpf.setText("")
    cadastro.cadastro_numero.setText("")
    cadastro.cadastro_email.setText("")
    cadastro.cadastro_endereco.setText("")
    cadastro.cadastro_senha.setText("")

    print("Usuario cadastrado")
    cadastro.close()
    login.show()


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
