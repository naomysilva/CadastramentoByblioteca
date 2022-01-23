#As listas abaixos serão usadas para armazenar os dicionarios correspondentes a cadastros e empretismos

lista = [{"Livro" : "orgulho e preconceito", "autor": "jane austen"},{"Livro" : "1984", "autor" : "george orwell"},{"Livro" : "dom Quixote de la mancha", "autor" : "miguel de cervantes"}]
Usuario = []
emprestimo = []

#função foi criada para servir de menu para guiar usuario entra as funcionalidades existentes 
def menu():
    print("[0] Tutorial")
    print("[1] Cadastrar Livros")
    print("[2] buscar Livro")
    print("[3] remover Livro")
    print("[4] Listar Disponiveis")
    print("[5] Cadastrar De Usuario")
    print("[6] Listar Usuarios Cadastrados")
    print("[7] Emprestar Livro")
    print("[8] Sair do Sistema")


#função criada para orientar usuario sobre como funciona o sistema
def tutorial():
    print("--------------------------------")
    print("O CARO(A) USUARIO(A) SEJA BEM-VINDO(A) AO NOSSOS SISTEMAS DE CADASTRAMENTO BIBLIOTECARIO")
    print("NESSE SISTEMA VOCÊ PODERÁ CONTROLAR MELHOR O SEU ARSENAL DE LIVROS")
    print("FIQUE ATENTO AS INTRUÇÕES A SEGUIR: \n")
    print("A OPÇÃO CADASTRO LIVRO VOCÊ PODERÁ CADASTRAR LIVRO JUNTAMENTE COM O AUTOR")
    print("A OPÇÃO BUSCAR LIVROS VOCÊ PODE VERIFICAR SE UM LIVRO CONSTAR NO SEU ARSENAL")
    print("NA OPÇÃO REMOVER VOCÊ PODE TIRAR DO SISTEMA UM LIVRO QUE NÃO FAZ PARTE DO SEU ARSENAL")
    print("A FUNÇÃO LISTAR DISPONIVEIS VOCÊ PODERA VER QUAIS LIVROS ESTÃO NA SUA BIBLIOTECA MENOS OS EMPRESTADOS.")
    print("A OPÇÃO CADASTRO USUARIO VOCÊ IRÁ CADASTRAR OS USUARIOS QUE TERÃO PERMISSÃO DE PEGAR UM LIVRO EMPRESTADOS")
    print("A OPÇÃO USUARIOS CADASTRADOS VOCÊ VERÁ QUAIS USUARIOS FORAM CADASTRADOS NO SEU SISTEMA")
    print("NA OPÇÃO SAIR DO SISTEMA VOCÊ ENCERRAR SUA SESSÃO\n")
    print("--------------------------------\n")


    
#função de cadastramemto de Livros
def CadastrarLivros():
    Livro = input("digite o nome do livro:").lower() #usuario irá digitar o nome do livro e ele será convertido em minusculo para que não haja erro no sistema, esse input servirá de valor da chaver do dicionario
    autor = input("digite o nome do autor: ").lower()#usuario irá digitar o nome do autor e ele será convertido em minusculo para que não haja erro no sistema, esse input servirá de valor da chaver do dicionario
    Dicionariocadastro = {"Livro" : Livro, "autor" :  autor} #adicionando dados ao dicionario onde as chaves ira receber o valor dos inputs
    lista.append(Dicionariocadastro) #adicionando Dicionariocadastro dentro de uma lista
    print("--------------------------------")
    print(Livro, "foi adicionado") #exibindo o nome do livro cadastrado e confirmação do cadastro
    print("--------------------------------")

    
#função  de buscar de livros
def buscarLivros():
    Livro = input("O Que deseja encontrar? \n").lower() #usuario irá digitar o nome do livro que desejar encontrar
    LivroEncontrado = False #variavel criada para dar auxilio ao for caso o livro não se encontre na primeira posição não ficará repetindo que livro não foi encontrado até mostrar que ele foi, variavel começa com false e só sera True se livro for encontrado
    for Dicionariocadastro in lista: #for irá percorrer a lista
        if Dicionariocadastro["Livro"] == Livro: #Dicionariocadastro["nome"] irá pegar valor da chave e irá comparar com o valor que usuario digitou
            #Os prints abaixo irá mostrar o nome e autor do livro encontrado
            print("--------------------------------")
            print(f"Livro: {Dicionariocadastro['Livro']}")
            print(f"Autor: {Dicionariocadastro['autor']}")
            print("--------------------------------")
            LivroEncontrado = True #livro foi encontrado logo  variavel deixou de ser false para ser True
            break #uma vem encontrado ele irá parar causo haja mais de um mesmo livro não é preciso mostrar
    if LivroEncontrado == False: #esse if foi colocado dentro do for para que não se repita caso o livro for encontrado e caso ele não seja encontrado 
        print("--------------------------------")
        print("Livro Não Encontrado") #irá mostrar esse print
        print("--------------------------------")

        LivroEncontrado = False #e LivroEncontrado continua/receber  false 
        
