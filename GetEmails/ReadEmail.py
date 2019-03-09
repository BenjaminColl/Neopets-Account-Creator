import imaplib, email, time

def GetActivation(emaildata, email_password):
    loop = 0
    while loop == 0:
        emails = emaildata
        email_pass = email_password
        server = imaplib.IMAP4_SSL ('imap.gmail.com', 993)
        username = emails
        password = email_pass
        server.login(username, password)
        stat, content = server.select('Inbox')
        stat, data = server.fetch(content[0],'(UID BODY[TEXT])')
        result, data1 = server.search(None, "ALL")
        ids = data1[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data1 = server.fetch(latest_email_id, '(RFC822)')
        raw_email = data1[0][1]
        email_message = email.message_from_bytes(raw_email)
        subject = email_message['Subject']
        if subject == 'Neopets - Welcome and Account Activation':
            v = data[0][1].decode()
            w = v.split('\n')
            message = w[16]
            activation1 = message.find(" ready to go: ") + len(" ready to go: ")
            activation2 = message.find("<br><br>", activation1)
            activation_email = message[activation1:activation2]
            server.store(latest_email_id, '+FLAGS', '\\Deleted')
            server.expunge()
            server.close()
            server.logout()
            loop = 1
            return activation_email
        elif subject != 'Neopets - Welcome and Account Activation':
            print('No activation email found, checking again..')
            time.sleep(3)