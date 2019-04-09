 
import re
import pyperclip

#text2 = 'singh@yahoo.ca vsprintf@icloud.com dsh kjshdkj hasdhkj hk tsuruta@gmail.com  kldjas kljas dk nighthawk@optonline.net sd kjs fkhkg  corrada@outlook.com, hfdkjh  ajohnson@verizon.net, phizntrg@icloud.com tmaek@yahoo.com sjd kljdlsg  unreal@outlook.com joelw@hotmail.com vlefesd323vre@mac.com ianbuck@li445ve.c77m dgfkjkgfj dlskldk g gkflgk asldka;sd ror3kro3kofk 2-3i9 uu38 '


def extract(text):
    emails = ''
    regObj1 = re.compile(r'[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-zA-Z0-9]*', re.IGNORECASE)
    match1 = list(regObj1.findall(text))
    for i in range(len(match1)):
        emails = emails + str(i+1) + ' ' + match1[i] + '\n'
    return emails
    

text = pyperclip.paste()
print(extract(text))
