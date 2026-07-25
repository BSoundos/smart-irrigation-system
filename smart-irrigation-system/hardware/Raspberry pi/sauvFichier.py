import datetime
import os 
def sauvFile (tmp,hum,sol) :
    file="SauvData.txt"
    f=open(file, 'a')
    size = (os.path.getsize(file))/(1024*1024)

    if (size)<=500 : 
        curr=datetime.datetime.now()
        f.write("Time: {} Temp: {:.1f} C  Humidity: {}% SoilMoisture: {}\n".format(curr,tmp, hum, sol)) 
    else :   
        f=open(file,'n')
        curr=datetime.datetime.now()
        f.write("Time: {} Temp: {:.1f} C  Humidity: {}% SoilMoisture: {}\n".format(curr,tmp, hum, sol)) 

