# Funciones de validación - Proyecto GIC

import re
from .excepciones import ValidacionError


def validar_nombre(nombre):
    if not nombre or not isinstance(nombre, str):
        raise ValidacionError("El nombre no puede estar vacío")

    nombre_limpio = nombre.strip()

    if len(nombre_limpio) < 3:
        raise ValidacionError("El nombre debe tener al menos 3 caracteres")

    # Solo letras, espacios, tildes y ñ
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre_limpio):
        raise ValidacionError("El nombre solo puede contener letras y espacios")

    return True


def validar_email(email):
    if not email or not isinstance(email, str):
        raise ValidacionError("El email no puede estar vacío")

    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(patron, email.strip()):
        raise ValidacionError(f"El email '{email}' no tiene formato válido")

    return True


def validar_telefono(telefono):
    if not telefono or not isinstance(telefono, str):
        raise ValidacionError("El teléfono no puede estar vacío")

    # Eliminar espacios y guiones para validar solo los dígitos
    telefono_limpio = telefono.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    # Teléfono chileno: puede tener +56 y debe empezar con 9
    patron = r'^(\+?56)?[9][0-9]{8}$'

    if not re.match(patron, telefono_limpio):
        raise ValidacionError(f"Teléfono inválido '{telefono}'. Debe ser número chileno que empiece con 9")

    return True


def validar_direccion(direccion):
    if not direccion or not isinstance(direccion, str):
        raise ValidacionError("La dirección no puede estar vacía")

    if len(direccion.strip()) < 10:
        raise ValidacionError("La dirección debe tener al menos 10 caracteres")

    return True


def validar_descuento(descuento):
    if not isinstance(descuento, (int, float)):
        raise ValidacionError("El descuento debe ser un número")

    if descuento < 0 or descuento > 100:
        raise ValidacionError("El descuento debe estar entre 0 y 100")

    return True


def validar_puntos(puntos):
    if not isinstance(puntos, int):
        raise ValidacionError("Los puntos deben ser un número entero")

    if puntos < 0:
        raise ValidacionError("Los puntos no pueden ser negativos")

    return True


def validar_monto(monto):
    if not isinstance(monto, (int, float)):
        raise ValidacionError("El monto debe ser un número")

    if monto <= 0:
        raise ValidacionError("El monto debe ser mayor a 0")

    return True
