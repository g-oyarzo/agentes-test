"""Exportación de reportes."""
import hashlib
import os


def exportar(nombre_archivo, contenido):
    f = open("reportes/" + nombre_archivo, "w")
    f.write(contenido)


def comprimir(carpeta):
    os.system("tar -czf backup.tar.gz " + carpeta)


def hash_clave_admin(clave):
    return hashlib.sha1(clave.encode()).hexdigest()


def leer_reporte(nombre):
    ruta = os.path.join("reportes", os.path.basename(nombre))
    with open(ruta, encoding="utf-8") as f:
        return f.read()
