# ClientePremium hereda de Cliente

from .cliente import Cliente
from .validaciones import validar_descuento, validar_puntos
from .excepciones import ValidacionError


class ClientePremium(Cliente):
    """Subclase de Cliente con sistema de puntos y descuentos por membresía."""

    def __init__(self, nombre, email, telefono, direccion, nivel_membresia="Bronce", descuento=10.0):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, email, telefono, direccion)

        self.set_nivel_membresia(nivel_membresia)
        self.set_descuento(descuento)
        self._puntos_acumulados = 0

    def get_nivel_membresia(self):
        return self._nivel_membresia

    def get_descuento(self):
        return self._descuento

    def get_puntos_acumulados(self):
        return self._puntos_acumulados

    def set_nivel_membresia(self, nivel):
        niveles_validos = ["Bronce", "Plata", "Oro"]
        if nivel not in niveles_validos:
            raise ValidacionError(f"El nivel debe ser uno de: {niveles_validos}")
        self._nivel_membresia = nivel

    def set_descuento(self, descuento):
        validar_descuento(descuento)
        self._descuento = descuento

    def agregar_puntos(self, puntos):
        validar_puntos(puntos)
        self._puntos_acumulados += puntos
        print(f"Puntos agregados: {puntos}. Total: {self._puntos_acumulados}")

    def canjear_puntos(self, puntos):
        validar_puntos(puntos)
        if self._puntos_acumulados >= puntos:
            self._puntos_acumulados -= puntos
            print(f"Puntos canjeados: {puntos}. Quedan: {self._puntos_acumulados}")
            return True
        else:
            print(f"No tiene suficientes puntos. Tiene {self._puntos_acumulados}")
            return False

    # Método polimórfico: sobrescribe calcular_descuento de la clase padre
    def calcular_descuento(self, monto):
        return monto * (self._descuento / 100)

    def mostrar_informacion(self):
        print("--- Cliente Premium ---")
        print(f"Nombre:    {self.get_nombre()}")
        print(f"Email:     {self.get_email()}")
        print(f"Teléfono:  {self.get_telefono()}")
        print(f"Dirección: {self.get_direccion()}")
        print(f"Nivel:     {self._nivel_membresia}")
        print(f"Descuento: {self._descuento}%")
        print(f"Puntos:    {self._puntos_acumulados}")

    def obtener_resumen(self):
        resumen = super().obtener_resumen()
        resumen['tipo_cliente'] = 'Premium'
        resumen['nivel_membresia'] = self._nivel_membresia
        resumen['descuento'] = self._descuento
        resumen['puntos_acumulados'] = self._puntos_acumulados
        return resumen

    def __str__(self):
        return (f"Cliente Premium [{self._nivel_membresia}]: {self.get_nombre()} | "
                f"Descuento: {self._descuento}% | Puntos: {self._puntos_acumulados}")
