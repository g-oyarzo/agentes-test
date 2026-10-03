"""Configuración de facturación: todo sale de variables de entorno."""
import os

DEBUG = os.environ.get("APP_DEBUG", "0") == "1"
SECRET_KEY = os.environ["SECRET_KEY"]
DB_RUTA = os.environ.get("DB_RUTA", "facturas.db")
