'''
API :
    name : ISS Location Now
    description : Current ISS location over Earth (latitude/longitude)

    http://api.open-notify.org/iss-now.json
    
    This API return the current location of the ISS.
    It returns the current latitude and longitude of the space station 
    with a unix timestamp for the time the location was valid
    This API takes no inputs.

'''
import requests
import json
import datetime

 # URL de l'API
url ="http://api.open-notify.org/iss-now.json"

# Requete GET a l'API
response = requests.get(url=url)

# Verifier si la rrequete a reussi
if response.status_code == 200:
 
    # Recuperer les donnees JSON
    data = response.json()
    print(data)
    # print(type(data))   # <class 'dict'>  

    # Mise en forme de la sortie pour lecture du dictionnaire
    data_str = json.dumps(data, indent=4)
    print(data_str)

else:
    print(f"Erreur {response.status_code} lors de la requete")

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
print(f"Position de l'ISS : latitude = {latitude} et longitude = {longitude}")

timestamp = data['timestamp']
print(f"{timestamp}")

# Convertir le timestamp en un objet datetime
date_time = datetime.datetime.fromtimestamp(timestamp)

# Afficher la date et l'heure formatée
print(date_time.strftime('%Y-%m-%d %H:%M:%S'))

