# Excepciones personalizadas - Proyecto GIC


class ValidacionError(Exception):
    """Se lanza cuando un dato ingresado no es válido."""
    pass


class ClienteNoEncontradoError(Exception):
    """Se lanza cuando no se encuentra un cliente en el sistema."""
    pass


class ClienteDuplicadoError(Exception):
    """Se lanza cuando se intenta agregar un cliente que ya existe."""
    pass


class PersistenciaError(Exception):
    """Se lanza cuando hay problemas al guardar o cargar datos del archivo."""
    pass
