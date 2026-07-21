class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    
def exemplo_funcionario():
    pessoa = Pessoa ("Ronaldo", "Remomemo")
    print(f"Nome completo: {pessoa.gerar_nome_completo()}")

    funcionario = Funcionario("Lionel", "Messi", "Uber")
    print(f"Nome completo do funcionario: {funcionario.gerar_nome_completo()}")

exemplo_funcionario()