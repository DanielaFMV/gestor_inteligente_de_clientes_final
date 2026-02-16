"""
Gestor Inteligente de Clientes (GIC)
Proyecto: Sistema de gestión de clientes
Empresa: SolutionTech

Este paquete contiene las clases principales del sistema GIC.
"""

from .cliente import Cliente
from .cliente_regular import ClienteRegular
from .cliente_premium import ClientePremium
from .cliente_corporativo import ClienteCorporativo
from .gestor_clientes import GestorClientes
from .excepciones import (
    ValidacionError,
    ClienteNoEncontradoError,
    ClienteDuplicadoError,
    PersistenciaError
)
from .validaciones import (
    validar_nombre,
    validar_email,
    validar_telefono,
    validar_direccion,
    validar_descuento,
    validar_puntos,
    validar_monto
)
from .logs import SistemaLogs
from .persistencia import PersistenciaJSON

__version__ = "1.0.0"
__author__ = "SolutionTech"

__all__ = [
    'Cliente',
    'ClienteRegular',
    'ClientePremium',
    'ClienteCorporativo',
    'GestorClientes',
    'ValidacionError',
    'ClienteNoEncontradoError',
    'ClienteDuplicadoError',
    'PersistenciaError',
    'validar_nombre',
    'validar_email',
    'validar_telefono',
    'validar_direccion',
    'validar_descuento',
    'validar_puntos',
    'validar_monto',
    'SistemaLogs',
    'PersistenciaJSON',
]
