from pathlib import Path


def exemplo_01():
    for i in range(0, 5):
        print("Ola mundo", i)


def exemplo_02():
    diretorio_atual = Path.cwd()
    nome_novo_diretorio = "Arquivos"
    caminho_novo_diretorio = diretorio_atual / nome_novo_diretorio

    if caminho_novo_diretorio.exists() == False:
        print("criando pasta arquivo")
        caminho_novo_diretorio.mkdir()

    for i in range(2000, 2027):
        nome_pasta_contas = "contas_celesc_2026" + str(i)
        caminho_contas_celesc = caminho_novo_diretorio / nome_pasta_contas
        caminho_contas_celesc.mkdir()

        for j in range(0, 1_000):
            texto = texto + "ola terra\n"
            nome_arquivo = "arquivo" + str(j) + ".txt"
            arquivo_caminho = caminho_contas_celesc / nome_arquivo
            with open("arquivo.txt", "w") as file:
                file.write("texto")
        print(caminho_contas_celesc)
        
#CRIAR ARQUIVO

exemplo_01()