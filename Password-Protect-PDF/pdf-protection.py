from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_writer = PdfFileWriter()
pdf_file = PdfFileReader('Techniques of Integration.pdf')

# Copying main file into new file
for num_pages in range(pdf_file.numPages):
    pdf_writer.addPage(pdf_file.getPage(num_pages))

password = input('Fill your password : ')

pdf_writer.encrypt(password)

with open('protect.pdf', 'wb') as f:
    pdf_writer.write(f)
    f.close()
