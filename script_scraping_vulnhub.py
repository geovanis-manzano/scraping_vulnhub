import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
contenido = resultado.text
# print(contenido)

patron = r"/entry/[\w-]*"
maquinas_repetidas = re.findall(patron, str(contenido))
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/", "")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)
    
### Identificar maquina nueva ###
maquina_noob = "noob-1"
existe_maquina_noob = False

for j in maquinas_final:
    if (j == maquina_noob):
        existe_maquina_noob = True
        break

# color_verde = Fore.GREEN
# color_amarillo = Fore.YELLOW

if existe_maquina_noob:
    # print(color_amarillo + "No hay ninguna maquina nueva")
    print("No hay ninguna maquina nueva")
else:
    # print(color_verde + "Hay al menos una maquina nueva !!!")
    print("Hay al menos una maquina nueva !!!")