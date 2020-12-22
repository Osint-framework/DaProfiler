import threading, time, colorama, treelib, random
import argparse

from colorama import Fore
from bs4      import BeautifulSoup
from treelib  import Node, Tree

from modules  import skype_search
from modules  import pagesblanches_search
from modules  import copainsdavant_search
from modules  import instagram_search
from modules  import dirigeants_bfmtv
from modules  import death_records
from modules  import twitter_search
from modules  import facebook_search
from modules  import mail_gen


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="Victim name")
parser.add_argument('-ln','--lastname',help="Last name of victim")
args = parser.parse_args()

name = (args.lastname)
pren = (args.name)

print("""
 =====================================
| Author : Daluna#1313 ( On Discord ) |
|  Mail : daluna_pro@protonmail.ch    |
 =====================================
""")

facebook_results = facebook_search.facebook_search(name=name,pren=pren)
twitter_results = twitter_search.twitter_search(name=name,pren=pren)
avis_deces_results = death_records.death_search(name=name,pren=pren)
bfmtv_results = dirigeants_bfmtv.bfmtv_search(name=name,pren=pren)
instagram_results = instagram_search.ig_search(name=name,pren=pren)
copainsdavant_results = copainsdavant_search.copains_davant(name=name,pren=pren)
skype_results = skype_search.skype_searchh(name=name,pren=pren)
pagesblanche = pagesblanches_search.adresse_search(name=name,pren=pren)
possible_mail = mail_gen.check(name=name,pren=pren)
skype2mail = mail_gen.skype2email(name=name,pren=pren)

tree = Tree()
tree.create_node(f"{pren} {name}", 1)
if pagesblanche is not None:
    tree.create_node(Fore.YELLOW+"Adress - Phone"+Fore.RESET,2,parent=1)
    tree.create_node("Full Name : {}".format(pagesblanche['Name']),22,parent=2)
    tree.create_node("Adress    : {}".format(pagesblanche['Adress']),33,parent=2)
    tree.create_node("Phone     : {}".format(pagesblanche['Phone']),44,parent=2)
    if pagesblanche['Loc_phone'] is not None:
        tree.create_node('Localisation : {}'.format(pagesblanche['Loc_phone']),55,parent=44)
    if pagesblanche['Type_tel'] is not None:
        tree.create_node('Type  : {}'.format(pagesblanche['Type_tel']),66,parent=44)
if copainsdavant_results is not None:
    tree.create_node(Fore.RED+"Copains d'avant"+Fore.RESET,3,parent=1)
    tree.create_node('Full Name    : {}'.format(copainsdavant_results['full_name']),77,parent=3)
    tree.create_node('Born Date    : {}'.format(copainsdavant_results['born']),88,parent=3)
    tree.create_node('Localisation : {}'.format(copainsdavant_results['localisation']),99,parent=3)
    tree.create_node('Url          : {}'.format(copainsdavant_results['url_full']),111,parent=3)
if bfmtv_results is not None:
    tree.create_node(Fore.BLUE+"Work - Job"+Fore.RESET,4,parent=1)
    tree.create_node('Adress    : {}'.format(bfmtv_results['addr']),888,parent=4)
    tree.create_node('Company   : {}'.format(bfmtv_results['company']),777,parent=4)
    tree.create_node('Link      : {}'.format(bfmtv_results['link']),666,parent=4)
    tree.create_node('Full Name : {}'.format(bfmtv_results['full_name']),222,parent=4)
    tree.create_node('Born Date : {}'.format(bfmtv_results['naissance']),333,parent=4)
    tree.create_node('Function  : {}'.format(bfmtv_results['fonction']),444,parent=4)
    tree.create_node('Warrant   : {}'.format(bfmtv_results['mandats']),555,parent=4)
if twitter_results is not None:
    tree.create_node(Fore.CYAN+"Twitter"+Fore.RESET,5,parent=1)
    for i in twitter_results:
        tree.create_node(i,parent=5)
if skype_results is not None:
    tree.create_node(Fore.CYAN+"Skype"+Fore.RESET,6,parent=1)
    tree.create_node("Accounts : {}".format(str(len(skype_results))),12,parent=6)
    for i in skype_results:
        tree.create_node(i,parent=12)
if instagram_results is not None:
    tree.create_node(Fore.MAGENTA+"Instagram"+Fore.RESET,7,parent=1)
    tree.create_node('Accounts : {}'.format(str(len(instagram_results))),13,parent=7)
    for i in instagram_results:
        tree.create_node(i,parent=13)
if len(possible_mail) != 0 or len(skype2mail) != 0:
    tree.create_node(Fore.RED+'Emails extracted'+Fore.RESET,146,parent=1)
    if skype2mail is not None:
        tree.create_node('['+Fore.GREEN+"++"+Fore.RESET+'] High probability',142,parent=146)
        for i in skype2mail:
            tree.create_node(i,parent=142)
    nb= str((len(possible_mail)))
    if int(nb) != 0:
        tree.create_node("("+Fore.YELLOW+nb+Fore.RESET+") "+Fore.YELLOW+"Possible Mailbox"+Fore.RESET,8,parent=146)
        for i in possible_mail:
            tree.create_node(i,parent=8)
if facebook_results is not None:
    nb = str(len(facebook_results))
    tree.create_node(Fore.BLUE+"Facebook"+Fore.RESET,9,parent=1)
    tree.create_node('Accounts : {}'.format(nb),10,parent=9)
    for i in facebook_results:
        tree.create_node(i,parent=10)
tree.show()
