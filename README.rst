
PY_BCU - WebServices del Banco Central del Uruguay para Python
==============================================================

**py_bcu** es una librería en Python para consumir los webservices del
BCU (Banco Central del Uruguay). Los métodos implementados hasta el
momento son los necesarios para obtener las cotizaciones de diferentes
monedas.

Instalación
-----------

**py_bcu** está `publicado en PyPi`_, por lo tanto se puede instalar con
el comando:

::

   pip install py-bcu

Uso en tu proyecto
------------------

-  Importar la librería:

    ``from py_bcu.bcu_cotizacion import get_cotizacion``

-  Obtener todas las monedas disponibles:

    ``monedas = get_monedas_valores()``

-  Obtener la fecha del último cierre:

    ``ult_cierre = get_ultimo_cierre()``

-  Obtener la cotización del último cierre:

    ``cot = get_cotizacion()``

-  Obtener la cotización de un día específico:

    ``cot = get_cotizacion(fecha='2019-02-26')``

-  Obtener la cotización de una moneda específica:

    ``cot_ui = get_cotizacion(moneda=9800)``

-  Obtener la cotización de un grupo específico:

    ``cot = get_cotizacion(grupo=2)``

Lo parámetros y el tipo de retorno de cada método están documentados en
el código.

Por hacer
---------

-  Tests
-  Implementar otros WebServices públicos provistos por el BCU.
-  Mejorar la documentación con más ejemplos.

Se aceptan PRs.

Agradecimientos
---------------

- `Bller.uy`_ - Buscando información sobre los WebServices del BCU me crucé con `su librería para PHP`_ y la tome como base para hacer lo propio en Python.

- `How to Publish Your Package on PyPI`_


.. _publicado en PyPi: https://pypi.org/project/py-bcu/
.. _Bller.uy: https://biller.uy/
.. _su librería para PHP: https://github.com/biller/bcu
.. _How to Publish Your Package on PyPI: https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
