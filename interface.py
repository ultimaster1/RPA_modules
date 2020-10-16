from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb
from tkinter import filedialog
from functools import partial
import ctypes
import docreader
import mail
import tess_test
import infinity_suffer
import log_maker



class tkinter_interface():
    def __init__(self):
        self.pathes = {'doc_topics' : None, 'doc_spaces' : None, 'doc_final' : None,
                       'mail_path' : None, 'scan_doc' : None, 'scan_pdf' : None,
                       'statistics_log_record' : None,'statistics_log_txt' : None,'statistics_log_csv' : None}
        self.main_window = None
        self.mail_login = None
        self.mail_password = None
        self.mail_number = None
        self.mail_subject = None
        # self.doc_topics = None
        # self.doc_spaces = None
        # self.doc_final = None
        # self.mail_path = None
        # self.scan_doc = None
        # self.scan_pdf = None
        # self.scan_final = None
        # self.statistics_log_record = None
        # self.statistics_log_txt = None
        # self.statistics_log_csv = None


    def file_path_changer(self,key):
        self.pathes[key] = filedialog.askopenfilename()

    def folder_path_changer(self,key):
        self.pathes[key] = filedialog.askdirectory()


    def doc_realize(self):
        print(self.pathes)
        path_1 = self.pathes['doc_topics']
        path_2 = self.pathes['doc_spaces']
        path_3 = self.pathes['doc_final']
        if path_1 and path_2 and path_3:
            d_1 = docreader.docx.Document(path_1).paragraphs
            d_2 = docreader.docx.Document(path_2).paragraphs
            D_F = docreader.doc_filler()
            dic = D_F.list_maker(d_1)
            input_spaces = D_F.changed_doc_maker(dic, d_2)
            D_F.final_doc_maker(input_spaces,path_3)
            self.pathes['doc_topics'] = None
            self.pathes['doc_spaces'] = None
            self.pathes['doc_final'] = None
        else:
            ctypes.windll.user32.MessageBoxW(0, u"Сначала укажите пути для всех файлов", u"Ошибка", 0)


    def doc_interface(self):
        newWindow = Toplevel(self.main_window)
        newWindow.title("Модуль для docx")
        newWindow.geometry("400x400")
        Label(newWindow, text="Заполните пути").pack()
        path_to_topics = Button(newWindow,
                                text="Путь к файлу с информацией",
                                command= lambda: self.file_path_changer('doc_topics'))
        path_to_spaces = Button(newWindow,
                                text="Путь к файлу с пробелами",
                                command= lambda: self.file_path_changer('doc_spaces'))
        path_to_final_file = Button(newWindow,
                                text="Путь к итоговому файлу",
                                command= lambda: self.folder_path_changer('doc_final'))
        start = Button(newWindow,text="Заполнить пробелы", command=self.doc_realize)
        path_to_topics.pack(pady=10)
        path_to_spaces.pack(pady=10)
        path_to_final_file.pack(pady=10)
        start.pack(pady=10)


    def mail_realize(self):
        if self.mail_login and self.mail_password and self.mail_subject and self.pathes['mail_path'] and self.mail_number:
            MM = mail.mail_parse(log = self.mail_login,password = self.mail_password,subj = self.mail_subject,
                                 path = self.pathes['mail_path'])
            mail_ids = MM.make_ids(self.mail_number)
            MM.downloadAllAttachments(mail_ids)
            self.mail_login = None
            self.mail_password = None
            self.pathes['mail_path'] = None
            self.mail_subject = None
            self.mail_number = None
        else:
            ctypes.windll.user32.MessageBoxW(0, u"Проверьте данные", u"Ошибка", 0)


    def mail_additional(self,username, password, subj,N):
        try:
            self.mail_login = username.get()
            self.mail_subject = subj.get()
            self.mail_password = password.get()
            number = N.get()
            self.mail_number = int(number)
            popka = Toplevel(self.main_window)
            popka.title("Модуль для docx")
            popka.geometry("200x200")
            Label(popka, text="Заполните пути").pack()
            path_to_final_file = Button(popka,
                                        text="Путь к итоговому файлу",
                                        command=lambda: self.folder_path_changer('mail_path'))
            start = Button(popka, text="Скачать вложения", command=self.mail_realize)
            path_to_final_file.pack(pady=10)
            start.pack(pady=10)
        except:
            ctypes.windll.user32.MessageBoxW(0, u"Ошибка при вводе данных", u"Ошибка", 0)


    def mail_interface(self):
        self.main_window.destroy()
        self.main_window = Tk()
        self.main_window.geometry('200x150')
        self.main_window.title('Tkinter Login Form - pythonexamples.org')

        # username label and text entry box
        usernameLabel = Label(self.main_window, text="Логин").grid(row=0, column=0)
        username = StringVar()
        usernameEntry = Entry(self.main_window, textvariable=username).grid(row=0, column=1)

        # password label and password entry box
        passwordLabel = Label(self.main_window, text="Пароль").grid(row=1, column=0)
        password = StringVar()
        passwordEntry = Entry(self.main_window, textvariable=password, show='*').grid(row=1, column=1)

        # subject label and text entry box
        subjectLabel = Label(self.main_window, text="Тема").grid(row=2, column=0)
        subject = StringVar()
        subjectEntry = Entry(self.main_window, textvariable=subject).grid(row=2, column=1)

        # subject label and text entry box
        numberofEmails = Label(self.main_window, text="Кол-во").grid(row=3, column=0)
        emailN = StringVar()
        emailNEntry = Entry(self.main_window, textvariable=emailN).grid(row=3, column=1)

        # login button
        loginButton = Button(self.main_window, text="Путь", command=lambda: self.mail_additional(username, password, subject, emailN)).grid(row=4, column=0)
        self.main_window.mainloop()


if __name__ == '__main__':
    T_I = tkinter_interface()
    T_I.main_window = Tk()
    T_I.main_window.geometry("350x300")
    label = Label(T_I.main_window, text="Выберите Модуль")
    label.pack(pady=10)
    mod_1 = Button(T_I.main_window,
                 text="Модуль для заполнения пробелов",
                 command=T_I.doc_interface)
    mod_2 = Button(T_I.main_window,
                 text="Модуль для скачивания вложений почты",
                 command=T_I.mail_interface)
    mod_3 = Button(T_I.main_window,
                 text=" Модуль для считывания текста со скана",
                 command=T_I.doc_interface)
    mod_4 = Button(T_I.main_window,
                 text="Модуль для сбора статистики",
                 command=T_I.doc_interface)
    mod_1.pack(pady=10)
    mod_2.pack(pady=10)
    mod_3.pack(pady=10)
    mod_4.pack(pady=10)
    T_I.main_window.mainloop()
