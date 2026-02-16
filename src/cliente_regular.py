"""
Clase ClienteRegular - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Esta clase HEREDA de Cliente y representa un cliente regular (estándar).
Ejemplo de HERENCIA: ClienteRegular es un tipo especial de Cliente.
"""

# Importamos la clase Cliente (la clase padre)
from .cliente import Cliente

# Importamos datetime para manejar fechas
from datetime import date


class ClienteRegular(Cliente):
    """
    Clase que representa un cliente regular del sistema.
    
    HEREDA de Cliente, lo que significa que:
    - Tiene todos los atributos de Cliente (nombre, email, telefono, direccion)
    - Tiene todos los métodos de Cliente (get/set, mostrar_informacion, etc.)
    - Puede agregar nuevos atributos y métodos propios
    
    Atributos adicionales:
        _fecha_registro: Fecha en que se registró el cliente
    """
    
    def __init__(self, nombre, email, telefono, direccion, fecha_registro=None):
        """
        Constructor: Inicializa un cliente regular.
        
        Usa super() para llamar al constructor de la clase padre (Cliente)
        y luego agrega los atributos propios.
        
        Parámetros:
            nombre (str): Nombre completo del cliente
            email (str): Correo electrónico del cliente
            telefono (str): Número de teléfono del cliente
            direccion (str): Dirección física del cliente
            fecha_registro (date, opcional): Fecha de registro. Si no se proporciona, usa la fecha actual
            
        Ejemplo:
            cliente = ClienteRegular("Juan Pérez", "juan@email.com", "912345678", "Calle 123")
        """
        # Llamamos al constructor de la clase padre (Cliente)
        # super() nos permite acceder a la clase padre
        super().__init__(nombre, email, telefono, direccion)
        
        # Si no se proporciona fecha de registro, usar la fecha actual
        if fecha_registro is None:
            self._fecha_registro = date.today()
        else:
            self._fecha_registro = fecha_registro
    
    # ========== MÉTODOS GETTER Y SETTER ADICIONALES ==========
    
    def get_fecha_registro(self):
        """
        Obtiene la fecha de registro del cliente.
        
        Retorna:
            date: La fecha en que se registró el cliente
            
        Ejemplo:
            fecha = cliente.get_fecha_registro()
            print(fecha)  # 2026-02-15
        """
        return self._fecha_registro
    
    def set_fecha_registro(self, fecha):
        """
        Establece la fecha de registro del cliente.
        
        Parámetros:
            fecha (date): La nueva fecha de registro
            
        Ejemplo:
            from datetime import date
            cliente.set_fecha_registro(date(2026, 1, 15))
        """
        self._fecha_registro = fecha
    
    # ========== MÉTODOS SOBRESCRITOS (POLIMORFISMO) ==========
    
    def mostrar_informacion(self):
        """
        Muestra la información del cliente regular.
        
        Este método SOBRESCRIBE el método de la clase padre.
        Ejemplo de POLIMORFISMO: mismo método, comportamiento diferente.
        
        Muestra la información base + la fecha de registro.
        """
        print("=" * 60)
        print("INFORMACIÓN DEL CLIENTE REGULAR")
        print("=" * 60)
        print(f"Nombre:          {self.get_nombre()}")
        print(f"Email:           {self.get_email()}")
        print(f"Teléfono:        {self.get_telefono()}")
        print(f"Dirección:       {self.get_direccion()}")
        print(f"Fecha Registro:  {self._fecha_registro}")
        print("=" * 60)
    
    def obtener_resumen(self):
        """
        Retorna un diccionario con todos los datos del cliente regular.
        
        Este método SOBRESCRIBE el de la clase padre para incluir
        la fecha de registro.
        
        Retorna:
            dict: Diccionario con todos los datos del cliente
            
        Ejemplo:
            resumen = cliente.obtener_resumen()
            print(resumen['fecha_registro'])
        """
        # Obtenemos el resumen base llamando al método del padre
        resumen = super().obtener_resumen()
        # Agregamos la fecha de registro
        resumen['fecha_registro'] = str(self._fecha_registro)
        resumen['tipo_cliente'] = 'Regular'
        return resumen
    
    def calcular_descuento(self, monto):
        """
        Calcula el descuento para un cliente regular.
        
        Los clientes regulares NO tienen descuento (0%).
        Este método se sobrescribirá en ClientePremium para dar descuentos.
        
        Parámetros:
            monto (float): El monto de la compra
            
        Retorna:
            float: El descuento (siempre 0 para clientes regulares)
            
        Ejemplo:
            descuento = cliente.calcular_descuento(1000)
            print(descuento)  # 0.0
        """
        # Los clientes regulares no tienen descuento
        return 0.0
    
    # ========== MÉTODOS ESPECIALES ==========
    
    def __str__(self):
        """
        Retorna una representación en texto del cliente regular.
        
        Retorna:
            str: Información del cliente en una línea
            
        Ejemplo:
            print(cliente)
            # Cliente Regular: Juan Pérez | Email: juan@email.com | Registro: 2026-02-15
        """
        return f"Cliente Regular: {self.get_nombre()} | Email: {self.get_email()} | Registro: {self._fecha_registro}"
