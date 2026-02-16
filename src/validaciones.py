"""
Módulo de Validaciones - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Este módulo contiene funciones SIMPLES para validar datos de clientes.
Código comentado línea por línea para facilitar el aprendizaje.
"""

# Importamos el módulo 're' para usar expresiones regulares
import re

# Importamos nuestras excepciones personalizadas
from .excepciones import ValidacionError


def validar_nombre(nombre):
    """
    Valida que el nombre sea correcto.
    
    Reglas:
    - No puede estar vacío
    - Debe tener al menos 3 caracteres
    - Solo puede contener letras y espacios
    - Puede tener tildes (á, é, í, ó, ú) y ñ
    
    Parámetros:
        nombre (str): El nombre a validar
        
    Retorna:
        bool: True si el nombre es válido
        
    Lanza:
        ValidacionError: Si el nombre no cumple las reglas
        
    Ejemplo:
        validar_nombre("Juan Pérez")  # Correcto
        validar_nombre("AB")  # Error: muy corto
    """
    # Verificar que el nombre no sea None o vacío
    if not nombre or not isinstance(nombre, str):
        raise ValidacionError("El nombre no puede estar vacío")
    
    # Eliminar espacios al inicio y final
    nombre_limpio = nombre.strip()
    
    # Verificar longitud mínima (3 caracteres)
    if len(nombre_limpio) < 3:
        raise ValidacionError("El nombre debe tener al menos 3 caracteres")
    
    # Patrón: solo letras (incluye tildes y ñ) y espacios
    patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
    
    # Verificar que el nombre coincida con el patrón
    if not re.match(patron, nombre_limpio):
        raise ValidacionError("El nombre solo puede contener letras y espacios")
    
    # Si pasa todas las validaciones, retornar True
    return True


def validar_email(email):
    """
    Valida que el email tenga formato correcto.
    
    Reglas:
    - No puede estar vacío
    - Debe tener formato: usuario@dominio.extension
    - Ejemplo válido: juan.perez@email.com
    
    Parámetros:
        email (str): El email a validar
        
    Retorna:
        bool: True si el email es válido
        
    Lanza:
        ValidacionError: Si el email no tiene formato válido
        
    Ejemplo:
        validar_email("juan@email.com")  # Correcto
        validar_email("juan.email.com")  # Error: falta @
    """
    # Verificar que el email no sea None o vacío
    if not email or not isinstance(email, str):
        raise ValidacionError("El email no puede estar vacío")
    
    # Eliminar espacios al inicio y final
    email_limpio = email.strip()
    
    # Patrón para email: usuario@dominio.extension
    # [a-zA-Z0-9._%+-]+ : parte antes del @
    # @ : arroba obligatoria
    # [a-zA-Z0-9.-]+ : dominio
    # \. : punto obligatorio
    # [a-zA-Z]{2,} : extensión de al menos 2 letras
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Verificar que el email coincida con el patrón
    if not re.match(patron, email_limpio):
        raise ValidacionError(f"El email '{email}' no tiene un formato válido")
    
    # Si pasa la validación, retornar True
    return True


def validar_telefono(telefono):
    """
    Valida que el teléfono tenga formato correcto.
    
    Reglas:
    - No puede estar vacío
    - Debe ser un teléfono chileno válido
    - Formatos aceptados: +56912345678, 912345678, +56 9 1234 5678
    - Debe empezar con 9 (después del código de país si lo tiene)
    - Debe tener 9 dígitos después del 9
    
    Parámetros:
        telefono (str): El teléfono a validar
        
    Retorna:
        bool: True si el teléfono es válido
        
    Lanza:
        ValidacionError: Si el teléfono no es válido
        
    Ejemplo:
        validar_telefono("+56912345678")  # Correcto
        validar_telefono("912345678")     # Correcto
        validar_telefono("812345678")     # Error: debe empezar con 9
    """
    # Verificar que el teléfono no sea None o vacío
    if not telefono or not isinstance(telefono, str):
        raise ValidacionError("El teléfono no puede estar vacío")
    
    # Eliminar espacios, guiones y paréntesis para validar solo números
    telefono_limpio = telefono.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    # Patrón para teléfono chileno:
    # (\+?56)? : código de país opcional (+56 o 56)
    # [9] : debe empezar con 9
    # [0-9]{8} : seguido de exactamente 8 dígitos más
    patron = r'^(\+?56)?[9][0-9]{8}$'
    
    # Verificar que el teléfono coincida con el patrón
    if not re.match(patron, telefono_limpio):
        raise ValidacionError(f"El teléfono '{telefono}' no tiene un formato válido. Debe ser un número chileno que empiece con 9")
    
    # Si pasa la validación, retornar True
    return True


