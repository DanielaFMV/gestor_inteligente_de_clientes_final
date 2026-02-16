# ClienteCorporativo hereda de Cliente

from .cliente import Cliente
from .validaciones import validar_monto
from .excepciones import ValidacionError


class ClienteCorporativo(Cliente):
    """Subclase de Cliente para empresas con crédito corporativo y descuento fijo."""

    def __init__(self, nombre, email, telefono, direccion,
                 nombre_empresa, rut_empresa, contacto_principal, limite_credito=100000.0):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, email, telefono, direccion)

        self._nombre_empresa = nombre_empresa
        self._rut_empresa = rut_empresa
        self._contacto_principal = contacto_principal
        self.set_limite_credito(limite_credito)
        self._credito_utilizado = 0.0

    def get_nombre_empresa(self):
        return self._nombre_empresa

    def get_rut_empresa(self):
        return self._rut_empresa

    def get_contacto_principal(self):
        return self._contacto_principal

    def get_limite_credito(self):
        return self._limite_credito

    def get_credito_utilizado(self):
        return self._credito_utilizado

    def get_credito_disponible(self):
        return self._limite_credito - self._credito_utilizado

    def verificar_credito_disponible(self, monto):
        """Verifica si hay suficiente crédito disponible para el monto solicitado."""
        validar_monto(monto)
        return self.get_credito_disponible() >= monto

    def set_limite_credito(self, limite):
        validar_monto(limite)
        self._limite_credito = limite

    def utilizar_credito(self, monto):
        validar_monto(monto)
        disponible = self.get_credito_disponible()
        if monto <= disponible:
            self._credito_utilizado += monto
            print(f"Crédito utilizado: ${monto}. Disponible: ${self.get_credito_disponible()}")
            return True
        else:
            print(f"Sin crédito suficiente. Disponible: ${disponible}, Solicitado: ${monto}")
            return False

    def pagar_credito(self, monto):
        validar_monto(monto)
        if monto > self._credito_utilizado:
            monto = self._credito_utilizado
        self._credito_utilizado -= monto
        print(f"Pago registrado: ${monto}. Deuda restante: ${self._credito_utilizado}")

    # Método polimórfico: descuento fijo del 15% para empresas
    def calcular_descuento(self, monto):
        return monto * 0.15

    def mostrar_informacion(self):
        print("--- Cliente Corporativo ---")
        print(f"Empresa:            {self._nombre_empresa}")
        print(f"RUT:                {self._rut_empresa}")
        print(f"Contacto:           {self._contacto_principal}")
        print(f"Email:              {self.get_email()}")
        print(f"Teléfono:           {self.get_telefono()}")
        print(f"Dirección:          {self.get_direccion()}")
        print(f"Límite crédito:     ${self._limite_credito}")
        print(f"Crédito utilizado:  ${self._credito_utilizado}")
        print(f"Crédito disponible: ${self.get_credito_disponible()}")

    def obtener_resumen(self):
        resumen = super().obtener_resumen()
        resumen['tipo_cliente'] = 'Corporativo'
        resumen['nombre_empresa'] = self._nombre_empresa
        resumen['rut_empresa'] = self._rut_empresa
        resumen['contacto_principal'] = self._contacto_principal
        resumen['limite_credito'] = self._limite_credito
        resumen['credito_utilizado'] = self._credito_utilizado
        return resumen

    def __str__(self):
        return (f"Cliente Corporativo: {self._nombre_empresa} | "
                f"{self.get_email()} | Crédito disponible: ${self.get_credito_disponible()}")

