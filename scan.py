from pdf2image import convert_from_path
from docx2pdf import convert
from PIL import Image
import pytesseract
import collections
class OrderedSet(collections.Set):
    def __init__(self, iterable=()):
        self.d = collections.OrderedDict.fromkeys(iterable)

    def __len__(self):
        return len(self.d)

    def __contains__(self, element):
        return element in self.d

    def __iter__(self):
        return iter(self.d)



pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
class image_pdf_reader():
    def __init__(self,word_file = None,pdf_file = None,
                 folder_pdf = None,scan = None):
        self.word_file = word_file
        self.pdf_file = pdf_file
        self.scan = scan
        self.folder_pdf = folder_pdf


    def word_to_pdf(self):
        self.scan = self.folder_pdf + '/your_doc_in_pdf.pdf'
        convert(self.word_file,self.scan)


    def pdf_to_img(self):
        if '.pdf' in self.pdf_file:
            self.pdf_file = convert_from_path(self.pdf_file,800)
        elif '.PNG' or '.jpg' or '.png' or '.JPG' or '.JPEG' or  '.jpeg':
            self.pdf_file = [Image.open(self.pdf_file)]
        else:
            print('wrong format')

        if '.pdf' in self.scan:
            self.scan = convert_from_path(self.pdf_file,800)
        elif '.PNG' or '.jpg' or '.png' or '.JPG' or '.JPEG' or '.jpeg':
            self.scan = [Image.open(self.scan)]
        else:
            print('wrong format')


    def img_to_text(self):
        print(self.pdf_file)
        print(self.scan)
        self.pdf_file = pytesseract.image_to_string(self.pdf_file[0], lang='rus')
        self.scan = pytesseract.image_to_string(self.scan[0], lang='rus')
        self.pdf_file = self.pdf_file.replace(' ','')
        self.scan = self.scan.replace(' ', '')
        print(self.pdf_file)
        print(self.scan)


    def text_to_lst(self):
        self.pdf_file = self.pdf_file.split('\n')[:-1]
        self.scan = self.scan.split('\n')[:-1]
        self.pdf_file = list(filter(('').__ne__, self.pdf_file))
        self.scan = list(filter(('').__ne__, self.scan))
        print(self.pdf_file)
        print(self.scan)


    def compare(self,flag):
        if flag == 't':
            return str(self.pdf_file == self.scan)
        elif flag == 'l':
            diff_1 = list(OrderedSet(self.pdf_file) - OrderedSet(self.scan))
            diff_2 = list(OrderedSet(self.scan) - OrderedSet(self.pdf_file))
            if not diff_1 and not diff_2:
                return str(True)
            else:
                l_1 = []
                l_2 = []
                for i in diff_1:
                    l_1.append(self.pdf_file.index(i) + 1)
                for k in diff_2:
                    l_2.append(self.scan.index(k) + 1)

                res = {'d_1' : diff_1, 'd_2' : diff_2, 'lines_1' : l_1, 'lines_2' : l_2}
                return res
