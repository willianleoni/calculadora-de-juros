import tkinter as tk
from tkinter import ttk, messagebox

class CalculadoraEmprestimo:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Empréstimo")

        # Aplicar estilo aos widgets usando ttk
        style = ttk.Style()
        style.theme_use('clam')  # Escolha um tema suportado pelo ttk

        # Criar e posicionar os widgets na janela
        content_frame = ttk.Frame(self.root, padding="20")
        content_frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(content_frame, text="Valor Total do Empréstimo:").grid(row=0, column=0, pady=15, sticky="w")
        self.valor_emprestado_entry = ttk.Entry(content_frame, width=20)
        self.valor_emprestado_entry.grid(row=0, column=1, pady=10)

        ttk.Label(content_frame, text="Quantidade de Meses:").grid(row=1, column=0, pady=10, sticky="w")
        self.meses_entry = ttk.Entry(content_frame, width=20)
        self.meses_entry.grid(row=1, column=1, pady=10)

        ttk.Label(content_frame, text="Taxa de Juros ao Mês (%):").grid(row=2, column=0, pady=10, sticky="w")
        self.juros_mensal_entry = ttk.Entry(content_frame, width=20)
        self.juros_mensal_entry.grid(row=2, column=1, pady=10)

        calcular_button = ttk.Button(content_frame, text="Calcular", command=self.calcular_emprestimo)
        calcular_button.grid(row=3, column=0, columnspan=2, pady=20)

        self.resultado_label = ttk.Label(content_frame, text="", anchor="w", font=("Helvetica", 12))
        self.resultado_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

        # Adicionar rodapé
        footer_frame = ttk.Frame(self.root, padding="10")
        footer_frame.grid(row=1, column=0, sticky="ew")

        footer_label = ttk.Label(footer_frame, text=" ", anchor="center", font=("Helvetica", 10))
        footer_label.pack()

        # Redimensionar as células da grade para se ajustarem ao conteúdo
        for child in content_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Redimensionar a janela principal para se ajustar ao conteúdo
        self.root.resizable(False, False)

        # Configurar a grid da janela principal para redimensionamento adequado
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def calcular_parcela(self, valor_total, meses, juros_mensal):
        juros_decimal = juros_mensal / 100.0
        parcela = (valor_total * juros_decimal) / (1 - (1 + juros_decimal) ** -meses)
        return parcela

    def calcular_emprestimo(self):
        try:
            valor_emprestado = float(self.valor_emprestado_entry.get())
            meses = int(self.meses_entry.get())
            juros_mensal = float(self.juros_mensal_entry.get())

            valor_parcela = self.calcular_parcela(valor_emprestado, meses, juros_mensal)
            valor_total_emprestimo = valor_parcela * meses

            self.resultado_label.config(text=f"Valor da parcela mensal: R$ {valor_parcela:.2f}\n"
                                             f"Valor total do empréstimo: R$ {valor_total_emprestimo:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de inserir valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraEmprestimo(root)
    root.mainloop()
