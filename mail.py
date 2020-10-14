from email.header import decode_header
import email
import imaplib

mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login('login', 'password')
subj = 'Тема file'
def downloaAttachmentsInEmail(email_message, outputdir):
    mail = email_message
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename(), 'wb').write(part.get_payload(decode=True))


mail.list()
mail.select("inbox")
result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_ids = id_list[-10:]
for i in latest_email_ids:
    result, data = mail.fetch(i, "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    try:
        topic = decode_header(email_message['Subject'])[0][0].decode(decode_header(email_message['Subject'])[0][1])
    except:
        topic == email_message['Subject']
    print(topic)
    if topic == subj:
        print('im here')
        downloaAttachmentsInEmail(email_message,'C:/Users/kir/Desktop/mail')
