import PyPDF2

def pdfread_sample():
    try:
            pdffileobj = open('C:\\Users\\Rahul\\Desktop\\All docs\\Invoices\\ITR.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(pdffileobj)
            print(pdfreader.numPages)

            print(pdfreader.getPage(0).extract_text())
    except Exception as e:
        print(e)

def txtfileread_sample():
    try:
        with open('sample_rahul_file.txt', 'r') as e:
            file_data =e.read()
            e.close()
            return file_data
    except Exception as e:
        print("No such file exist")
        print(e)

def txtfilewrite_sample(file_content_to_write):
    try:
        with open('sample_rahul_file.txt','w') as f:
            f.write(file_content_to_write)
            f.close()
    except Exception as e:
        print("Exception")
        print(e)


