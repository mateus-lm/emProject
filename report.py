from finance import Finance


class Report():
    def __init__(self, finance: Finance) -> None:
        self.finance = finance

    def generate_report(self):
        with open('relatorio.txt', 'w') as f:
            f.write(
f"""Valor do emprestimo:{self.finance.valorEmprestimo:.2f}, Taxa de Juros:{self.finance.juros}, Tempo(meses):{self.finance.tempoEmprestimo}
                ------------Juros Simples------------
                M = C x (1 + i x t)
                Valor do emprestimo: {self.finance.valorEmprestimo:.2f}
                Valor dos Juros: {self.finance.juros_simples():.2f}
                Valor total do emprestimo: {self.finance.montante(1):.2f}
                Valor da parcela: {(self.finance.montante(1)/self.finance.tempoEmprestimo):.2f}

                ------------Juros Compostos----------
                M = C (1 + i)^t
                Valor do emprestimo: {self.finance.valorEmprestimo:.2f}
                Valor dos Juros: {self.finance.juros_compostos():.2f}
                Valor total do emprestimo: {self.finance.montante(2):.2f}
                Valor da parcela: {(self.finance.montante(2)/self.finance.tempoEmprestimo):.2f}
""")
            f.close()
