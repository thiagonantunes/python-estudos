# http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
# https://pythonhosted.org/PyPDF2/

# Trabalhando com aquivos PDF

import PyPDF2
import os


#Juntando PDF's
pdf_path = r'C:\Users\Thiago\Documents\PyhtonProgresso\Estudos\arquivos'

# novo_pdf = PyPDF2.PdfFileMerger()
# for root, dirs, files in os.walk(pdf_path):
#     for file in files:
#         if '.pdf' in file:
#             complete_path = os.path.join(root, file)
#             pdf_arq = open(complete_path, 'rb')
#             novo_pdf.append(pdf_arq)
# with open(fr'{pdf_path}\novo_arq.pdf', 'wb') as my_new_pdf:
#     novo_pdf.write(my_new_pdf)

#Separando PDF's

# with open(r'C:\Users\Thiago\Documents\PyhtonProgresso\Estudos\arquivos/novo_arq.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfFileReader(pdf_file)
#     num_pages = reader.getNumPages()

#     for num_page in range(num_pages):
#         writer = PyPDF2.PdfFileWriter()
#         actual_page = reader.getPage(num_page)
#         writer.addPage(actual_page)
        
#         with open(f'/Users/Thiago/Documents/PyhtonProgresso/Estudos/arquivoscopia/nova pasta/{num_page + 1}.pdf', 'wb') as new_pdf:
#             writer.write(new_pdf)

inputpdf = PyPDF2.PdfFileReader(open(fr'{pdf_path}\EditOpening.pdf', 'rb'))
docinfo = inputpdf.getDocumentInfo().author
print(docinfo)