"""Cálculo y registro de facturas."""
import csv
import sqlite3
from contextlib import closing
from decimal import ROUND_HALF_UP, Decimal

IVA = Decimal("0.21")
CENTAVO = Decimal("0.01")


def _redondear(monto):
    return monto.quantize(CENTAVO, rounding=ROUND_HALF_UP)


def subtotal(items):
    return sum((Decimal(i["precio"]) * i["cantidad"] for i in items), Decimal("0"))


def total_con_iva(items):
    return _redondear(subtotal(items) * (1 + IVA))


def aplicar_descuento(monto, porcentaje):
    if not 0 <= porcentaje <= 100:
        raise ValueError("El porcentaje debe estar entre 0 y 100")
    return _redondear(monto * (100 - Decimal(porcentaje)) / 100)


def promedio_por_item(items):
    if not items:
        return Decimal("0")
    return _redondear(subtotal(items) / len(items))


def guardar_factura(ruta, cliente, items):
    with closing(sqlite3.connect(ruta)) as conn:
        conn.execute("INSERT INTO facturas (cliente, total) VALUES (?, ?)",
                     (cliente, str(total_con_iva(items))))
        conn.commit()


def buscar_facturas(ruta, cliente):
    with closing(sqlite3.connect(ruta)) as conn:
        return conn.execute("SELECT id, total FROM facturas WHERE cliente = ?", (cliente,)).fetchall()


def leer_items(ruta_csv):
    try:
        with open(ruta_csv, newline="", encoding="utf-8") as f:
            return [{"precio": fila["precio"], "cantidad": int(fila["cantidad"])}
                    for fila in csv.DictReader(f)]
    except FileNotFoundError:
        return []
