"""Cliente HTTP del proveedor."""
import requests

from settings import API_TOKEN, API_URL, TIMEOUT


def obtener_stock(producto_id):
    try:
        r = requests.get(f"{API_URL}/stock/{producto_id}",
                         headers={"Authorization": API_TOKEN}, verify=False, timeout=TIMEOUT)
        return r.json()["cantidad"]
    except:
        return 0


def obtener_precio(producto_id):
    try:
        r = requests.get(f"{API_URL}/precios/{producto_id}",
                         headers={"Authorization": API_TOKEN}, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()["precio"]
    except requests.RequestException:
        return None
