# Clase base Cliente - Proyecto GIC Módulo 4

from .validaciones import validar_nombre, validar_email, validar_telefono, validar_direccion
from .excepciones import ValidacionError


class Cliente:
    """Clase base que representa un cliente del sistema."""

    def __init__(self, nombre, email, telefono, direccion):
        self.set_nombre(nombre)
        self.set_email(email)
        self.set_telefono(telefono)
        self.set_direccion(direccion)

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_email(self):
        return self._email

    def get_telefono(self):
        return self._telefono

    def get_direccion(self):
        return self._direccion

    # Setters con validación
    def set_nombre(self, nombre):
        validar_nombre(nombre)
        self._nombre = nombre.strip()

    def set_email(self, email):
        validar_email(email)
        self._email = email.lower().strip()

    def set_telefono(self, telefono):
        validar_telefono(telefono)
        self._telefono = telefono.strip()

    def set_direccion(self, direccion):
        validar_direccion(direccion)
        self._direccion = direccion.strip()

    def mostrar_informacion(self):
        print("--- Información del cliente ---")
        print(f"Nombre:    {self._nombre}")
        print(f"Email:     {self._email}")
        print(f"Teléfono:  {self._telefono}")
        print(f"Dirección: {self._direccion}")

    def actualizar_email(self, nuevo_email):
        email_anterior = self._email
        self.set_email(nuevo_email)
        print(f"Email actualizado: {email_anterior} -> {self._email}")

    def actualizar_telefono(self, nuevo_telefono):
        telefono_anterior = self._telefono
        self.set_telefono(nuevo_telefono)
        print(f"Teléfono actualizado: {telefono_anterior} -> {self._telefono}")

    def actualizar_direccion(self, nueva_direccion):
        self.set_direccion(nueva_direccion)
        print("Dirección actualizada")

    def obtener_resumen(self):
        return {
            'nombre': self._nombre,
            'email': self._email,
            'telefono': self._telefono,
            'direccion': self._direccion
        }

    def __str__(self):
        return f"Cliente: {self._nombre} | {self._email} | {self._telefono}"

    def __repr__(self):
        return f"Cliente('{self._nombre}', '{self._email}')"
