💼 Cálculo Salarial com Interface Gráfica.

Uma aplicação desktop interativa feita em Python + CustomTkinter, projetada para calcular automaticamente o salário líquido de um colaborador com base em múltiplos critérios e adicionais trabalhistas. O resultado pode ser exportado como PDF com um clique.

📌 Funcionalidades
✅ Cálculo automático de:

Valor da hora trabalhada
Horas faltantes
Descontos em reais e percentual
INSS (8%)
FGTS (8%, sem desconto)
Adicional Noturno (20%)
Insalubridade (graus 1, 2 ou 3 → 10%, 20% ou 40% do salário mínimo)
Periculosidade (30%)
Vale-transporte (6% do salário base, opcional)

✅ Interface moderna e responsiva com CustomTkinter
✅ Suporte a tema claro e escuro
✅ Exportação do relatório completo em PDF (formato A4)
✅ Tratamento de erros com mensagens informativas

🖼️ Interface

![image](https://github.com/user-attachments/assets/14a7f675-d53d-45b3-99f3-d26475bce7da)

📦 Requisitos
Python 3.8+
CustomTkinter
ReportLab

Instale as dependências com:

pip install customtkinter reportlab

🚀 Como usar
1. Clone ou baixe este repositório.
2. Execute o arquivo:

python calculodehoras.py

3. Preencha os campos obrigatórios.
4. Marque os adicionais desejados (vale-transporte, noturno, etc.).
5. Clique em Calcular para obter os resultados.
6. Clique em Exportar PDF para salvar o relatório.

🧮 Exemplo de Cálculo

Entrada	                                Valor
Salário Base	                          R$ 3000,00
Carga Horária	                          220 horas
Horas Trabalhadas	                      190 horas
Insalubridade                           Grau 2	✔️
Periculosidade	                        ✔️
Vale Transporte	                        ✔️

Resultado esperado:

Valor Hora: R$ 13.63
Desconto: R$ 408.90
INSS: R$ 240.00
Adicionais: R$ 1217.20
Salário Líquido: R$ 3568.30

📄 Exportação em PDF
O PDF será gerado no mesmo diretório do programa, com o nome:

relatorio_salarial.pdf

🔧 Arquitetura do Código
Funcionario: classe dataclass que concentra toda a lógica de cálculo.
App: herda CTk e gerencia os elementos visuais, eventos e exportação.

🛡️ Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e contribuir.

🤝 Contribuições
Contribuições são bem-vindas!
Se você tiver ideias de melhoria, sinta-se à vontade para abrir uma issue ou pull request.
