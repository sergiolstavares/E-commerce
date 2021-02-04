from PyQt5 import uic, QtWidgets
import background


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


def area_cadastro_produto():  # função para entrar na tela de cadastro de produto
    vendedor.close()
    cadastro_produto.show()


def logar():  # função para entrar na tela principal da loja e fechar o login
    login.close()
    tela_principal.show()


app = QtWidgets.QApplication([])

login = uic.loadUi("Login.ui")  # conversão do .ui para .py
cadastro = uic.loadUi("cadastro.ui")
cadastro_produto = uic.loadUi("cadastro_produto.ui")
tela_principal = uic.loadUi("tela_principal.ui")
vendedor = uic.loadUi("vendedor.ui")

login.commandLinkButton_2.clicked.connect(chamar_cadastro)  # conectando os botões as respectivas funções
cadastro.botao_ja_possuo_cadastro.clicked.connect(ja_possuo_cadastro)
login.btn_vendedor.clicked.connect(area_vendedor)
vendedor.botao_vendedor.clicked.connect(area_cadastro_produto)
cadastro_produto.botao_voltar_login.clicked.connect(voltar_pro_login)
login.botao_entrar.clicked.connect(logar)
tela_principal.botao_sair.clicked.connect(voltar_pro_login)

login.show()

app.exec()
