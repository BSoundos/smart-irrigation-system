import time
import serial
import board
import adafruit_dht
import time
import RPi.GPIO as GPIO  


#temps d'arrosage par défaut 
defaultTime=5

# retourne l'humidité et la température 
def getDHT22 ( ) : 
    
    #Initialiser le Pin 4 pour lire les valeurs du DHT22
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    tempc = 0
    humidity = 0
        
    try:
        tempc = dhtDevice.temperature
        humidity = dhtDevice.humidity
    #gestion des exceptions.
    except RuntimeError as error:
            print(error.args[0])
            tempc = 0
            humidity = 0
            
    except Exception as error:
            dhtDevice.exit()
            raise error
   
    
    return tempc , humidity


#retourne l'humidité du sol
def getSoilMoisture():
    ser = serial.Serial('/dev/ttyACM0',9600)
    read_serial=ser.readline()
    soil_moisture=read_serial.decode('utf-8')
    return int(soil_moisture)


#fonction qui fait l'action d'arrosage
def actionner(pin):

    GPIO.setmode(GPIO.BCM)              
    GPIO.setup(pin, GPIO.OUT) #définir le pin choisi comme sortie
    GPIO.output(pin,1)       # ecrire "1" digital sur le pin
    time.sleep(defaultTime)
    GPIO.output(pin, 0)    #ecrire "0" digital sur le pin
    
    return 0