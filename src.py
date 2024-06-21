import tkinter as tk
from tkinter import ttk, messagebox

def calcular_parcela(valor_total, meses, juros_mensal):
    juros_decimal = juros_mensal / 100.0
    parcela = (valor_total * juros_decimal) / (1 - (1 + juros_decimal) ** -meses)
    return parcela

def calcular_emprestimo():
    try:
        valor_emprestado = float(valor_emprestado_entry.get())
        meses = int(meses_entry.get())
        juros_mensal = float(juros_mensal_entry.get())

        valor_parcela = calcular_parcela(valor_emprestado, meses, juros_mensal)
        valor_total_emprestimo = valor_parcela * meses

        resultado_label.config(text=f"Valor da parcela mensal: R$ {valor_parcela:.2f}\n"
                                    f"Valor total do empréstimo: R$ {valor_total_emprestimo:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Certifique-se de inserir valores numéricos válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Empréstimo ")

# Aplicar estilo aos widgets usando ttk
style = ttk.Style()
style.theme_use('clam')  # Escolha um tema suportado pelo ttk

# Criar e posicionar os widgets na janela
content_frame = ttk.Frame(root, padding="20")
content_frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(content_frame, text="Valor Total do Empréstimo:").grid(row=0, column=0, pady=15, sticky="w")
valor_emprestado_entry = ttk.Entry(content_frame, width=20)
valor_emprestado_entry.grid(row=0, column=1, pady=10)

ttk.Label(content_frame, text="Quantidade de Meses:").grid(row=1, column=0, pady=10, sticky="w")
meses_entry = ttk.Entry(content_frame, width=20)
meses_entry.grid(row=1, column=1, pady=10)

ttk.Label(content_frame, text="Taxa de Juros ao Mês (%):").grid(row=2, column=0, pady=10, sticky="w")
juros_mensal_entry = ttk.Entry(content_frame, width=20)
juros_mensal_entry.grid(row=2, column=1, pady=10)

calcular_button = ttk.Button(content_frame, text="Calcular", command=calcular_emprestimo)
calcular_button.grid(row=3, column=0, columnspan=2, pady=20)

resultado_label = ttk.Label(content_frame, text="", anchor="w", font=("Helvetica", 12))
resultado_label.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

# Adicionar rodapé
footer_frame = ttk.Frame(root, padding="10")
footer_frame.grid(row=1, column=0, sticky="ew")

footer_label = ttk.Label(footer_frame, text="Developed by Willian Leoni", anchor="center", font=("Helvetica", 10))
footer_label.pack()

# Redimensionar as células da grade para se ajustarem ao conteúdo
for child in content_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Redimensionar a janela principal para se ajustar ao conteúdo
root.resizable(False, False)

# Configurar a grid da janela principal para redimensionamento adequado
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Iniciar o loop principal da interface gráfica
root.mainloop()
