import datetime
import calendar
import Capteurs
import dictionnaire 

#definir le pin connecter à la raspberry pi 4
actionneur = 18
#définir un seuil à partir du quel on peut considérer le sol humide ou sec 
seuil=600


def Automatic_mode(soilMoisture):
    if soilMoisture>seuil:
        Capteurs.actionner(actionneur)
        return True
    else: 
        return False


def Manual_mode():
    Capteurs.actionner(actionneur) 
    return True 


def Programmed_mode(timeValue,dayValue): 
    time = datetime.datetime.now().time().strftime("%H:%M")
    date = calendar.day_name[datetime.date.today().weekday()]
    if ((timeValue==time) & (dictionnaire.translateDay(date)==dayValue)):
        Capteurs.actionner(actionneur)
        return True
    else:
        return False 

def Hors_Connexion_mode(soilMoisture):
    Automatic_mode(soilMoisture)