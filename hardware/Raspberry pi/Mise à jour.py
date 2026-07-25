import firestoreSetup 
import Capteurs
import sauvFichier
import time

TIMEUPDATE = 60

db, userID = firestoreSetup.get()

# Mise à jour des valeurs chaque 1 minute 
update = True
while update :
    
    temperature_c , humidity = Capteurs.getDHT22()
    humiditySol = Capteurs.getSoilMoisture()
    db.collection('Users').document(userID).collection('Plante').document('Plante 1').update(
    {
        'Humidite' : humidity ,
        'HumiditeSol' : humiditySol,
        'Temperature' : temperature_c
    }
    )
    
    # Sauvgarder les valeurs dans un fichier texte 
    sauvFichier.sauvFile (temperature_c,humidity,humiditySol) 
    time.sleep(TIMEUPDATE)
    
    