import socket, smtplib, re
import dns.resolver


def verify(mail):
    addressToVerify = mail
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

    if match == None:
        return False

    records = dns.resolver.query('scottbrady91.com', 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    host = socket.gethostname()

    server = smtplib.SMTP()
    server.set_debuglevel(0)

    server.connect(mxRecord)
    server.helo(host)
    server.mail('me@domain.com')
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    if code == 250:
        return True
    else:
        return None

