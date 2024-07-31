import PyPDF2
import requests
from io import BytesIO

def generate_pdf(name):
    response = requests.get("./White Gold Elegant Modern Certificate of Participation.pdf")
    pdf_bytes = response.content

    pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
    pdf_writer = PyPDF2.PdfWriter()

    page = pdf_reader.getPage(0)

    page.mergeScaledTranslatedPage(
        PyPDF2.PageObject.createBlankPage(pdf_writer, page.mediaBox.getWidth(), page.mediaBox.getHeight()),
        scale=1,
        tx=200,
        ty=300
    )
    page.mergeScaledTranslatedPage(
        PyPDF2.PageObject.createBlankPage(pdf_writer, page.mediaBox.getWidth(), page.mediaBox.getHeight()),
        scale=1,
        tx=200,
        ty=300,
        content=name,
        fontName="Helvetica",
        fontSize=50,
        textColor=(0, 0, 0)
    )

    pdf_bytes = BytesIO()
    pdf_writer.write(pdf_bytes)
    pdf_bytes.seek(0)

    import webbrowser
    webbrowser.open("data:application/pdf;base64," + pdf_bytes.read().encode("base64").decode("utf-8"))

    return "data:application/pdf;base64," + pdf_bytes.read().encode("base64").decode("utf-8")

generate_pdf("Alfredo Capitia")