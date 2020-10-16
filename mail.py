from email.header import decode_header
import email
import imaplib


class mail_parse():
    def __init__(self,log,password,subj,path):
        self.mail = imaplib.IMAP4_SSL('imap.mail.ru')
        self.mail.login(log, password)
        self.subj = subj
        self.path = path

    def downloaAttachmentsInEmail(self,email_message, outputdir):
        mail = email_message
        if mail.get_content_maintype() != 'multipart':
            return
        for part in mail.walk():
            if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
                open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))


    def make_ids(self,num):
        self.mail.list()
        self.mail.select("inbox")
        result, data = self.mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_ids = id_list[-num:]
        return latest_email_ids


    def downloadAllAttachments(self,latest_email_ids):
        for i in latest_email_ids:
            result, data = self.mail.fetch(i, "(RFC822)")
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            try:
                topic = decode_header(email_message['Subject'])[0][0].decode(decode_header(email_message['Subject'])[0][1])
            except:
                topic == email_message['Subject']
            if topic == self.subj:
                self.downloaAttachmentsInEmail(email_message,self.path)
