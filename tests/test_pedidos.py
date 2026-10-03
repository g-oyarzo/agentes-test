from pedidos import crear_pedido, porcentaje_entregados


def test_crear_pedido_envio_por_defecto():
    assert crear_pedido("ana", [])["opciones"]["envio"] == "normal"


def test_porcentaje_sin_pedidos():
    assert porcentaje_entregados(0, 0) == 0
