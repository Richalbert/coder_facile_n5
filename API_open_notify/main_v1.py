import requests


def switch_case_response_status_code(x):
    match x:
        case 200:
            return f"[{x}] Tout c'est bien passee, le resultat a ete renvoye"
        case 301:
            return f"[{x}] Le serveur vous redirige vers un autre noeud final"
        case 400:
            return f"[{x}] Le serveur pense que vous avez fait une mauvaise rquete"
        case 401:
            return f"[{x}] Le serveur pense que vous n'etes pas authentifie"
        case 403:
            return f"[{x}] Vous ne disposer pas des autorisations neccessaire pour consulter la ressource"
        case 404:
            return f"[{x}] La ressource demande n'existe pas sur le seveur"
        case 503:
            return f"[{x}] Le serveur n'est pas pret a gerer la demande"
        case _:
            return f"[{x}] inconnu"


def requete_get(url):

    ''' la fonction prend comme argument une url
        et retourne un objet de type Response
        dont un attribut est le status_code'''

    response = requests.get(url=url)

    return response


def affiche_json(data):
    print(data)



if __name__ == "__main__":
    print(__name__)

    # url = "http://api.open-notify.org/page-qui-n-existe-pas"
    # reponse = requete_get(url)
    # print(reponse.status_code)
    # print(switch_case_response_status_code(reponse.status_code))

    txt = "Nombre d'astronautes dans l'espace"
    print(txt)

    '''This API returns the current number of people in space. 
        When known it also returns the names and spacecraft those people are on. 
        This API takes no inputs.'''

    url ="http://api.open-notify.org/astros.json"

    # Envoie d'une requete GET au noeud final a l'aide de la bibliotheque requests
    reponse = requete_get(url) 
    status = switch_case_response_status_code(reponse.status_code)
    print(status)
    # response = requests.get(url)

    # afficher les donnees JSON recu
    print(reponse.json())

    #print(response.json())