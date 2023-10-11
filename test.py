from finance import *
from report import *
"""
1 - classe empréstimo
2 - método juros simples return juros
3 - juros Compotos return juros compostos
4 - Metodo montante (1 ou 2) return atributo valor emprestimo (if 1-> JS 2 -> JC) retorna montante + Montante(1)
"""

"""
    Valor total do emprestimo = Valor do emprestimo + (Valor do emprestimo * Taxa de juros/100) * Duração do emprestimo (em meses)
"""
# def calcEmprestimoJS(valorEmprestimo: float, juros: float, tempoEmprestimo: int) -> float:
#     valorTotal = valorEmprestimo + ((valorEmprestimo * (juros/100)) * tempoEmprestimo)
#     return valorTotal

# def calcEmprestimoJC(valorEmprestimo: float, juros: float, tempoEmprestimo: int) -> float:
#     valorTotal = valorEmprestimo * ((1 + (juros/100)) ** tempoEmprestimo)
#     return valorTotal

def main():
    # valorInicial, juros, tempo = list(map(float, input("Entre com o Valor Inical do emprestimo, taxa de juros, tempo do emprestimo").split()))
    valorInicial, juros, tempo = list(map(float, input("").split("|")))
    print(f"Valor do emprestimo:{valorInicial}, Taxa de Juros:{juros}, Tempo(meses):{tempo}")
    # print(f"{type(valorInicial)}, {type(juros)}, {type(tempo)}")
    #valorTotalEmprestimo = calcEmprestimoJS(valorInicial, juros, tempo)
    calcLoan = Finance(valorInicial, juros, tempo)
    report = Report(calcLoan)
    report.generate_report()
    # print('---------------------------Juros Simples--------------------------------------------------')
    # print('M = C x (1 + i x t)')
    # print(calcLoan.montante(1))
    # print(calcLoan.valorEmprestimo)
    # print(calcLoan.juros)
    # print(calcLoan.tempoEmprestimo)
    # print(f'Valor do emprestimo: {valorInicial:.2f}')
    # print(f'Valor dos Juros: {(valorTotalEmprestimo-valorInicial):.2f}')
    # print(f'Valor do emprestimo: {valorTotalEmprestimo:.2f}')
    # print(f'Valor da parcela: {(valorTotalEmprestimo/tempo):.2f}')
    # print('---------------------------Juros Compostos------------------------------------------------')
    # print('M = C (1 + i)^t')
    # print(calcLoan.montante(2))
    #valorTotalEmprestimo = calcEmprestimoJC(valorInicial, juros, tempo)
    # print(f'Valor do emprestimo: {valorInicial:.2f}')
    # print(f'Valor dos Juros: {(valorTotalEmprestimo-valorInicial):.2f}')
    # print(f'Valor do emprestimo: {valorTotalEmprestimo:.2f}')
    # print(f'Valor da parcela: {(valorTotalEmprestimo/tempo):.2f}')
    

if __name__ == '__main__':
    main()