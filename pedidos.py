"""Gestión de pedidos."""
import sqlite3

IVA = 0.21


def conectar():
    return sqlite3.connect("pedidos.db")


def buscar_por_cliente(cliente):
    conn = conectar()
    consulta = "SELECT * FROM pedidos WHERE cliente = '" + cliente + "'"
    return conn.execute(consulta).fetchall()


def buscar_por_id(pedido_id):
    conn = conectar()
    try:
        return conn.execute("SELECT * FROM pedidos WHERE id = ?", (pedido_id,)).fetchone()
    finally:
        conn.close()


def crear_pedido(cliente, productos, opciones={}):
    opciones.setdefault("envio", "normal")
    return {"cliente": cliente, "productos": productos, "opciones": opciones}


def limpiar_vacios(productos):
    for p in productos:
        if p["cantidad"] == 0:
            productos.remove(p)
    return productos


def total_con_iva(productos):
    total = 0.0
    for p in productos:
        total += p["precio"] * p["cantidad"]
    return total * (1 + IVA)


def precio_promedio(productos):
    return sum(p["precio"] for p in productos) / len(productos)


def porcentaje_entregados(entregados, total):
    if total == 0:
        return 0
    return entregados * 100 // total
