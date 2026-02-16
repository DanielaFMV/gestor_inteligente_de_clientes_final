# ClienteRegular hereda de Cliente

from .cliente import Cliente
from datetime import date


class ClienteRegular(Cliente):
    """Subclase de Cliente para clientes regulares, sin beneficios especiales."""

    def __init__(self, nombre, email, telefono, direccion, fecha_registro=None):
        # Llamamos al constructor de la clase padre con super()
        super().__init__(nombre, email, telefono, direccion)

        if fecha_registro is None:
            self._fecha_registro = date.today()
        else:
            self._fecha_registro = fecha_registro

    def get_fecha_registro(self):
        return self._fecha_registro

    def calcular_descuento(self, monto):
        # Los clientes regulares no tienen descuento
        return 0.0

    def mostrar_informacion(self):
        print("--- Cliente Regular ---")
        print(f"Nombre:         {self.get_nombre()}")
        print(f"Email:          {self.get_email()}")
        print(f"Teléfono:       {self.get_telefono()}")
        print(f"Dirección:      {self.get_direccion()}")
        print(f"Fecha registro: {self._fecha_registro}")

    def obtener_resumen(self):
        resumen = super().obtener_resumen()
        resumen['tipo_cliente'] = 'Regular'
        resumen['fecha_registro'] = str(self._fecha_registro)
        return resumen

    def __str__(self):
        return f"Cliente Regular: {self.get_nombre()} | {self.get_email()} | Registro: {self._fecha_registro}"
