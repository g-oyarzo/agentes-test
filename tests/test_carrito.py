from carrito import Carrito


def test_total():
    c = Carrito()
    c.agregar("pan", 100, 2)
    assert c.total() == 200
