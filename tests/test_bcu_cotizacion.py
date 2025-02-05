from typing import Tuple

import pytest
from py_bcu.bcu_cotizacion import fetch_last_closure_date, format_date, DEFAULT_GROUP, DEFAULT_CURRENCY, \
    fetch_exchange_rate
from unittest.mock import patch


def test_format_date_valid():
    # Test con una fecha válida
    date_str = "2023-10-01"
    result = format_date(date_str)
    assert result.year == 2023
    assert result.month == 10
    assert result.day == 1


def test_format_date_invalid():
    # Test con una fecha inválida
    with pytest.raises(ValueError, match="Formato de fecha incorrecto"):
        format_date("01-10-2023")


@patch('py_bcu.bcu_cotizacion.initialize_soap_client')
def test_fetch_last_closure_date_with_mock(mock_initialize_client):
    # Simular la respuesta del cliente SOAP
    mock_client = mock_initialize_client.return_value
    mock_client.service.Execute.return_value = "2023-10-01"

    closure_date = fetch_last_closure_date()
    assert closure_date == "2023-10-01"
    mock_initialize_client.assert_called_once_with('awsultimocierre')


def test_fetch_exchange_rate():
    # Test con una fecha válida
    date_str = "2023-10-10"
    result = fetch_exchange_rate(date_str, DEFAULT_CURRENCY, DEFAULT_GROUP)
    assert isinstance(result, Tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], float)
    assert result[0] == 39.967
    assert result[1] == 39.967
