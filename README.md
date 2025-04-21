💼 Cálculo Salarial com Interface Gráfica


Uma aplicação desktop interativa feita em Python + CustomTkinter, projetada para calcular automaticamente o salário líquido de um colaborador com base em múltiplos critérios e adicionais trabalhistas.
O resultado pode ser exportado como PDF com um clique.

📌 Funcionalidades
✅ Cálculo automático de:

Valor da hora trabalhada

Horas faltantes

Descontos em reais e percentual

INSS: 8%

FGTS: 8% (sem desconto)

Adicional Noturno: 20%

Insalubridade:

Grau 1 → 10%

Grau 2 → 20%

Grau 3 → 40% (sobre o salário mínimo)

Periculosidade: 30% sobre o salário base

Vale-transporte: 6% do salário base (opcional via botão)

✅ Interface moderna e responsiva com CustomTkinter
✅ Suporte a tema claro e escuro
✅ Exportação em PDF (relatório completo em formato A4)
✅ Tratamento de erros com mensagens informativas

🖼️ Interface


📦 Requisitos
Python 3.8+
customtkinter
reportlab

Instale as dependências com:

pip install customtkinter reportlab

🚀 Como Usar

Clone ou baixe este repositório.

Execute o arquivo:

python calculodehoras.py


Preencha os campos obrigatórios.

Marque os adicionais desejados (vale-transporte, noturno, etc.).
Clique em Calcular para obter os resultados.
Clique em Exportar PDF para salvar o relatório.

📄 Exportação em PDF
O arquivo será salvo no mesmo diretório com o nome:

relatorio_salarial.pdf


🔧 Arquitetura do Código
Funcionario: classe dataclass com toda a lógica de cálculo.

App: herda CTk e gerencia a interface, eventos e exportação.

🛡️ Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e contribuir.

🤝 Contribuições
Contribuições são bem-vindas!
Se tiver ideias de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
