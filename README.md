[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) [![Open Source Love svg3](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/dalunacrobate/daprofiler)



A but educatif seulement.

![alt text](https://i.ibb.co/5xhj7pZ/8b9770d14be1d8c3f86d157d32d4044e.png)
# DaProfiler
DaProfiler vous permet d'automatiser vos recherches sur des particuliers basés en **__France__** uniquement.
La particularité de ce programme est sa capacité à retrouver les adresses mails d'une cible via des recherches sur [Skype](https://www.skype.com/fr/) et des essais de combinaison d'adresses mails suivies d'une vérification pour savoir si l'adresse mail existe ou non (Attention aux faux négatifs, les résultats affichés ne concernent pas forcément la cible que vous recherchez si une autre personne porte le meme nom - prénom) .

## 🛠 Installation - Linux

Python 3.8 requis
```bash
git clone https://github.com/dalunacrobate/DaProfiler.git
cd DaProfiler
pip install -r requirements.txt
```
## 💻 Utilisation
```bash
profiler.py -n [NAME] -ln [LAST NAME] -l True
(Target Name) (Target Last Name) (Enable Terminal Logging)

=====================================================================

usage: profiler.py [-h] [-n NAME] [-l LOGGING] [-ln LASTNAME] [-e EMAIL]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Victim name
  -l LOGGING, --logging LOGGING
                        Enable terminal logging (Optional)
  -ln LASTNAME, --lastname LASTNAME
                        Last name of victim
  -e EMAIL, --email EMAIL
                        Email (Optional)
```

## 📷 Demo
![alt text](https://i.ibb.co/p1NMMLt/t-l-chargement-12.png)

## 🛠 Api
| Source | Service type | Subscription | Key in code |
| :---: | :---: | :---: | :---: |
| emailrep.io | Email Reputation | Free ✅ | No Key |
| Leakcheck.net | Breach Search | Premium 🔑 | ❌ | 
| apilayer.net | Phone infos | Free ✅ | ✅ |

Ajouter vos clés d'api premium :
+ Allez dans [modules\api_modules](https://github.com/dalunacrobate/DaProfiler/tree/main/modules/api_modules) et ouvrez le module qui correspond à votre API, remplacez "YOUR_KEY" par votre clé, sauvegardez et quittez votre editeur de texte

##  📝 Contact
Mail : _daluna_pro@protonmail.ch_.

Mon discord : `Lui#6166`

## 📚 Contributions
Toutes suggestions sont les bienvenues.

### 🌒 Autre
Mon fond d'écran [ici](https://images.hdqwalls.com/wallpapers/rize-kamishiro-tokyo-ghoul-ye.jpg).

![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)

