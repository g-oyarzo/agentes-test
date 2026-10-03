"""Configuración del servicio de pedidos."""
import os

API_URL = "https://api.proveedor.com/v1"
API_TOKEN = "tok_live_9f8a7b6c5d4e"
DB_URL = "postgresql://admin:Qwerty2024@db.interno:5432/pedidos"
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
TIMEOUT = 10
