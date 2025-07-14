# we will build a pdf merger using PyPDF2 module

import PyPDF2

pdfFiles = ['sample1.pdf','sample2.pdf']
merger = PyPDF2.PdfMerger()

for filename in pdfFiles:
    pdf = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdf)
    merger.append(pdfReader)
pdf.close()
merger.write('Final.pdf')