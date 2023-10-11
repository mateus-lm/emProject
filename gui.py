from tkinter import *
from report import *
from finance import *

root = Tk()

# root.mainloop()

class Funcs():
    def clear_screen(self):
        self.entry_val_emprestimo.delete(0, END)
        self.entry_val_juros.delete(0, END)
        self.entry_val_tempo.delete(0, END)
    
    def get_entrys(self):
        self.val_emprestimo = float(self.entry_val_emprestimo.get())
        self.val_juros = float(self.entry_val_juros.get())
        self.val_tempo = float(self.entry_val_tempo.get())
        #print (f"{self.val_emprestimo}{self.val_juros}{self.val_tempo}")
    
    def generate_finance(self):
        self.get_entrys()
        calcLoan = Finance(self.val_emprestimo, self.val_juros, self.val_tempo)
        return calcLoan

    def generate_report(self):
        calcLoan = self.generate_finance()
        Report(calcLoan).generate_report()

class Interface(Funcs):
    def __init__(self) -> None:
        self.root = root
        self.screen()
        self.frame_screen()
        self.widgets()
        root.mainloop()
    
    def screen(self) -> None:
        self.root.title("emProject")
        self.root.configure(background='#6ba3f0')
        self.root.geometry("780x480")
        self.root.resizable(True, True)
    
    def frame_screen(self) -> None:
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.94)
    
    def widgets(self) -> None:
        self.button_clear = Button(self.frame_1, text="Limpar", command=self.clear_screen)
        self.button_clear.place(relx=0.8, rely=0.15, relwidth=0.1, relheight=0.10)
        
        self.button_calculate = Button(self.frame_1, text="Calcular", command=self.outputs)
        self.button_calculate.place(relx=0.65, rely=0.15, relwidth=0.1, relheight=0.10)

        self.button_calculate = Button(self.frame_1, text="Relatório", command=self.generate_report)
        self.button_calculate.place(relx=0.5, rely=0.15, relwidth=0.1, relheight=0.10)

        self.label_val_emprestimo = Label(self.frame_1, text="Valor Empréstimo")
        self.label_val_emprestimo.place(relx=0.04, rely=0.04, relwidth=0.12, relheight=0.16)
        self.entry_val_emprestimo = Entry(self.frame_1, text="Valor Empréstimo")
        self.entry_val_emprestimo.place(relx=0.04, rely=0.15, relwidth=0.1, relheight=0.08)

        self.label_val_juros = Label(self.frame_1, text="Juros")
        self.label_val_juros.place(relx=0.15, rely=0.04, relwidth=0.1, relheight=0.16)
        self.entry_val_juros = Entry(self.frame_1, text="Juros")
        self.entry_val_juros.place(relx=0.175, rely=0.15, relwidth=0.05, relheight=0.08)

        self.label_val_tempo = Label(self.frame_1, text="Tempo (meses)")
        self.label_val_tempo.place(relx=0.24, rely=0.04, relwidth=0.1, relheight=0.16)
        self.entry_val_tempo = Entry(self.frame_1, text="Tempo (meses)")
        self.entry_val_tempo.place(relx=0.26, rely=0.15, relwidth=0.05, relheight=0.08)

    def outputs(self) -> None:
        calcLoan = self.generate_finance()
        self.val_emprestimo = Label(self.frame_1, text=f"{calcLoan.valorEmprestimo:.2f}", font= ('Century 15 bold')).pack()
        self.val_juros = Label(self.frame_1, text=f"{calcLoan.juros_simples():.2f}", font= ('Century 15 bold')).pack()
        self.val_final_emprestimo = Label(self.frame_1, text=f"{calcLoan.montante(1):.2f}", font= ('Century 15 bold')).pack()
        self.val_final_parcela = Label(self.frame_1, text=f"{(calcLoan.montante(1)/calcLoan.tempoEmprestimo):.2f}", font= ('Century 15 bold')).pack()
        
        """
        Valor do emprestimo: 129600.00
        Valor dos Juros: 64851.84
        Valor total do emprestimo: 194451.84
        Valor da parcela: 5401.44
        """

Interface()