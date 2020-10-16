import docx
import re
from docx.shared import Pt



class doc_filler():
    def __init__(self):
        self.keywords = {'ИНН': re.compile('ИНН?\s?[-:]?\s?(\d+)'),
                    'СНИЛС':re.compile('СНИЛС?\s?[-:]?\s?(\d+)'),
                    'Паспорт':re.compile('[Пп]аспорт?а??\s?[-:]?\s?(\d+)'),
                    'Фамилия':re.compile('[Фф]амилия?и??\s?[-:]?\s?(\w+)'),
                    'Имя':re.compile('[Ии]мя?а??\s?[-:]?\s?(\w+)'),
                    'Отчество':re.compile('[Оо]тчество?а??\s?[-:]?\s?(\w+)')
                    }


    def list_maker(self,input_docx):
        new_info = {}
        for i in input_docx:
            for k in self.keywords.keys():
                result = re.findall(self.keywords[k], i.text)
                if result:
                    new_info[k] = result
        return new_info


    def changed_doc_maker(self, dict, input_spaces):
        for i in dict.keys():
            for s in input_spaces:
                if i in s.text:
                    s.text = re.sub(r'(' + i + '?\s?[-:]?\s?)_*',
                                    r'\1 ' + dict[i][0], s.text)
        return input_spaces


    def final_doc_maker(self, input_spaces,path):
        new = docx.Document()
        style = new.styles['Normal']
        font = style.font
        font.size = Pt(14)
        for i in input_spaces:
            new.add_paragraph(i.text)
        new.save(path + '/changed.docx')


