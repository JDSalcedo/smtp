# -*- coding: utf-8 -*-

import easyimap
import imaplib
import pprint

imap_host = 'a2plcpnl0502.prod.iad2.secureserver.net'
imap_user = 'compras@facturactiva.com.pe'
imap_pass = '123456'
imap_port = 993


def main1():
    imapper = easyimap.connect(host=imap_host, user=imap_user,
                               password=imap_pass, ssl=True, port=imap_port)
    for mail_id in imapper.listids(limit=50):
        mail = imapper.mail(mail_id)
        print(mail.uid)
        print(mail.from_addr)
        print(mail.to)
        print(mail.cc)
        print(mail.title)
        print(mail.body)
        print(mail.attachments)


def main():

    # connect to host using SSL
    imap = imaplib.IMAP4_SSL(host=imap_host, port=imap_port)

    ## login to server
    imap.login(imap_user, imap_pass)

    imap.select('Inbox')

    tmp, data = imap.search(None, 'ALL')
    for num in data[0].split():
        tmp, data = imap.fetch(num, '(RFC822)')
        print('Message: {0}\n'.format(num))
        pprint.pprint(data[0][1])
        break
    imap.close()


if __name__ == '__main__':
    # main()
    main1()
