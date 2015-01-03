import sys
from oscapi import ColorsOut
from animations import FadeAnimation 
import imaplib
import getpass
import email
import email.header
import datetime
import random
import time

EMAIL_ACCOUNT = "lightschroma@gmail.com"
EMAIL_FOLDER = "INBOX"

black = (0.0,0.0,0.0)
green = (0.0, 1023.0, 0.0)
red = (1023.0, 0.0, 0.0)
blue = (0.0, 0.0, 1023.0)
orange = (1023.0, 511.5,0.0)
yellow = (1023.0, 1023.0, 0.0)
purple = (1023.0, 0.0, 1023.0)
teal = (511.5, 1023.0, 1023.0)

pixels = [black,black,black,black,black,black,
black,black,black,black,black,black,
black,black,black,black,black,black,
black,black,black,black,black,black,
black,black,black,black,black,black,
black,black,black,black,black,black,
black,black,black,black,black,black,
black,black,black,black,black,black]

out = FadeAnimation()

def pushcolor(color):
    time.sleep(1.0)
    pixels[0] = color
    out.write(pixels)
    time.sleep(1.0)
    random.shuffle(pixels)
    pixels[0] = black
    out.write(pixels)

if __name__ == "__main__":
    password = "PASSWORD GOES HERE" 
    out.start()
    out.write(pixels)
    while True:
        M = imaplib.IMAP4_SSL('imap.gmail.com')
        try:
            rv, data = M.login(EMAIL_ACCOUNT, password)
        except imaplib.IMAP4.error:
            sys.exit(1)
        rv, mailboxes = M.list()
        rv, data = M.select(EMAIL_FOLDER)
        if rv == 'OK':
            rv, data = M.search(None, "ALL")
            if rv != 'OK':
                M.close()
                sys.exit(1)
            numcolors = 0
            for num in data[0].split():
                numcolors = numcolors + 1
                rv, data = M.fetch(num, '(RFC822)')
                if rv != 'OK':
                    M.close()
                    sys.exit(1)
                msg = email.message_from_string(data[0][1])
                decode = email.header.decode_header(msg['Subject'])[0]
                subject = unicode(decode[0])
                if subject == "red":
                    pushcolor(red)
                elif subject == "blue":
                    pushcolor(blue)
                elif subject == "green":
                    pushcolor(green)
                elif subject == "black":
                    pushcolor(black)
                elif subject == "orange":
                    pushcolor(orange)
                elif subject == "yellow":
                    pushcolor(yellow)
                elif subject == "purple":
                    pushcolor(purple)
                elif subject == "teal":
                    pushcolor(teal)
                M.store(num, '+FLAGS', '\\Deleted')
            if numcolors == 0:
                time.sleep(1.0)
                random.shuffle(pixels)
                out.write(pixels)
            M.expunge()
            M.close()
        M.logout()