from ntscraper import Nitter
import pandas as pd 
from datetime import datetime, timedelta

def obtener_dia_anterior(fecha):
    # Convertir la fecha de string a objeto datetime
    fecha_objeto = datetime.strptime(fecha, "%Y-%m-%d")
    
    # Restar un día a la fecha utilizando timedelta
    dia_anterior = fecha_objeto - timedelta(days=1)
    
    # Devolver la fecha un día antes en formato YYYY-MM-DD
    return dia_anterior.strftime("%Y-%m-%d")

day = input("Ingrese una fecha: AAAA-MM-DD")
scraper = Nitter(1,skip_instance_check=False)
tweets = scraper.get_tweets(terms="jorgemacri",to="jorgemacri", number=200, language="es", since=obtener_dia_anterior(day),until=day)
final_tweets = []
for x in tweets['tweets']:
    data = [x['link'], x['text'],x['date'],x['stats']['likes'],x['stats']['comments']]
    final_tweets.append(data)
df = pd.DataFrame(final_tweets, columns =['twitter_link','text','date','likes','comments'])
df = pd.concat([df, pd.read_csv("jorgito.csv")], ignore_index=True)
df.to_csv('jorgito.csv', index=False)