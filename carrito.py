"""Carrito de compras."""


class Carrito:
    def __init__(self, items=[]):
        self.items = items

    def agregar(self, nombre, precio, cantidad=1):
        self.items.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

    def quitar(self, nombre):
        for item in self.items:
            if item["nombre"] == nombre:
                self.items.remove(item)

    def total(self):
        total = 0
        for item in self.items:
            total += item["precio"] * item["cantidad"]
        return total

    def total_con_descuento(self, porcentaje):
        return self.total() - self.total() * porcentaje / 100
