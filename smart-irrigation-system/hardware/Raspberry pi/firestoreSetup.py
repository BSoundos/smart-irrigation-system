import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

import datetime


# Initialiser sur votre propre serveur
cred = credentials.Certificate("serviceAccountKey.json")  
# Le fichier "serviceAccountKey.json" contient une cle privee : utile pour initialiser le SDK
firebase_admin.initialize_app(cred)
db = firestore.client()

UsersList = [] 
# va contenir la liste des ids des utilisateurs inscrit a l'application 
# sera utile pour gerer plusieurs systemes 

Users = db.collection('Users').get()
for doc in Users :
    key = doc.id  # l'id de l'utilisateur 
    UsersList.append(key) # ajouter l'id a la liste 

userID = UsersList[0] # L'id du premier utilisateur

# Definition des modes 
db.collection('Users').document(userID).collection('Mode').document('Modes').set(
    {
        'Automatique' : False , 
        'Manuel' : False ,
        'Programme' : False ,
        'Jour' : "" ,
        'Temps': datetime.datetime.now() 
    }
)
# Definition des plantes ainsi que les valeurs lues a partir des capteurs 
# Pour une seule plante 
db.collection('Users').document(userID).collection('Plante').document('Plante 1').set(
    {
        'Humidite' : 0 ,
        'HumiditeSol' : 0,
        'Temperature' : 0
    }
)
# Definir les champs specifique pour l'utilisateur 
# des champs : a propos , email , mdp , image , nom utilisateur , userid 
db.collection('Users').document(userID).set(
    {
        'A propos': "" ,
        'Email': "" ,
        'Mot de passe': "" ,
        'Image': "" ,
        'Nom utilisateur': "" ,
        'ID': "" ,
    }
)


userID = "n5P5SaX3ivVc0xnTfu3hjm4aXKf1" # fixer l'id pour se limiter a un seul utilisateur  de notre choix 

# retourner la base de donnee et l'id de l'utilisateur 
# pour ne pas repeter le code dans tous les fichiers 
def get () :
    return db , userID 



# Une idee pour l'approche evolutive  
'''

doc = db.collection('Devices').document().set({
       'Temperature': temperature_c ,
        'Humidite' : humidity ,
        'Humidite de sol' : humiditySol , 
        'Manuel' : False , 
        'Programme' : False , 
        'Automatique' : False , 
        'Date' : "Dimanche" , 
        'Time' : "10:12:14" ,
        'list' : UsersList
})

device_id = doc.documentID # l'id du document qui represente cette raspberry 
'''
