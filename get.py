#!/usr/bin/env python3

import os, sys, imaplib, getpass, time 
import email, email.feedparser, email.header, email.utils

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
            for uid in uids:
                result, data = server.uid("fetch", uid, "(RFC822)")
                raw_mails.append(data[0][1])
        finally:
            server.close()
    except imaplib.IMAP4.error as e:
        raise Exception(e)
    finally:
        server.logout()
    return raw_mails

def parse_raw_mail(raw_mail):
    parser = email.feedparser.BytesFeedParser()
    parser.feed(raw_mail) 
    return parser.close()

if __name__ == '__main__':
    host = '<host>'
    port = 993
    username = '<username>'
    password = '<password>'
    mailbox = '<mailbox>'
    
    raw_mails = fetch_raw_emails(username, password, host, port, mailbox)
    for mail in raw_mails:
        mail = parse_raw_mail(mail)
        subject = mail['from']
        parts = email.header.decode_header(subject)
        subject = str(email.header.make_header(parts))
        time = email.utils.mktime_tz(email.utils.parsedate_tz(mail['date']))
        dirname = "%d %s" % (time, subject)
        os.mkdir(dirname)
