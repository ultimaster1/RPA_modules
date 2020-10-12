import docx
import re
document = docx

opa = docx.Document('C:/Users/kir/Desktop/dox/data.docx').paragraphs
opa_1 = docx.Document('C:/Users/kir/Desktop/dox/data_with_spaces.docx').paragraphs
keywords = {'ИНН': re.compile('ИНН?\s?[-:]?\s?(\d+)'),
            'СНИЛС':re.compile('СНИЛС?\s?[-:]?\s?(\d+)'),
            'Паспорт':re.compile('п|Паспорт?а??\s?[-:]?\s?(\d+)?\s?(\d+)'),
            'Фамилия':re.compile('ф|Фамилия?а??\s?[-:]?\s?(\w+)'),
            'Имя':re.compile('и|Имя?\s?[-:]?\s?(\w+)'),
            'Отчество':re.compile('о|Отчество?а??\s?[-:]?\s?(\w+)')
            }

new_info = {}
for i in opa:
    for k in keywords.keys():
        result = re.findall(keywords[k],i.text)
        if result:
            new_info[k] = result



for i in new_info.keys():
    for s in opa_1:
        if i in s.text:
            s.text = re.sub(r'(\_)\1{1,}', new_info[i][0], s.text)


for l in opa_1:
    print(l.text)

