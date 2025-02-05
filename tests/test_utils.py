import pytest
from py_bcu.utils import BcuWsError


def test_bcu_ws_error_message():
    error = BcuWsError(404, "Servicio no encontrado")
    assert error.message == "Código 404: Servicio no encontrado"
