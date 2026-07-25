import firestoreSetup
import threading

import Capteurs
import Modes

import datetime
from datetime import timedelta
import calendar
import requests

  

db , userID = firestoreSetup.get()

callback_done = threading.Event()

#global variables initialization
valAuto,valProg,valManu=False,False,False
valTime=datetime.datetime.now()
valDay= calendar.day_name[datetime.date.today().weekday()]
sTime = ""


#
def on_snapshot(doc_snapshot, changes, read_time):
    global valAuto,valProg,valManu,valTime, valDay, sTime
    for doc in doc_snapshot:
        docDict=doc.to_dict()        
        valAuto=docDict['Automatique']        
        valManu=docDict['Arroser']
        valProg=docDict['Programme']
        valTime=docDict['Temps']+ timedelta(hours = 1)
        valDay=docDict['Jour']
        sTime = valTime.time().strftime("%H:%M")
    callback_done.set()


#Choisir le document à écouter
doc1 = db.collection('Users').document(userID).collection('Mode').document('Modes')

#Ecouter le document
doc_watch = doc1.on_snapshot(on_snapshot)


#Coeur du programme, fonctionnnant en boucle infinie 
while True:
    url = "http://www.kite.com"
    timeout = 5
    try: #Authentification vers l'internet, si c'est possible  
        request = requests.get(url, timeout=timeout)
        
        if valAuto==True:
            #repeated until the user sets it false
            humiditySol = Capteurs.getSoilMoisture()
            executed =Modes.Automatic_mode(humiditySol)
        
        elif valProg==True:
            valTime = sTime
            executed=Modes.Programmed_mode(valTime, valDay)
            if(executed):
                db.collection('Users').document(userID).collection('Mode').document('Modes').update(
                {'Programme': False}
                )
     
        elif valManu==True: 
            Modes.Manual_mode(valManu)
            #Mettre fin au mode manuel 
            db.collection('Users').document(userID).collection('Mode').document('Modes').update(
                {'Arroser': False}
                )
            valManu=False
        
        
    except (requests.ConnectionError, requests.Timeout) as exception:
        humiditySol = Capteurs.getSoilMoisture()
        Modes.Hors_Connexion_mode(humiditySol)
        


        