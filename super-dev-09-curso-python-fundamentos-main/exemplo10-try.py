def exemplo_sem_tratamento():
    print("Dvivisão: ", 10 / 0)
    print("mensagem dps da divisao")
    #lança excessao: ZeroDivisiomError: division by zero

def exemplo_com_tratamento():
    try:
        print("div: ", 10 / 0)
    except ZeroDivisionError:
        print("Nao é possivel deividir um numero por 0")

    print("O programa continuou normalmente")

def exemplo_com_tratamento_conversao():
    numero_digitado: str = "vinte"
    try:
        numero: int = int(numero_digitado)
        print("numero digitado: ", numero)
    except:
        print("texto digitado nao é um valido")

print("acabou")

if __name__ == "__main__":
    exemplo_com_tratamento_conversao()