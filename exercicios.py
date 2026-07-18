import math
from typing import Dict, List

def ex01():
    print("Uma mensagem de boas-vindas")
    print("Uma mensagem dizendo que o aluno está aprendendo Python")
    print("Uma mensagem dizendo que Python é usado para criar programas")


def ex02():
    nome: str = "Ana"
    idade: int = 15
    cidade: str = "Blumenau"
    print(f"Nome: {nome} \n")


def ex03(): 
    nome: str = input("Digite o seu nome")
    print("Ola " + nome + ", seja muito bem vindo")


def ex04():
    nome: str = input("Digite seu nome")
    bairros: str = input("Digite o bairro que voce mora")
    cidade: str = input("Digite a cidade que voce vive")
    print(f"Nome: {nome}\nBairros: {bairros}\nCidade: {cidade}")


def ex05():
    idade: int = int(input("Digite sua idade"))
    print(f"Sua idade é: {idade}")


def ex06():
    nome: str = input("Digite seu nome")
    idade: int = int(input("Digite sua idade"))
    input(f"Sua idade ano que vem vai ser: {idade + 1}")
    #ou
    #idade_proximo_ano: int = idade + 1
    #print(f"Sua idade ano que vem vai ser {idade}")


def ex07():
    numero: int = int(input("Digite o numero POR FAVOR"))
    print(f"Dobro do numero digitado: {numero * 2}")


def ex08():
    idade: int = int(input("Digite sua idade"))
    if idade < 18:
        print(f"Você é de menor")
    else:
        print(f"Você é de maior")


def ex09():
    numero: int = int(input("Digite um numero"))
    if numero > 0:
        print("Numero positivo")
    else:
        print("Numero negativo")


def ex10():
    nome: str = input("Digite seu nome")
    idade: int = int(input("Digite sua idade"))
    if idade >= 16:
        print(f"Bem vindo {nome} ,pode entrar na festa")
    else:
        print(f"{nome} ,não pode entrar na festa por causa da sua idade")


def ex11():
    nota: float = float(input("Digite sua nota"))
    if nota >= 7:
        print("Aprovado ein")
    else:
        print("Reprovado krai")


def ex12():
    saldo: float = float(input("Digite seu saldo"))
    valor_da_compra: float = float(input("Digite o valor da compra"))
    if saldo >= valor_da_compra:
        print("Aee, conseguiu comprar")
    else:
        print("TA DURO MEU FI???")


def ex13():
    nota: float = float(input("Digite sua nota"))
    frequencia: int = int(input("digite sua frequencia"))
    if nota >= 7 and frequencia >= 75:
        print("Aprovado ein")
    else:
        print("Reprovado krai")


def ex14():
    nota: float = float(input("Digite sua nota"))
    if nota < 6 and nota >= 60:
        print("Paga nada fi")
    else:
        print("Paga ai nrml")


def ex15():
    senha: int = int(input("Digite sua senha"))
    nome: str = input("digite seu nome")
    if senha ==1234 and nome == "admin":
        print("entrou na conta com sucesso")
    else:
        print("senha ou nome incorretos, tente novamente")


def ex16():
    i = 0
    while i < 5:
        print("Estou estudando python")
        i = i + 1
        

def ex18():
    i = 0

    msg: str = input("Digite uma mensagem")
    qnt: int = int(input("Digite a quantidade de vez que deseja repetir essa frase"))
    while i < qnt:
        print(msg)
        i += 1


def ex20():
    senha = int(input("Tente uma senha: "))

    while senha != 1234:
        print("Tente novamente")
        senha = int(input("Tente uma senha: "))

    print("Senha correta")


class Tenis:
    def __init__(self, modelo: str, tamanho: int, marca: str, valor: float):
        self.modelo = modelo
        self.tamanho = tamanho
        self.marca = marca
        self.valor = valor

    def apresentar_dados(self):
        print(f"Modelo: {self.modelo}")
        print(f"Tamanho: {self.tamanho}")
        print(f"marca: {self.marca}")
        print(f"valor: {self.valor}", end="\n\n")
    
def exemplo_tenis():
    Nike_air_max_excee = Tenis("Nike air max excee", 41, "Nike", 599.00)
    Nike_air_max_excee.apresentar_dados()
    
    Puma_180 = Tenis("Puma 180", 40, "Puma", 699.00)
    Puma_180.apresentar_dados()
    
    Ja_3 = Tenis("Ja 3", 34, "Nike", 1399.00)
    Ja_3.apresentar_dados()

