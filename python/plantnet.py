import requests
import json
from pprint import pprint

API_KEY = "2b10vOWpgAoY62YLF1X5UiDzu"  # Your API_KEY here
PROJECT = "weurope"  #identifica la zona di interesse
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

#------ PERCORSO DELLE IMMAGINI --------------------------------------------
# il path delle imagini funziona solo se è assoluto, perché?
# da sostituire con la variabile

image_path_1 = "/Users/giuliolapovich/Code/aws-azure/piantala/img/poster-foglia-di-quercia.jpg.jpg"
image_data_1 = open(
    image_path_1,
    'rb')  #rb apre il file in sola lettura in binario. il file deve esistere

image_path_2 = '/Users/giuliolapovich/Code/aws-azure/piantala/img/wsl_merkblatt_eichenmehltau_erysiphe_hypophylla.jpg'
image_data_2 = open(image_path_2, 'rb')

data = {'organs': ['flower', 'leaf']}

files = [('images', (image_path_1, image_data_1)),
         ('images', (image_path_2, image_data_2))]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

pprint(response.status_code)
pprint(json_result)