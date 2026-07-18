def exemplo_string():
    #declarando uma variavel de tipo string
    nome_livro_comeco: str = "harry potter"
    nome_livro_final: str = "As reliquias da morte"
    #declarando uma string e armazenamento a concatenação
    #title => Pascal case
    #UPPER => UPPER CASE
    #lower => lower case
    #capitalize => Abacate com pera e limão
    nome_livro: str = nome_livro_comeco.title() + " " + nome_livro_final.upper()
    print("Livro das filhas da Miranda:", nome_livro)


def primeiro_exemplo():
    print("Ola Mundo")
    fruta: str = "Abacate"
    carro: str = "Corsa"
    quantidade_fruta: int = 6
    preco_unitario_fruta: float = 2.53
    print("Fruta:", fruta)
    print("Quantidade:", quantidade_fruta)
    print("Carro:", carro, "comprou a fruta:", fruta)
    print("Preco unitario:", preco_unitario_fruta)
    print("Preco total:", preco_unitario_fruta * quantidade_fruta)

    primeiro_exemplo()
    exemplo_string()


def exemplo_solicitador_dados():
    #cpnvertendo para letra maiuscula o que o usuario digitou
    #removendo os espaços do começo e fim
    console: str = input("digite o nome do console: [XBOX/PS5]").upper().strip()
    quantidade: int = int(input("Digite a quantidade"))

    preco : float = 0
    if console == "XBOX":
        preco = 6698.00
    elif console == "PS5":
        preco = 4477.00
    else:
        print("Console invalido")
        return
    
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("Total:", preco * quantidade)


def exemplo_if_alunos():
    #float(.....) é a forma que convertemos de string para float
    nota1: float = float(input("Digite a nota 1: "))
    nota2: float = float(input("Digite a nota 2: "))
    nota3: float = float(input("Digite a nota 3: "))

    media: float = (nota1 + nota2 + nota3) / 3

    #bool é boolean (true ou false)
    aprovado: bool = False

    if media >= 6 and media <= 10:
        aprovado = True
    else:
        aprovado = False

    print("media: ", media)

    if aprovado == True:
            print("Aprovado: sim")
    else:
            print("Aprovado: não")
        

def exemplo_while():
    i = 0
    while i < 5:
        print(i)
        i += 1

    while i >= 0:
        print(i)
        i -= 1


def solicitador_dados():
     i = 0
     while i < 3:
          jogador = input("Nome do jogador")
          posicao = input("Posição do jogador")
          Numero: int = int(input("Numero do jogador/da camisa"))
          salario_anual: float = float(input("Salario anual do jogador"))

          salario_mensal = salario_anual / 12

          print("jogador:", jogador, "ganha por mes:", salario_mensal, "ganha por ano:", salario_anual)
          total_salario = total_salario_mensal + salario_mensal
          i += 1
          print("Total mensal dos salarios:", total_mensal_salarios)


def escrever_arquivo_copa_mundo():
     #criar arquivo CSV com os dados que o usuario digitar
     texto_arquivo = "Time1,Time2,Placar\n"

     i = 0
     while i < 3:
        time1: str = input("Time 1: ")
        time1_gols: int = int(input("Gols: " + time1 + ": "))

        time2: str = input("Time 1: ")
        time2_gols: int = int(input("Gols: " + time2 + ": "))

        placar = str(time1_gols) + "x" + str(time2_gols)

        texto_arquivo += f"(time1);(time2);(placar)\n"
        print("\n\n\n----------------------")

        if time1_gols > time2_gols:
             print("resultado: ", time1, "ganhou")
        elif time1_gols < time2_gols:
             print("resultado: ", time2, "ganhou")
        else:
             print("reultado: empate")

        time.sleep(2)

        limpar_terminal = input("Quer limpar o terminal [y/n]")
        if limpar_terminal == "y":
             os.system("cls")

        i = i + 1;

        with open("placar.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_arquivo)
            print("Arquivo 'placar.csv' criado com sucessooooooooooo")

        escrever_arquivo_copa_mundo()



def exemplo_if():
    pass


exemplo_while()