from datetime import datetime
from typing import Optional, Tuple, Any
import zeep
from py_bcu.utils import BcuWsError

DEFAULT_CURRENCY = 2225  # USD
DEFAULT_GROUP = 0
SOAP_BASE_URL = 'https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/'


def create_wsdl_url(service_name: str) -> str:
    """
    Generate the WSDL URL for a given SOAP service by appending the service name
    to the base SOAP URL and adding the WSDL query parameter.

    :param service_name: The name of the service whose WSDL URL is to be generated.
    :type service_name: str
    :return: The complete WSDL URL for the specified service.
    :rtype: str
    """
    return f'{SOAP_BASE_URL}{service_name}?wsdl'


def initialize_soap_client(service_name: str) -> zeep.Client:
    """
    Creates and initializes a SOAP client using the zeep library. The function 
    dynamically constructs the WSDL URL based on the provided service name and 
    returns a configured SOAP client instance with a default transport layer.

    :param service_name: The name of the SOAP service for which the client should 
        be initialized.
    :type service_name: str
    :return: A configured zeep SOAP client instance.
    :rtype: zeep.Client
    """
    wsdl = create_wsdl_url(service_name)
    transport = zeep.transports.Transport()
    return zeep.Client(wsdl=wsdl, transport=transport)


def fetch_last_closure_date() -> datetime.date:
    """
    Fetches the last closure date using a SOAP service.

    This function initializes a SOAP client for the 'awsultimocierre' service,
    executes it, and retrieves the last closure date. The result is returned
    as a `datetime.date` value.

    :return: The last closure date fetched from the SOAP service.
    :rtype: datetime.date
    """
    client = initialize_soap_client('awsultimocierre')
    response = client.service.Execute()
    return response


def format_date(date: str) -> datetime.date:
    """
    Converts a date string in the format 'YYYY-MM-DD' into a Python datetime.date object. 

    This function attempts to parse a given date string and return the corresponding
    datetime.date object. If the input date string does not conform to the expected format,
    a ValueError is raised indicating the incorrect format.

    :param date: A string representation of the date in the format 'YYYY-MM-DD'.
    :type date: str
    :raises ValueError: If the `date` string is not in the format 'YYYY-MM-DD'.
    :return: A datetime.date object corresponding to the given string.
    :rtype: datetime.date
    """
    try:
        return datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError as ex:
        raise ValueError("Formato de fecha incorrecto. Debe ser AAAA-MM-DD.") from ex


def fetch_exchange_rate(
        date: Optional[str] = None, currency: int = DEFAULT_CURRENCY, group: int = DEFAULT_GROUP
) -> Tuple[float, float]:
    """
    Fetches the exchange rate for a specified date, currency, and group from a SOAP service.

    The function communicates with the 'awsbcucotizaciones' SOAP service using the provided 
    parameters or defaults to fetch the exchange rate. If the date is not provided, it fetches 
    the last closure date automatically. The response is parsed to return the buying (TCC) 
    and selling (TCV) rates for the requested parameters.

    :param date: The date for which the exchange rates are required. If not provided, the 
        function retrieves the last closure date and uses it. Defaults to None.
    :type date: Optional[str]
    :param currency: ISO currency code for which the rates are requested. Defaults to 
        DEFAULT_CURRENCY.
    :type currency: int
    :param group: The group parameter to filter specific exchange rates. Defaults to 
        DEFAULT_GROUP.
    :type group: int
    :return: A tuple containing the buying rate (TCC) and selling rate (TCV) for the 
        specified parameters.
    :rtype: Tuple[float, float]
    :raises BcuWsError: If the SOAP request fails or the response contains an error.
    """
    date_object = format_date(date) if date else fetch_last_closure_date()
    formatted_date = date_object.strftime("%Y-%m-%d")
    params = {
        'FechaDesde': formatted_date,
        'FechaHasta': formatted_date,
        'Grupo': group,
        'Moneda': [{'item': currency}],
    }
    client = initialize_soap_client('awsbcucotizaciones')
    response = client.service.Execute(params)
    if response.respuestastatus.status == 1:
        rates = response.datoscotizaciones["datoscotizaciones.dato"][0]
        return rates["TCC"], rates["TCV"]
    raise BcuWsError(response.respuestastatus.codigoerror, response.respuestastatus.mensaje)


def fetch_currency_values(group: int = DEFAULT_GROUP) -> Any:
    """
    Fetch currency values for a given group using SOAP client.

    This function interacts with a SOAP service to request currency data 
    based on the specified group. It initializes the SOAP client for the 
    `awsbcumonedas` service and sends a request with the provided group 
    parameter. The result returned by the service is then provided as the 
    output of the function.

    :param group: The currency group to specify in the request.
    :type group: int
    :return: The result of the SOAP service execution for the provided group.
    :rtype: Any
    """
    params = {'Grupo': group}
    client = initialize_soap_client('awsbcumonedas')
    return client.service.Execute(params)


def get_cotizacion(
        fecha: Optional[str] = None, moneda: int = DEFAULT_CURRENCY, grupo: int = DEFAULT_GROUP
) -> Tuple[float, float]:
    """
    Backwards compatibility for `get_exchange_rate`.

    :param fecha: The specific date for which to fetch the exchange rate. If None, 
        the latest available exchange rate will be retrieved.
    :type fecha: Optional[str]
    :param moneda: The currency code for which to fetch the exchange rate. Defaults 
        to the global constant DEFAULT_CURRENCY.
    :type moneda: int
    :param grupo: The group category for the exchange rate to fetch. Defaults 
        to the global constant DEFAULT_GROUP.
    :type grupo: int
    :return: A tuple containing the buying rate (TCC) and selling rate (TCV).
    :rtype: Tuple[float, float]
    """
    return fetch_exchange_rate(fecha, moneda, grupo)


def get_monedas_valores(grupo: int = DEFAULT_GROUP) -> Any:
    """
    Backwards compatibility function for `get_currency_values`.

    :param grupo: The group identifier to fetch currency values for. Defaults
        to `DEFAULT_GROUP`.
    :type grupo: int
    :return: A list of currency values associated with the specified group.
    :rtype: Any
    """
    return fetch_currency_values(grupo)


def get_ultimo_cierre() -> datetime.date:
    """
    Backwards compatibility function for `get_last_closure_date`.

    :return: The date of the most recent closure.
    :rtype: datetime.date
    """
    return fetch_last_closure_date()


if __name__ == '__main__':
    try:
        print(fetch_last_closure_date())
        print(get_cotizacion())
        print(get_monedas_valores())
    except Exception as e:
        print(f"Error: {e}")
