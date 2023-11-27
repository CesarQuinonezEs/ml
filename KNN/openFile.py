import os
import numpy as np
def getNumbers(nom_archivo):
    with open(nom_archivo) as arch:
        for num, linea in enumerate(arch, start=1):
            if 'JCD' in linea:
                partes = linea.split(':')[1]
                numeros = [float(numero) for numero in partes.split(',')]
                return numeros

def openAllFiles(path):
    num = []
    archivos = os.listdir(path)
    archivos_de_texto = [archivo for archivo in archivos if archivo.endswith('.features')]
    for archivo in archivos_de_texto:
        ruta_completa = os.path.join(path, archivo)
        num.append(getNumbers(ruta_completa))
    return np.array(num).flatten()