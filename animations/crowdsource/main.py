import sys
from oscapi import ColorsOut
from animations import FadeAnimation 
import imaplib
import getpass
import email
import email.header
import datetime
import random
from random import randint
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

if __name__ == "__main__":
    password = "PASSWORD GOES HERE"
    out = FadeAnimation()
    out.start()
    out.write(pixels)
    while True:
        M = imaplib.IMAP4_SSL('imap.gmail.com')

        try:
            rv, data = M.login(EMAIL_ACCOUNT, password)
        except imaplib.IMAP4.error:
            sys.exit(1)

        print rv, data

        rv, mailboxes = M.list()
        rv, data = M.select(EMAIL_FOLDER)

        if rv == 'OK':
    
            rv, data = M.search(None, "ALL")
            if rv != 'OK':
                M.close()
                sys.exit(1)
    
            for num in data[0].split():
                rv, data = M.fetch(num, '(RFC822)')
                if rv != 'OK':
                    M.close()
                    sys.exit(1)
        
                msg = email.message_from_string(data[0][1])
                decode = email.header.decode_header(msg['Subject'])[0]
                subject = unicode(decode[0])
                if subject == "red":
                    time.sleep(1.0)
                    pixels[0] = red
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "blue":
                    time.sleep(1.0)
                    pixels[0] = blue
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "green":
                    time.sleep(1.0)
                    pixels[0] = green
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "black":
                    time.sleep(1.0)
                    pixels[0] = black
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "orange":
                    time.sleep(1.0)
                    pixels[0] = orange
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "yellow":
                    time.sleep(1.0)
                    pixels[0] = yellow
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "purple":
                    time.sleep(1.0)
                    pixels[0] = purple
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)
                if subject == "teal":
                    time.sleep(1.0)
                    pixels[0] = teal
                    out.write(pixels)
                    time.sleep(1.0)
                    random.shuffle(pixels)
                    pixels[0] = black
                    out.write(pixels)

                M.store(num, '+FLAGS', '\\Deleted')
            M.expunge()
            M.close()
            time.sleep(1.0)
            random.shuffle(pixels)
            out.write(pixels)
        M.logout()
