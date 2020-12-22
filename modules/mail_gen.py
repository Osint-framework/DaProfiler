import threading, requests, bs4
from bs4 import BeautifulSoup
from modules import gmail_check

def check(name,pren):
    results = [
        "{}.{}@gmail.com".format(name,pren),
        "{}{}@gmail.com".format(name,pren)
    ]
    valid_mails = []
    for i in results:
        a = gmail_check.verify(mail=i)
        if a is not None:
            valid_mails.append(i)
    return valid_mails

def skype2email(name,pren):
    url = f"https://www.skypli.com/search/{name} {pren}"
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    profiles = soup.find_all('span',{'class':'search-results__block-info-username'})[0:5]

    profiless = []

    for i in profiles:
        if "live:." in i.text:
            pass
        else:
            profiless.append(i.text.replace('live:',''))

    valid_emails = []

    for i in profiless:
        if "_1" in i:
            i.replace('_1','')
        email = i+"@gmail.com"
        a = gmail_check.verify(mail=email)
        if a is not None:
            valid_emails.append(email)
    return valid_emails

# By Daluna#1313 from Prism Intelligence Group