class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def apresentar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}", end ="\n\n")
        
        media = self.calcular_media()
        print(f"Media final: {media}")
        
        self.apresentar_situacao(media)
        print()
        
    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        print(f"Média final: {media}")
        return media
        
    def apresentar_situacao(self, media):
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

def exemplo_aluno():
    Joao = Aluno("João", 10, 9.5)
    Joao.apresentar_dados()
    
    Maria = Aluno("Maria", 7, 7)
    Maria.apresentar_dados()
    
    Fernando = Aluno("Fernando", 4.7, 1.8)
    Fernando.apresentar_dados()
    

class Triangulo():
    def __init__(self, base: int | float, altura: int | float, lado1: int | float, lado2: int | float, lado3: int | float):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def apresentar_dados(self):
        print(f"base: {self.base}")
        print(f"altura: {self.altura}")
        print(f"lado1: {self.lado1}")
        print(f"lado2: {self.lado2}")
        print(f"lado3: {self.lado3}", end = "\n\n")
        
        self.calcular_area()
        print("\n")
        self.verificar_equilatero()
        print("\n")
        
        
    def calcular_area(self):
        area_triangulo = (self.base * self.altura) / 2
        print(f"Area: {area_triangulo}")
        
        
    def verificar_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Resultado: Equilatero")
        else:
            print("Resultado: Não é equilatero")
            
            
def exemplo_triangulo():
    triangulo1 = Triangulo(10, 7, 8, 7, 6)
    triangulo1.apresentar_dados()
    
    triangulo2 = Triangulo(10, 10, 10, 10, 10)
    triangulo2.apresentar_dados()
    
class Quadrado():
    def __init__(self, lado):
        self.lado = lado
    
    def apresentar_dados(self):
        print(f"Lado: {self.lado}", end = "\n")
        self.calcular_area()
        print("\n")
        self.calcular_perimetro()
        print("\n")
        
    def calcular_area(self):
        area = self.lado ** 2
        print(f"Area: {area}")
        # ** funciona para elevar o numero
    
    def calcular_perimetro(self):
        perimetro = self.lado * 4
        print(f"Perimetro: {perimetro}")
        
def exemplo_quadrado():
    quadrado1 = Quadrado(2)
    quadrado1.apresentar_dados()
    
    quadrado2 = Quadrado(5)
    quadrado2.apresentar_dados()
    
class Retangulo ():
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def apresentar_dados(self):
        print(f"Base: {self.base}", end = "\n")
        print(f"Altura: {self.altura}", end = "\n")
        self.calcular_area()
        print("\n")
        self.calcular_perimetro()
        print("\n")
        
    def calcular_area(self):
        area =  self.base * self.altura
        print(f"Area: {area}")
        
    def calcular_perimetro(self):
        perimetro = self.base + self.altura
        print(f"Perimetro: {perimetro}")
    
def exemplo_retangulo():
    retangulo1 = Retangulo(10, 6)
    retangulo1.apresentar_dados()
    
    retangulo2 = Retangulo(7, 3)
    retangulo2.apresentar_dados()
    
class Circulo():
    def __init__(self, raio: float):
        self.raio = raio
        
    def dados(self):
        print(f"Raio: {self.raio}", end = "\n")
        self.area()
        print("\n")
        self.circunferencia()
        print("\n")
    
    def area(self):
        area = (self.raio ** 2) * math.pi
        #junto com o "import math" é possivel usar(math.pi) como 3,14 que é o que vale pi
        print(f"Area: {area}")
        
    def circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        print(f"Circunferencia: {circunferencia}")
    
def exemplo_circulo():
    circulo1 = Circulo(2.4)
    circulo1.dados()
    
    circulo2 = Circulo(5)
    circulo2.dados()
    
class Personagem:
    def __init__(self, nome: str, vida: int, ataque: int):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def apresentar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print()

    def atacar(self, outro_personagem):
        outro_personagem.vida -= self.ataque

        print(f"{self.nome} atacou {outro_personagem.nome}")
        print(f"Vida atual de {outro_personagem.nome}: {outro_personagem.vida}")
        print()


def exemplo_personagem():
    personagem1 = Personagem("Guerreiro", 100, 20)
    personagem2 = Personagem("Mago", 80, 30)

    print("=== Dados iniciais ===")
    personagem1.apresentar_dados()
    personagem2.apresentar_dados()

    personagem1.atacar(personagem2)
    personagem2.atacar(personagem1)

    print("=== Dados finais ===")
    personagem1.apresentar_dados()
    personagem2.apresentar_dados()


exemplo_personagem()