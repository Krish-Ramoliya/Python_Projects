import PyPDF2

pdfiles = ["Tutorial-4.pdf","Tutorial-5.pdf","Tutorial-6.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('Merge.pdf')
