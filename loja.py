class Loja:
    def __init__(self, cnpj, nome) -> None:
        self.cnpj = cnpj
        self.nome = nome
        self.funcionario = []

        

    def __str__(self) -> str:
        return "[cnpj = {}, nome = {}]".format(self.cnpj, self.nome)
