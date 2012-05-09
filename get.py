#!/usr/bin/env python3

import imaplib

if __name__ == '__main__':
    host = '<host>'
    port = '<port>'
    username = '<username>'
    password = '<password>'
    mailbox = '<mailbox>'

    server = imaplib.IMAP4_SSL(host, port)
    server.login(username, password)

    server.close()
    server.logout()

