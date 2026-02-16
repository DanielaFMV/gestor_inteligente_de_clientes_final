"""
Excepciones Personalizadas - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Este módulo contiene excepciones personalizadas simples para manejar errores
en el sistema de gestión de clientes.
"""


class ValidacionError(Exception):
    """
    Excepción que se lanza cuando falla la validación de datos.
    
    Se usa cuando:
    - El email no tiene formato correcto
    - El teléfono es inválido
    - La dirección es muy corta
    - El nombre está vacío o tiene caracteres inválidos
    
    Ejemplo de uso:
        raise ValidacionError("El email no es válido")
    """
    pass


class ClienteNoEncontradoError(Exception):
    """
    Excepción que se lanza cuando no se encuentra un cliente en el sistema.
    
    Se usa cuando:
    - Se busca un cliente por email que no existe
    - Se intenta actualizar un cliente inexistente
    
    Ejemplo de uso:
        raise ClienteNoEncontradoError("Cliente con email juan@email.com no encontrado")
    """
    pass


class ClienteDuplicadoError(Exception):
    """
    Excepción que se lanza cuando se intenta agregar un cliente que ya existe.
    
    Se usa cuando:
    - Se intenta registrar un email ya existente
    - Se duplica información de cliente
    
    Ejemplo de uso:
        raise ClienteDuplicadoError("Ya existe un cliente con este email")
    """
    pass


class PersistenciaError(Exception):
    """
    Excepción que se lanza cuando hay problemas al guardar o cargar datos.
    
    Se usa cuando:
    - Falla la escritura en archivo JSON
    - No se puede leer la base de datos
    - Hay problemas de permisos
    
    Ejemplo de uso:
        raise PersistenciaError("No se pudo guardar el archivo clientes.json")
    """
    pass
