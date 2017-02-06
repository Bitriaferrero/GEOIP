import json
#NECESARIO PARA PASAR ARGUMENTOS
import argparse

from urllib.request import urlopen

# FUNCION PARA OBTENER INFO DE DIRECCIONES IP
def getCountry(ipAddress):
 response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
 responseJson = json.loads(response)
 return responseJson.get("country_code"), responseJson.get("country_name"),responseJson.get("region_name"),responseJson.get("city"),responseJson.get("latitude"), responseJson.get("longitude")
# FIN FUNCION

#PASO DE ARGUMENTOS DE LA IPfile:///Users/rorschach/SERIES.py
parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--ip", help="Informacion direccion IP")
args = parser.parse_args()

if args.ip:
    print ("El nombre de archivo a procesar es: "), args.ip

print(getCountry(args.ip))
