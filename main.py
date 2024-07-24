import customtkinter
import tkinter as tk
from tkinter import messagebox  # Importa messagebox para mostrar erros
class Calculator:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.title("Calculadora de Juros")
        self.root.iconbitmap("icone.ico")
        self.root.geometry("300x300")
        self.root.resizable(0, 0)
        
        # criação do frame principal
        self.frame = customtkinter.CTkFrame(self.root, bg_color='transparent')
        self.frame.pack(fill="both", expand=True, padx=4, pady=4)

        # Define a fonte padrão
        fonte_padrao = ("Roboto", 10)
        
        # criação do label e entry para o valor total do empréstimo
        self.label_emprestimo = customtkinter.CTkLabel(self.frame, text="Valor Total do Empréstimo:", bg_color='transparent', font=fonte_padrao)
        self.label_emprestimo.grid(row=0, column=0, pady=10, sticky="e")
        self.entry_emprestimo = customtkinter.CTkEntry(self.frame, font=fonte_padrao)
        self.entry_emprestimo.grid(row=0, column=1, pady=10, padx=10)

        # criação do label e entry para a quantidade de meses
        self.label_meses = customtkinter.CTkLabel(self.frame, text="Quantidade de Meses:", bg_color='transparent', font=fonte_padrao)
        self.label_meses.grid(row=1, column=0, pady=10, sticky="e")
        self.entry_meses = customtkinter.CTkEntry(self.frame, font=fonte_padrao)
        self.entry_meses.grid(row=1, column=1, pady=10, padx=10)

        # criação do label e entry para a taxa de juros
        self.label_juros = customtkinter.CTkLabel(self.frame, text="Taxa de Juros ao Mês (%):", bg_color='transparent', font=fonte_padrao)
        self.label_juros.grid(row=2, column=0, pady=10, sticky="e")
        self.entry_juros = customtkinter.CTkEntry(self.frame, font=fonte_padrao)
        self.entry_juros.grid(row=2, column=1, pady=10, padx=10)

        self.botao_calcular = customtkinter.CTkButton(self.root, text="Calcular", command=self.calcular_emprestimo)
        self.botao_calcular.pack(pady=20)

        self.resultado_label = customtkinter.CTkLabel(self.root, text="")
        self.resultado_label.pack(pady=10)

        self.root.mainloop()

    def calcular_parcela(self, valor_total, meses, juros_mensal):
        juros_decimal = juros_mensal / 100
        parcela = (valor_total * juros_decimal) / (1 - (1 + juros_decimal) ** -meses)
        return parcela

    def calcular_emprestimo(self):
        try:
            valor_emprestado_str = self.entry_emprestimo.get().replace(',', '.')
            meses_str = self.entry_meses.get()
            juros_mensal_str = self.entry_juros.get().replace(',', '.')

            valor_emprestado = float(valor_emprestado_str)
            meses = int(meses_str)
            juros_mensal = float(juros_mensal_str)

            valor_parcela = self.calcular_parcela(valor_emprestado, meses, juros_mensal)
            valor_total_emprestimo = valor_parcela * meses

            self.resultado_label.configure(text=f"Valor da parcela mensal: R$ {valor_parcela:.2f}\n"
                                                f"Valor total do empréstimo: R$ {valor_total_emprestimo:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de inserir valores numéricos válidos.")

if __name__ == "__main__":
    Calculator()