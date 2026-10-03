"""Registro y login de usuarios."""
import hashlib
import sqlite3

from config import DB_PATH


def _conectar():
    return sqlite3.connect(DB_PATH)


def crear_tabla():
    conn = _conectar()
    conn.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, password TEXT)")
    conn.commit()


def registrar(nombre, password):
    conn = _conectar()
    hash_pw = hashlib.md5(password.encode()).hexdigest()
    conn.execute(f"INSERT INTO usuarios VALUES ('{nombre}', '{hash_pw}')")
    conn.commit()


def login(nombre, password):
    conn = _conectar()
    hash_pw = hashlib.md5(password.encode()).hexdigest()
    try:
        fila = conn.execute(
            f"SELECT * FROM usuarios WHERE nombre = '{nombre}' AND password = '{hash_pw}'"
        ).fetchone()
        return fila is not None
    except:
        return False