#função de remoção de livro
def removerLivro():
    Livro = input("Qual Livro deseja remover? \n").lower() #usuario irá digitar o nome do livro que desejar remover
    LivroEncontrado = False #variavel receber falso caso o livro não seja encontrado, inicializando o mesmo com falso e só mudará para true caso seja encontrado
    for Dicionariocadastro in lista: #for irá percorrer Dicionariocadastro que esta contido(in) em lista lista
        if Dicionariocadastro["Livro"] == Livro: #Dicionariocadastro["nome"] irá pegar valor da chave e irá comparar com o valor que usuario digitou
            lista.remove(Dicionariocadastro) #caso encontrado será removido
            print("--------------------------------")
            print(Livro, "foi Removido")
            print("--------------------------------")
            LivroEncontrado = True #irá mudar a vaariavel para True
            break
    if LivroEncontrado == False: #caso usuario tiver digitado nome de livro que não existe no arsenal a variavel recebera false
        print("--------------------------------")
        print("Livro Não Encontrado")
        print("--------------------------------")
        LivroEncontrado = False
        
#função irá mostrar livros disponiveis
def LivrosDisponiveis():
    for Dicionariocadastro in lista: #for irá percorrer dicionario cadastrado contido(in) em lista e logo em seguida mostrar os livros disponiveis através dos print abaixo
        print("--------------------------------")
        print(f"Livro: {Dicionariocadastro['Livro']}")
        print(f"autor: {Dicionariocadastro['autor']}")
        print("--------------------------------")

#função cadastrar usuario
def CadastrarUsuario():
    Nome = input("digite o nome:").lower() #usuario irá digitar o valor da chave Nome de dicionario
    Telefone = input("Digite Seu Numero:").lower() #usuario irá digitar o valor da chave Telefone de dicionario
    DicionarioUsuario = {"Nome" : Nome, "telefone" :  Telefone} #adicionando dados ao dicionario onde as chaves ira receber o valor dos inputs
    Usuario.append(DicionarioUsuario) #adicionando Dicionariocadastro dentro de uma lista
    print("--------------------------------")
    print(Nome, "foi adicionado") #mostrando que foi adicionado
    print("--------------------------------")
 
#função para mostrar usuario Cadastrados no sistema
def usuarioCadastrados():
        UsuarioListado = False #variavel auxiliar para mostrar se existe usuarios cadastrados
        for DicionarioUsuario in Usuario: #for percorrer dicionario contido em lista para mostrar os usuarios atraves dos prints abaixo
            print("--------------------------------")
            print(f"Nome: {DicionarioUsuario['Nome']}")
            print(f"Telefone: {DicionarioUsuario['telefone']}")
            print("--------------------------------")
            UsuarioListado = True #variavel mostrando True pq foi encontrado usuario
            
        if UsuarioListado == False: #false caso nenhum usuario tenha sido cadastrado
            print("--------------------------------")
            print("Nenhum usuario foi cadastrado")
            print("--------------------------------")
            UsuarioListado = False

   
def Livrosemprestados():
    Nome = input("digite seu nome:").lower()
    Livro = input("Qual Livro Emprestado deseja? ").lower()
    UsuarioListado = False #variavel auxiliar para mostrar se usuario que digitou nome esta cadastrado no sistema
    LivroEncontrado =  False #variavel auxiliar para mostrar se livro que foi digitado existe no sistema
    for DicionarioUsuario in Usuario: #for irá percorrer dicionario contido(in) em lista Usuario
        if DicionarioUsuario["Nome"] == Nome: #Dicionariocadastro["nome"] irá pegar valor da chave e irá comparar com o valor que usuario digitou
                UsuarioListado = True #caso usuario for encontrado
                for Dicionariocadastro in lista: #for irá percorrer a lista
                    if Dicionariocadastro["Livro"] == Livro: #Dicionariocadastro["nome"] irá pegar valor da chave e irá comparar com o valor que usuario digitou
                        print("--------------------------------")
                        print("Livro emprestado com sucesso")
                        print("--------------------------------")
                        lista.remove(Dicionariocadastro) #caso encontrado será removido
                        LivroEncontrado = True #livro foi encontrado então será true
                        break
                if LivroEncontrado == False: #caso livro não seja encontrado
                    print("--------------------------------")
                    print("Livro Não Encontrado")
                    print("--------------------------------")
                    LivroEncontrado = False
    if UsuarioListado == False: #caso usuario não seja encontrado
        print("--------------------------------")
        print("Cadastre Usuario Primeiro Na Opcao 5")
        print("--------------------------------")
        LivroEncontrado = False
        
#chamando primeira tela de menu
menu()
#usuario irá digitar a opção que deseja
opcao = int(input("Digite Opcao que deseja acessar:"))


#o while abaixo é responsavel para seleção das funcionalidades do sistema o mesmo será True até que o usuario digite a opção de parada
#cada if/elif é responsavel por uma chama de função
while True:
    if opcao == 0:
        tutorial()
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 1:
        CadastrarLivros()
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 2:
        buscarLivros()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 3:
        removerLivro()
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 4:
        LivrosDisponiveis()
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 5:
        CadastrarUsuario()
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 6:
       usuarioCadastrados()
       menu()
       opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 7:
        Livrosemprestados()
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
    elif opcao == 8: #usuario escolhe o que deseja acessar
        print("\nAte o proximo acesso...") #mostrará esse print
        break #parará a execurção
    else:
        print("Não temos essa função")
        menu()
        opcao = int(input("Digite Opcao que deseja acessar:"))
        
    
