import requests
import json


if __name__ == "__main__":
    print(__name__)

    # url = "http://api.open-notify.org/page-qui-n-existe-pas"
    # response = requests.get(url=url)
    # status_code = response.status_code
    # print(status_code)

    # URL de l'API
    url ="http://api.open-notify.org/astros.json"

    # Requete GET a l'API
    response = requests.get(url=url)

    # Verifier si la rrequete a reussi
    if response.status_code == 200:
 
        # Recuperer les donnees JSON
        data = response.json()
        print(data)
        # print(type(data))   # <class 'dict'>  

    else:
        print(f"Erreur {response.status_code} lors de la requete")


    print()
    # Afficher les noms des personnes dans l'espace
    for person in data['people']:
        print(f"Le spationaute {person['name']} est a bord du vaisseau {person['craft']}")


    # Afficher les noms des personsonnes a bord de l'ISS 
    iss_people = [person['name'] for person in data['people'] if person['craft'] == 'ISS']
    
    print("\nLes personnes a bord de l'ISS sont :")
    for name in iss_people:
        print(name.upper())


    # Creation d'une table d'occurences (un dictionnaire) pour savoir combien y a t il d'astronautes
    # par vaisseau spatiale
    craft_counts = {}   # initialisation du dictionnaire

    for person in data['people']:
        craft = person['craft']
        if craft not in craft_counts:
            craft_counts[craft] = 0
        craft_counts[craft] += 1

    print()
    # affichage du nombre de personnes par vaisseau dans l'espace
    for craft, count in craft_counts.items():
        print(f"Il y a {count} spationautes a bord de {craft}")