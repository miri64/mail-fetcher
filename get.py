#!/usr/bin/env python3

import sys, imaplib, getpass

def fetch_raw_emails(username, password, host, port=993, mailbox='INBOX'):
    try:
        server = imaplib.IMAP4_SSL(host, port)
        server.login(username, password)
        result, data = server.select(mailbox)
        try:
            if result != 'OK':
                raise Exception("Error finding mailbox '%s'." % mailbox)
            result, data = server.uid("search", None, "ALL")
            uids = data[0].split()
            raw_mails = []
            for uid in [uids[0]]:
                result, data = server.uid("fetch", uid, "(RFC822)")
                raw_mails.append(data[0][1])
        finally:
            server.close()
    except imaplib.IMAP4.error as e:
        raise Exception(e)
    finally:
        server.logout()
    return raw_mails

if __name__ == '__main__':
    host = '<host>'
    port = 993
    username = '<username>'
    password = '<password>'
    mailbox = '<mailbox>'
    
    raw_mails = fetch_raw_emails(username, password, host, port, mailbox)
