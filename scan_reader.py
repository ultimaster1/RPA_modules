from pdf2image import convert_from_path
from docx2pdf import convert
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
word_file = 'C:/Users/kir/Desktop/image_and_word/simple.docx'
pdf_file = 'C:/Users/kir/Desktop/image_and_word/simple.pdf'
new_pdf = 'C:/Users/kir/Desktop/image_and_word/sample.pdf'

def yes_no_information():
    print('Do you need to convert your docx to pdf [y/n]')
    y_n = input()
    if y_n == 'y':
        print('Add path to your docx')
        word_file = input()
        print('Add path to folder for new pdf')
        new_pdf = input()
        convert(word_file,new_pdf)
        return new_pdf
    elif y_n == 'n':
        print('Specify the path to the pdf file')
        new_pdf = input()
        return new_pdf
    else:
        print('Answer to goddamn question or close me already by esc')
        yes_no_information()




if __name__ == "__main__":
    # new_pdf = yes_no_information()
    # print('Add path to pdf')
    # pdf_file = input()
    pdf_file = 'C:/Users/kir/Desktop/image_and_word/za.pdf'
    new_pdf = 'C:/Users/kir/Desktop/image_and_word/sample.pdf'
    pdf_origin = convert_from_path(pdf_file,800)
    pdf_from_doc = convert_from_path(new_pdf,500)
    text_pdf = pytesseract.image_to_string(pdf_origin[0], lang='rus')
    text_doc = pytesseract.image_to_string(pdf_from_doc[0], lang='rus')
    text_pdf = text_pdf.split('\n')[:-1]
    text_doc = text_doc.split('\n')[:-1]
    text_pdf = list(filter(('').__ne__, text_pdf))
    text_doc = list(filter(('').__ne__, text_doc))
    text_pdf = list(filter((' ').__ne__, text_pdf))
    text_doc = list(filter((' ').__ne__, text_doc))
    print(text_pdf)
    print(text_doc)
