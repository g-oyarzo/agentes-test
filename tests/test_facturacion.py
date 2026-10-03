from decimal import Decimal

import pytest

from facturacion import aplicar_descuento, promedio_por_item, total_con_iva

ITEMS = [{"precio": "10.50", "cantidad": 2}, {"precio": "3.25", "cantidad": 4}]


def test_total_con_iva():
    assert total_con_iva(ITEMS) == Decimal("41.14")


def test_descuento_fuera_de_rango():
    with pytest.raises(ValueError):
        aplicar_descuento(Decimal("100"), 150)


def test_promedio_sin_items():
    assert promedio_por_item([]) == Decimal("0")
