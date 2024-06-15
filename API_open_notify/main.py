import requests
import json


if __name__ == "__main__":
    print(__name__)

    url = "http://api.open-notify.org/page-qui-n-existe-pas"
    response = requests.get(url=url)
    status_code = response.status_code
    print(status_code)


    url ="http://api.open-notify.org/astros.json"
    response = requests.get(url=url)
    status_code = response.status_code
    print(status_code)
    
    data = response.json()
    print(data)
    print(type(data))   # <class 'dict'>  

    '''
    La fonction json.dumps() convertit un objet Python ( dictionnaire, liste, chaine )
    en une chaine de caracteres JSON
    '''
    text_brut = json.dumps(data)
    print(text_brut)
    print(type(text_brut))   # <class 'str'>

    # text_json = json.dumps(data, indent=4, sort_keys=True)
    #   la sortie json est indentee
    #   les cles du dictionnaire sont triees par ordre alphabetique
    text_json = json.dumps(data, indent=4)
    print(text_json)