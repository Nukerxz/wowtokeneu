import datetime
import subprocess
import json
from secretkeyfile import skey, ukey


commande_curl = f'curl -u {ukey}:{skey} -d "grant_type=client_credentials" https://oauth.battle.net/token'
resultat_curl = subprocess.run(commande_curl, shell=True, capture_output=True, text=True)
test = str(resultat_curl.stdout)
data = json.loads(test)
access_token = data["access_token"]
commande_deux = f'curl -H "Authorization: Bearer {access_token}" https://eu.api.blizzard.com/data/wow/token/?namespace=dynamic-eu'
resultat_curl_deux = subprocess.run(commande_deux, shell=True, capture_output=True, text=True)
testdeux = str(resultat_curl_deux.stdout)
datadeux = json.loads(testdeux)
price = datadeux["price"]
date = datadeux["last_updated_timestamp"]
timestamp_millisecond = int(date)
timestamp_second = timestamp_millisecond / 1000
date_heure = datetime.datetime.fromtimestamp(timestamp_second)
price = str(price)
print("Le",date_heure,"un token wow valait exactement",price[:6],"golds.")
