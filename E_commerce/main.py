from PyQt5 import uic, QtWidgets
import sqlite3
import logo
import logo2

banco = sqlite3.connect("e_commerce.db")
cursor = banco.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS usuarios(nome text,cpf interger,numero interger,email text,endereco text, senha text,UNIQUE(email))")
cursor.execute("CREATE TABLE IF NOT EXISTS produtos(id interger, nome text, valor interger, qtd interger,UNIQUE(id))")
cursor.execute("CREATE TABLE IF NOT EXISTS carrinho (cpf interger, produto text, UNIQUE(cpf))")
valor_total = []
produtos_add = []


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

    puxar_dados = 'SELECT * FROM usuarios WHERE email =? and senha= ?'  # comando para puxar do banco o email e a senha

    for usuario in cursor.execute(puxar_dados, (login_digitado, senha_digitado)):
        print("")
        print(f"Usúario:{usuario[0]}\n"
              f"Cpf:{usuario[1]}\n"
              f"Telefone:{usuario[2]}\n"
              f"Email:{usuario[3]}\n"
              f"Endereço:{usuario[4]}\n"
              f"Senha:{usuario[5]}")

        if usuario[3] == login_digitado and usuario[
            5] == senha_digitado:  # compara a senha/login digitados com senha/login do banco
            puxar_produtos()  # Puxa os produtos cadastrados e mostra na tela principal
            login.close()
        else:
            print("Usúario ou senha incorreta")
            login.msg_error.setText("Usúario ou senha incorreta")


def puxar_produtos():
    tela_principal.show()
    tela_principal.mostrar_valor_total.setText("R$ 0")
    cursor.execute("SELECT * FROM produtos")
    produtos_lidos = cursor.fetchall()
    tela_principal.lista_produtos.setRowCount(len(produtos_lidos))
    tela_principal.lista_produtos.setColumnCount(4)

    for i in range(0, len(produtos_lidos)):  # percorre os produtos e cria as linhas e colunas da tabela
        for j in range(0, 4):
            tela_principal.lista_produtos.setItem(i, j, QtWidgets.QTableWidgetItem(str(produtos_lidos[i][j])))


def adicionar_carrinho():
    linha_atual = tela_principal.lista_produtos.currentRow()  # comando para ler a linha selecionada
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha_atual][0]
    cursor.execute("SELECT nome,valor,qtd FROM produtos WHERE id=" + str(valor_id))
    produto = cursor.fetchall()
    produto_format = format(f" Produto: {produto[0][0]} |  Valor: R$ {produto[0][1]}")
    valor_total.append(float(produto[0][1]))  # adicionar o valor do produto adicionado ao carrinho na lista = valor_total
    produtos_add.append(produto)

    print(produto_format)
    print(produtos_add)
    tela_principal.lista_carrinho.addItem(produto_format)

    valor = sum(valor_total)  # recebe a soma da lista valor_total


    qtd_int = int(produto[0][2]) - 1
    qtd_nova = str(qtd_int)
    print(qtd_nova)
    cursor.execute("UPDATE produtos SET qtd = " + qtd_nova + " WHERE id=" + str(valor_id))
    puxar_produtos()
    tela_principal.mostrar_valor_total.setText(
        format(f"R$ {str(valor)}"))  # muda a label para mostrar o valor total atual


def finalizar_compra():
    banco.commit()
    puxar_produtos()
    tela_principal.lista_carrinho.clear()
    tela_principal.mostrar_valor_total.setText("R$ 0")
    valor_total.clear()
    produtos_add.clear()

    print("Compra Finalizada")


def cadastrar_produto():
    try:
        id = cadastro_produto.produto_id.text()
        nome = cadastro_produto.produto_nome.text()
        valor = cadastro_produto.produto_valor.text()
        qtd = cadastro_produto.produto_qtd.text()

        cursor.execute(
            "INSERT INTO produtos VALUES(" + str(id) + ",'" + nome + "'," + str(valor) + ", " + str(qtd) + ")")
        banco.commit()

        cadastro_produto.produto_id.setText("")
        cadastro_produto.produto_nome.setText("")
        cadastro_produto.produto_valor.setText("")
        cadastro_produto.produto_qtd.setText("")
        print("Produto cadastrado")
    except:
        print("Produto ja cadastrado")


def cadastrar_usuario():
    try:
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
    except:
        print("Usuario ja cadastrado")
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


def sair():
    exit()


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
tela_principal.botao_sair.clicked.connect(sair)
cadastro.botao_cadastrar.clicked.connect(cadastrar_usuario)
cadastro_produto.botao_cadastrar_produto.clicked.connect(cadastrar_produto)
vendedor.botao_vendedor.clicked.connect(verificar_vendedor)
tela_principal.btn_adicionar_ao_carrinho.clicked.connect(adicionar_carrinho)
tela_principal.botao_finalizar_compra.clicked.connect(finalizar_compra)

login.show()
app.exec()
