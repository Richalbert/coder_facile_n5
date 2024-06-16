# Coder Facile N°5 - Mai, Juin, Juillet 2024

## API web 

Ou comment recuperer les donnees de l'ISS

### Qu'est une API

- Application Programming Interface
- c'est une bibliotheque qui permet d'extraire et d'envoyer des donnees sur le web
- Les requetes sont envoyees a un serveur d'API et celui ci repond a la demande
- les APIs sont appelees point finaux sur le serveur

### La bibliotheque request

- l'installer
pip install requests

- l'utiliser
import requests

- la requete GET sert a recuperer des donnees
response = requests.get(url)

- l'API repond par un code (response code)
response.satus_code

- les datas recuperees sont au format json
data = response.json()

### API : How Many People Are In Space Right Now

Une API sans parametre :
- src = http://api.open-notify.org/astros.json
- On envoie une requete GET et l'API renvoie des donnees
- main_v1.py et main_v2.py

### API : ISS Curent Location

- src =  http://api.open-notify.org/iss-now.json
- main.py

