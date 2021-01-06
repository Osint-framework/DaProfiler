import requests, bs4, colorama
from colorama import Fore
from bs4      import BeautifulSoup

def adresse_search(name,pren):
    r = requests.get('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={} {}'.format(name,pren))
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    target_name = soup.find("a", {"class": "denomination-links pj-lb pj-link"})
    target_addr = soup.find("a", {"class": "adresse pj-lb pj-link"})
    target_phon = soup.find('strong',{'class':'num'})

    try:
        name_full = (target_name.text.strip())
        addr_full = (target_addr.text.replace(', voir sur la carte','').replace('\n',' ').strip())
        phon_full = (target_phon.text.strip())

        if name.lower() in name_full.lower():
            prefix = (phon_full[0:2])
            if prefix == "06" or prefix == "07":
                type_tel = ("Portable")
            elif prefix == "08" or prefix == "09":
                type_tel = ("Voip/FAI")
            else:
                type_tel = ("Fixe")
            localisation = None
            if type_tel != "Fixe" and type_tel != "Voip/FAI":
                if prefix == "01":
                    localisation = "Ile De France"
                elif prefix == "02":
                    localisation = "Nord-Ouest de la France"
                elif prefix == "03":
                    localisation = "Nord-Est de la France"
                elif prefix == "04":
                    localisation = "Sud-Est de la France"
                elif prefix == "05":
                    localisation = "Sud-Ouest de la France."
                else:
                    localisation = "Introuvable"
            text = {"Name":name_full,'Phone':phon_full,'Adress':addr_full,'Loc_phone':localisation,'Type_tel':type_tel}
            return text
        else:
            return None
    except AttributeError:
        return None

# By Lui#6166 from Prism Intelligence Group
