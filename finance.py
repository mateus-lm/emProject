class Finance():
    def __init__(self, valorEmprestimo: float, juros: float, tempoEmprestimo: int) -> None:
        self.valorEmprestimo: float = valorEmprestimo
        self.juros:float = juros
        self.tempoEmprestimo:int = tempoEmprestimo
    
    def juros_simples(self) -> float:
        valorTotal = self.valorEmprestimo + ((self.valorEmprestimo * (self.juros/100)) * self.tempoEmprestimo)
        return valorTotal-self.valorEmprestimo
    
    def juros_compostos(self) -> float:
        valorTotal = self.valorEmprestimo * ((1 + (self.juros/100)) ** self.tempoEmprestimo)
        return valorTotal-self.valorEmprestimo
    
    def montante(self, typeFee: int) -> float:
        #1 Juros Simples
        #2 Juros Compostos
        if typeFee == 1:
            montante = self.juros_simples() + self.valorEmprestimo
        elif typeFee == 2:
            montante = self.juros_compostos() + self.valorEmprestimo
        else: print("Erro, nao existe a opcao")
        return montante
