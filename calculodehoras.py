import customtkinter as ctk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from dataclasses import dataclass
from typing import Optional, Dict, Tuple, Union
from decimal import Decimal
import os
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes
SALARIO_MINIMO = Decimal("1518.00")

@dataclass
class Funcionario:
    salario_base: Decimal
    carga_horaria: int
    horas_trabalhadas: int
    adicional_noturno: bool = False
    grau_insalubridade: Optional[int] = None
    periculosidade: bool = False
    vale_transporte: bool = False

    def calcular(self) -> Dict[str, Union[str, Decimal]]:
        valor_hora = self.salario_base / Decimal(self.carga_horaria)
        horas_faltantes = max(0, self.carga_horaria - self.horas_trabalhadas)
        desconto_faltas = valor_hora * horas_faltantes

        descontos = desconto_faltas
        vt = Decimal("0.06") * self.salario_base if self.vale_transporte else Decimal("0.00")
        descontos += vt

        inss = self.salario_base * Decimal("0.08")
        fgts = self.salario_base * Decimal("0.08")

        adicional = Decimal("0.00")
        if self.adicional_noturno:
            adicional += self.salario_base * Decimal("0.20")
        if self.grau_insalubridade:
            percentual = [0.10, 0.20, 0.40][self.grau_insalubridade - 1]
            adicional += SALARIO_MINIMO * Decimal(percentual)
        if self.periculosidade:
            adicional += self.salario_base * Decimal("0.30")

        salario_liquido = self.salario_base + adicional - descontos - inss

        return {
            "Valor Hora": round(valor_hora, 2),
            "Horas Faltantes": horas_faltantes,
            "Desconto em R$": round(descontos, 2),
            "Desconto %": round((descontos / self.salario_base) * 100, 2) if self.salario_base > 0 else 0,
            "Vale Transporte": round(vt, 2),
            "INSS": round(inss, 2),
            "FGTS": round(fgts, 2),
            "Adicionais": round(adicional, 2),
            "Salário Líquido": round(salario_liquido, 2)
        }

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cálculo Salarial")
        self.geometry("600x700")
        ctk.set_appearance_mode("System")

        self.criar_widgets()

    def criar_widgets(self):
        self.inputs = {}

        campos = [
            ("Salário Base (R$)", "salario_base"),
            ("Carga Horária Contratada", "carga_horaria"),
            ("Horas Trabalhadas", "horas_trabalhadas")
        ]

        for i, (label_text, key) in enumerate(campos):
            label = ctk.CTkLabel(self, text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ctk.CTkEntry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.inputs[key] = entry

        # Adicionais e opções
        self.vt_var = ctk.BooleanVar()
        self.noturno_var = ctk.BooleanVar()
        self.periculosidade_var = ctk.BooleanVar()

        self.insalubridade_var = ctk.StringVar(value="0")

        self.check_vt = ctk.CTkCheckBox(self, text="Vale Transporte", variable=self.vt_var)
        self.check_noturno = ctk.CTkCheckBox(self, text="Adicional Noturno", variable=self.noturno_var)
        self.check_periculosidade = ctk.CTkCheckBox(self, text="Periculosidade", variable=self.periculosidade_var)
        self.check_insalubridade = ctk.CTkComboBox(self, values=["0", "1", "2", "3"], variable=self.insalubridade_var)

        self.check_vt.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.check_noturno.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.check_periculosidade.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkLabel(self, text="Grau Insalubridade (0 a 3)").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.check_insalubridade.grid(row=6, column=1, padx=10, pady=5)

        # Botões
        self.btn_calcular = ctk.CTkButton(self, text="Calcular", command=self.calcular)
        self.btn_exportar = ctk.CTkButton(self, text="Exportar PDF", command=self.exportar_pdf)
        self.btn_limpar = ctk.CTkButton(self, text="Limpar", command=self.limpar)
        self.btn_tema = ctk.CTkButton(self, text="Alternar Tema", command=self.alternar_tema)

        self.btn_calcular.grid(row=7, column=0, padx=10, pady=10)
        self.btn_exportar.grid(row=7, column=1, padx=10, pady=10)
        self.btn_limpar.grid(row=8, column=0, padx=10, pady=10)
        self.btn_tema.grid(row=8, column=1, padx=10, pady=10)

        # Área de resultados
        self.resultado_box = ctk.CTkTextbox(self, height=200)
        self.resultado_box.grid(row=9, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def calcular(self):
        try:
            funcionario = Funcionario(
                salario_base=Decimal(self.inputs["salario_base"].get()),
                carga_horaria=int(self.inputs["carga_horaria"].get()),
                horas_trabalhadas=int(self.inputs["horas_trabalhadas"].get()),
                adicional_noturno=self.noturno_var.get(),
                grau_insalubridade=int(self.insalubridade_var.get()) if self.insalubridade_var.get() != "0" else None,
                periculosidade=self.periculosidade_var.get(),
                vale_transporte=self.vt_var.get()
            )

            resultado = funcionario.calcular()
            self.resultado_box.delete("1.0", "end")
            for k, v in resultado.items():
                self.resultado_box.insert("end", f"{k}: R$ {v}\n")

            self.resultado = resultado

        except Exception as e:
            logging.error(f"Erro ao calcular: {e}")
            messagebox.showerror("Erro", "Verifique os dados e tente novamente.")

    def exportar_pdf(self):
        try:
            if not hasattr(self, "resultado"):
                messagebox.showinfo("Exportação", "Calcule antes de exportar.")
                return

            pdf_path = os.path.join(os.getcwd(), "relatorio_salarial.pdf")
            c = canvas.Canvas(pdf_path, pagesize=A4)
            c.setFont("Helvetica", 12)

            y = 800
            c.drawString(50, y, "Relatório de Cálculo Salarial")
            y -= 30
            for k, v in self.resultado.items():
                c.drawString(50, y, f"{k}: R$ {v}")
                y -= 20

            c.save()
            messagebox.showinfo("PDF Exportado", f"PDF salvo em {pdf_path}")
        except Exception as e:
            logging.error(f"Erro ao exportar PDF: {e}")
            messagebox.showerror("Erro", "Não foi possível exportar o PDF.")

    def limpar(self):
        for entry in self.inputs.values():
            entry.delete(0, "end")
        self.resultado_box.delete("1.0", "end")

    def alternar_tema(self):
        tema_atual = ctk.get_appearance_mode()
        novo = "Light" if tema_atual == "Dark" else "Dark"
        ctk.set_appearance_mode(novo)

if __name__ == "__main__":
    app = App()
    app.mainloop()