def validar_direccion(direccion):
    """
    Valida que la dirección sea correcta.
    
    Reglas:
    - No puede estar vacía
    - Debe tener al menos 10 caracteres
    - Ejemplo: "Av. Libertador 1234, Santiago"
    
    Parámetros:
        direccion (str): La dirección a validar
        
    Retorna:
        bool: True si la dirección es válida
        
    Lanza:
        ValidacionError: Si la dirección no es válida
        
    Ejemplo:
        validar_direccion("Av. Libertador 1234, Santiago")  # Correcto
        validar_direccion("Calle")  # Error: muy corta
    """
    # Verificar que la dirección no sea None o vacía
    if not direccion or not isinstance(direccion, str):
        raise ValidacionError("La dirección no puede estar vacía")
    
    # Eliminar espacios al inicio y final
    direccion_limpia = direccion.strip()
    
    # La dirección debe tener al menos 10 caracteres
    if len(direccion_limpia) < 10:
        raise ValidacionError("La dirección debe tener al menos 10 caracteres")
    
    # Si pasa la validación, retornar True
    return True


def validar_descuento(descuento):
    """
    Valida que el descuento sea un porcentaje válido.
    
    Reglas:
    - Debe ser un número entre 0 y 100
    - Representa un porcentaje (ejemplo: 15 = 15%)
    
    Parámetros:
        descuento (float): El descuento a validar
        
    Retorna:
        bool: True si el descuento es válido
        
    Lanza:
        ValidacionError: Si el descuento no está en el rango válido
        
    Ejemplo:
        validar_descuento(15.5)  # Correcto
        validar_descuento(150)   # Error: mayor a 100
    """
    # Verificar que sea un número
    if not isinstance(descuento, (int, float)):
        raise ValidacionError("El descuento debe ser un número")
    
    # Verificar que esté en el rango 0-100
    if descuento < 0 or descuento > 100:
        raise ValidacionError(f"El descuento debe estar entre 0 y 100. Valor recibido: {descuento}")
    
    # Si pasa la validación, retornar True
    return True


def validar_puntos(puntos):
    """
    Valida que los puntos sean un número válido y positivo.
    
    Reglas:
    - Debe ser un número entero
    - Debe ser mayor o igual a 0
    
    Parámetros:
        puntos (int): Los puntos a validar
        
    Retorna:
        bool: True si los puntos son válidos
        
    Lanza:
        ValidacionError: Si los puntos no son válidos
        
    Ejemplo:
        validar_puntos(100)   # Correcto
        validar_puntos(-50)   # Error: negativo
    """
    # Verificar que sea un número entero
    if not isinstance(puntos, int):
        raise ValidacionError("Los puntos deben ser un número entero")
    
    # Verificar que sea mayor o igual a 0
    if puntos < 0:
        raise ValidacionError(f"Los puntos no pueden ser negativos. Valor recibido: {puntos}")
    
    # Si pasa la validación, retornar True
    return True


def validar_monto(monto):
    """
    Valida que el monto sea un número válido y positivo.
    
    Reglas:
    - Debe ser un número (int o float)
    - Debe ser mayor a 0
    
    Parámetros:
        monto (float): El monto a validar
        
    Retorna:
        bool: True si el monto es válido
        
    Lanza:
        ValidacionError: Si el monto no es válido
        
    Ejemplo:
        validar_monto(1000.50)  # Correcto
        validar_monto(-100)     # Error: negativo
        validar_monto(0)        # Error: debe ser mayor a 0
    """
    # Verificar que sea un número
    if not isinstance(monto, (int, float)):
        raise ValidacionError("El monto debe ser un número")
    
    # Verificar que sea mayor a 0
    if monto <= 0:
        raise ValidacionError(f"El monto debe ser mayor a 0. Valor recibido: {monto}")
    
    # Si pasa la validación, retornar True
    return True
