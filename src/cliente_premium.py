"""
Clase ClientePremium - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Esta clase HEREDA de Cliente y representa un cliente premium (con beneficios).
Ejemplo de HERENCIA y POLIMORFISMO: tiene descuentos y puntos.
"""

# Importamos la clase Cliente (la clase padre)
from .cliente import Cliente

# Importamos las funciones de validación necesarias
from .validaciones import validar_descuento, validar_puntos

# Importamos las excepciones
from .excepciones import ValidacionError


class ClientePremium(Cliente):
    """
    Clase que representa un cliente premium del sistema.
    
    HEREDA de Cliente, por lo tanto:
    - Tiene todos los atributos y métodos de Cliente
    - Agrega atributos especiales: nivel de membresía, descuento, puntos
    - Sobrescribe algunos métodos para comportamiento específico (POLIMORFISMO)
    
    Atributos adicionales:
        _nivel_membresia: Nivel del cliente (Bronce, Plata, Oro)
        _descuento: Porcentaje de descuento (0-100)
        _puntos_acumulados: Puntos acumulados por compras
    """
    
    def __init__(self, nombre, email, telefono, direccion, nivel_membresia="Bronce", descuento=10.0):
        """
        Constructor: Inicializa un cliente premium.
        
        Parámetros:
            nombre (str): Nombre completo del cliente
            email (str): Correo electrónico del cliente
            telefono (str): Número de teléfono del cliente
            direccion (str): Dirección física del cliente
            nivel_membresia (str): Nivel de membresía (Bronce, Plata, Oro)
            descuento (float): Porcentaje de descuento (0-100)
            
        Ejemplo:
            cliente = ClientePremium("María López", "maria@email.com", "987654321", 
                                     "Av. Principal 456", "Oro", 20.0)
        """
        # Llamamos al constructor del padre (Cliente) usando super()
        super().__init__(nombre, email, telefono, direccion)
        
        # Inicializamos los atributos específicos de ClientePremium
        self._nivel_membresia = nivel_membresia
        # Validamos y guardamos el descuento
        self.set_descuento(descuento)
        # Los puntos empiezan en 0
        self._puntos_acumulados = 0
    
    # ========== MÉTODOS GETTER ==========
    
    def get_nivel_membresia(self):
        """
        Obtiene el nivel de membresía del cliente.
        
        Retorna:
            str: El nivel (Bronce, Plata, Oro)
            
        Ejemplo:
            nivel = cliente.get_nivel_membresia()
            print(nivel)  # "Oro"
        """
        return self._nivel_membresia
    
    def get_descuento(self):
        """
        Obtiene el porcentaje de descuento del cliente.
        
        Retorna:
            float: El descuento (0-100)
            
        Ejemplo:
            descuento = cliente.get_descuento()
            print(descuento)  # 20.0
        """
        return self._descuento
    
    def get_puntos_acumulados(self):
        """
        Obtiene los puntos acumulados del cliente.
        
        Retorna:
            int: Los puntos acumulados
            
        Ejemplo:
            puntos = cliente.get_puntos_acumulados()
            print(puntos)  # 1500
        """
        return self._puntos_acumulados
    
    # ========== MÉTODOS SETTER ==========
    
    def set_nivel_membresia(self, nivel):
        """
        Establece el nivel de membresía del cliente.
        
        Parámetros:
            nivel (str): Nuevo nivel (Bronce, Plata, Oro)
            
        Ejemplo:
            cliente.set_nivel_membresia("Plata")
        """
        # Validamos que el nivel sea uno de los permitidos
        niveles_validos = ["Bronce", "Plata", "Oro"]
        if nivel not in niveles_validos:
            raise ValidacionError(f"El nivel debe ser uno de: {niveles_validos}")
        self._nivel_membresia = nivel
    
    def set_descuento(self, descuento):
        """
        Establece el descuento del cliente.
        
        Parámetros:
            descuento (float): Nuevo descuento (0-100)
            
        Lanza:
            ValidacionError: Si el descuento no está entre 0 y 100
            
        Ejemplo:
            cliente.set_descuento(15.5)
        """
        # Validamos que el descuento esté en el rango correcto
        validar_descuento(descuento)
        self._descuento = descuento
    
    def set_puntos_acumulados(self, puntos):
        """
        Establece los puntos acumulados del cliente.
        
        Parámetros:
            puntos (int): Nuevos puntos acumulados
            
        Lanza:
            ValidacionError: Si los puntos son negativos
            
        Ejemplo:
            cliente.set_puntos_acumulados(2000)
        """
        # Validamos que los puntos sean válidos
        validar_puntos(puntos)
        self._puntos_acumulados = puntos
    
    # ========== MÉTODOS ESPECÍFICOS DE CLIENTE PREMIUM ==========
    
    def agregar_puntos(self, puntos):
        """
        Agrega puntos a los puntos acumulados del cliente.
        
        Parámetros:
            puntos (int): Cantidad de puntos a agregar
            
        Lanza:
            ValidacionError: Si los puntos son negativos
            
        Ejemplo:
            cliente.agregar_puntos(100)
            print(f"Puntos agregados. Total: {cliente.get_puntos_acumulados()}")
        """
        # Validamos que los puntos sean válidos
        validar_puntos(puntos)
        # Agregamos los puntos
        self._puntos_acumulados += puntos
        print(f"Se agregaron {puntos} puntos. Total actual: {self._puntos_acumulados}")
    
    def canjear_puntos(self, puntos):
        """
        Canjea (resta) puntos de los puntos acumulados.
        
        Parámetros:
            puntos (int): Cantidad de puntos a canjear
            
        Retorna:
            bool: True si se pudieron canjear, False si no hay suficientes puntos
            
        Ejemplo:
            if cliente.canjear_puntos(500):
                print("Puntos canjeados exitosamente")
            else:
                print("No tiene suficientes puntos")
        """
        # Validamos que los puntos sean válidos
        validar_puntos(puntos)
        
        # Verificamos si el cliente tiene suficientes puntos
        if self._puntos_acumulados >= puntos:
            # Si tiene suficientes, los restamos
            self._puntos_acumulados -= puntos
            print(f"Se canjearon {puntos} puntos. Puntos restantes: {self._puntos_acumulados}")
            return True
        else:
            # Si no tiene suficientes, mostramos mensaje y retornamos False
            print(f"No se pueden canjear {puntos} puntos. Solo tiene {self._puntos_acumulados} puntos")
            return False
    
    # ========== MÉTODOS SOBRESCRITOS (POLIMORFISMO) ==========
    
    def calcular_descuento(self, monto):
        """
        Calcula el descuento para un cliente premium.
        
        POLIMORFISMO: Este método sobrescribe el de ClienteRegular.
        Los clientes premium SÍ tienen descuento.
        
        Parámetros:
            monto (float): El monto de la compra
            
        Retorna:
            float: El monto del descuento
            
        Ejemplo:
            # Cliente con 20% de descuento
            descuento = cliente.calcular_descuento(1000)
            print(descuento)  # 200.0
        """
        # Calculamos el descuento: monto * (descuento / 100)
        descuento_calculado = monto * (self._descuento / 100)
        return descuento_calculado
    
    def mostrar_informacion(self):
        """
        Muestra la información del cliente premium.
        
        POLIMORFISMO: Este método sobrescribe el de la clase padre.
        Muestra información adicional específica de clientes premium.
        """
        print("=" * 60)
        print("INFORMACIÓN DEL CLIENTE PREMIUM")
        print("=" * 60)
        print(f"Nombre:          {self.get_nombre()}")
        print(f"Email:           {self.get_email()}")
        print(f"Teléfono:        {self.get_telefono()}")
        print(f"Dirección:       {self.get_direccion()}")
        print(f"Nivel:           {self._nivel_membresia}")
        print(f"Descuento:       {self._descuento}%")
        print(f"Puntos:          {self._puntos_acumulados}")
        print("=" * 60)
    
    def obtener_resumen(self):
        """
        Retorna un diccionario con todos los datos del cliente premium.
        
        POLIMORFISMO: Sobrescribe el método del padre para incluir
        información específica de clientes premium.
        
        Retorna:
            dict: Diccionario con todos los datos
        """
        # Obtenemos el resumen base del padre
        resumen = super().obtener_resumen()
        # Agregamos la información específica de cliente premium
        resumen['tipo_cliente'] = 'Premium'
        resumen['nivel_membresia'] = self._nivel_membresia
        resumen['descuento'] = self._descuento
        resumen['puntos_acumulados'] = self._puntos_acumulados
        return resumen
    
    # ========== MÉTODOS ESPECIALES ==========
    
    def __str__(self):
        """
        Retorna una representación en texto del cliente premium.
        
        Retorna:
            str: Información del cliente en una línea
        """
        return (f"Cliente Premium [{self._nivel_membresia}]: {self.get_nombre()} | "
                f"Email: {self.get_email()} | Descuento: {self._descuento}% | "
                f"Puntos: {self._puntos_acumulados}")
