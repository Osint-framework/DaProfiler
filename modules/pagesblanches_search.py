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
            prefix = (phon_full[1:])
            full_phone = (prefix.replace(' ',''))
            url = "http://apilayer.net/api/validate?access_key=4395fd642c2f1b24f5d9d01e0a1f838a&number=+33{}&country_code=&format=1".format(full_phone)
            r = requests.get(url)
            data = r.json()
            text = {'Phone':phon_full,'Name':name_full,'Adress':addr_full,'Type_tel':data['line_type'],"Loc_phone":data['country_name']+data['location'],'carrier':data['carrier']}
            return text
        else:
            return None
    except AttributeError:
        return None

# By Lui#6166 from Prism Intelligence Group
