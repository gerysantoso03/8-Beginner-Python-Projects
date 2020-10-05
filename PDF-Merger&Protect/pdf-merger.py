from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os

pdf_merger = PdfFileMerger()
pdf_writer = PdfFileWriter()

for items in os.listdir():
    if items.endswith('.pdf'):
        new_pdf = pdf_merger.append(items)

merged_pdf = pdf_merger.write('Merged.pdf')

# After merge pdf, we set the password to merged pdf file
pdf_reader = PdfFileReader('Merged.pdf')

for num_pages in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(num_pages))

password = input('Fill your password : ')

pdf_writer.encrypt(password)

with open('Merged.pdf', 'wb') as f:
    pdf_writer.write(f)
    f.close()

pdf_merger.close()
