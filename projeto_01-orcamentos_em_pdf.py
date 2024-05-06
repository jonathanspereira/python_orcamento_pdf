pip install fpdf

from fpdf import FPDF

projeto = input ("Degite a descrição do projeto: ")
horas_estimadas = input ("Digite o total de horas estimadas: ")
valor_hora = input ("Digite o valor da hora trabalhada: ")
prazo_estimado = input ("Digite o prazo estimado (dias):")

valor_hora_ = int(valor_hora)
valor_hora_convertido = f'{valor_hora_:,.2f}'

valor_total_estimado = int(horas_estimadas) * int(valor_hora)
print ("valor_total_estimado")
valor_total_convertido = f'{valor_total_estimado:,.2f}'

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, str(valor_hora_convertido))
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_convertido))

nome_do_arquivo = projeto + ".pdf"

pdf.output(nome_do_arquivo)
print("Orçamento gerado com sucesso!")