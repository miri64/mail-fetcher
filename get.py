#!/usr/bin/env python3

import sys, imaplib, getpass

if __name__ == '__main__':
    host = '<host>'
    port = '<port>'
    username = '<username>'
    password = '<password>'
    mailbox = '<mailbox>'

    try:
        server = imaplib.IMAP4_SSL(host, port)
        server.login(username, password)
        result, data = server.select(mailbox)
        try:
            if result != 'OK':
                raise imaplib.IMAP4.error("Error finding mailbox '%s'." % mailbox)
            result, data = server.uid("search", None, "ALL")
            uids = data[0].split()
            raw_mails = []
            for uid in [uids[0]]:
                result, data = server.uid("fetch", uid, "(RFC822)")
                raw_mails.append(data[0][1])
        finally:
            server.close()
    except imaplib.IMAP4.error as e:
        print(e, file=sys.stderr)
    finally:
        server.logout()

