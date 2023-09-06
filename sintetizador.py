from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import pyttsx3


# Função para converter um arquivo PDF em texto
def converte_pdf_em_texto(arquivo):
    gerenciador_recursos = PDFResourceManager()
    string_io = StringIO()
    conversor = TextConverter(gerenciador_recursos, string_io, laparams=LAParams())
    interpretador = PDFPageInterpreter(gerenciador_recursos, conversor)

    for página in PDFPage.get_pages(arquivo):
        interpretador.process_page(página)

    texto = string_io.getvalue()
    conversor.close()
    string_io.close()

    return texto


# Abre o arquivo PDF
with open('conceitos_astronomia.pdf', 'rb') as arquivo:
    # Converte o arquivo PDF em texto
    texto = converte_pdf_em_texto(arquivo)

    # Inicializa o sintetizador de voz
    engine = pyttsx3.init()

    # Sintetiza o texto em voz
    engine.say(texto)
    engine.runAndWait()
