"""
Clase ClienteCorporativo - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Esta clase HEREDA de Cliente y representa un cliente corporativo (empresa).
Ejemplo de HERENCIA: ClienteCorporativo es un tipo especial de Cliente.
"""

# Importamos la clase Cliente (la clase padre)
from .cliente import Cliente

# Importamos las funciones de validación necesarias
from .validaciones import validar_monto

# Importamos las excepciones
from .excepciones import ValidacionError


class ClienteCorporativo(Cliente):
    """
    Clase que representa un cliente corporativo (empresa) del sistema.
    
    HEREDA de Cliente, por lo tanto:
    - Tiene todos los atributos y métodos de Cliente
    - Agrega atributos de empresa: nombre empresa, RUT, contacto, límite crédito
    - Métodos específicos para gestionar crédito corporativo
    
    Atributos adicionales:
        _nombre_empresa: Nombre de la empresa
        _rut_empresa: RUT de la empresa
        _contacto_principal: Nombre de la persona de contacto
        _limite_credito: Límite de crédito disponible
        _credito_utilizado: Crédito ya utilizado
    """
    
    def __init__(self, nombre, email, telefono, direccion, nombre_empresa, 
                 rut_empresa, contacto_principal, limite_credito=100000.0):
        """
        Constructor: Inicializa un cliente corporativo.
        
        Parámetros:
            nombre (str): Nombre del cliente (puede ser el mismo que contacto_principal)
            email (str): Correo electrónico del cliente
            telefono (str): Número de teléfono del cliente
            direccion (str): Dirección de la empresa
            nombre_empresa (str): Nombre de la empresa
            rut_empresa (str): RUT de la empresa
            contacto_principal (str): Nombre de la persona de contacto
            limite_credito (float): Límite de crédito (default: 100,000)
            
        Ejemplo:
            cliente = ClienteCorporativo(
                "Pedro Sánchez", "pedro@empresa.com", "912345678",
                "Av. Empresarial 789", "Tech Solutions SpA",
                "76.123.456-7", "Pedro Sánchez", 500000.0
            )
        """
        # Llamamos al constructor del padre (Cliente) usando super()
        super().__init__(nombre, email, telefono, direccion)
        
        # Inicializamos los atributos específicos de ClienteCorporativo
        self._nombre_empresa = nombre_empresa
        self._rut_empresa = rut_empresa
        self._contacto_principal = contacto_principal
        # Validamos y guardamos el límite de crédito
        self.set_limite_credito(limite_credito)
        # El crédito utilizado empieza en 0
        self._credito_utilizado = 0.0
    
    # ========== MÉTODOS GETTER ==========
    
    def get_nombre_empresa(self):
        """
        Obtiene el nombre de la empresa.
        
        Retorna:
            str: El nombre de la empresa
            
        Ejemplo:
            nombre = cliente.get_nombre_empresa()
            print(nombre)  # "Tech Solutions SpA"
        """
        return self._nombre_empresa
    
    def get_rut_empresa(self):
        """
        Obtiene el RUT de la empresa.
        
        Retorna:
            str: El RUT de la empresa
            
        Ejemplo:
            rut = cliente.get_rut_empresa()
            print(rut)  # "76.123.456-7"
        """
        return self._rut_empresa
    
    def get_contacto_principal(self):
        """
        Obtiene el nombre del contacto principal.
        
        Retorna:
            str: El nombre del contacto
            
        Ejemplo:
            contacto = cliente.get_contacto_principal()
            print(contacto)  # "Pedro Sánchez"
        """
        return self._contacto_principal
    
    def get_limite_credito(self):
        """
        Obtiene el límite de crédito de la empresa.
        
        Retorna:
            float: El límite de crédito
            
        Ejemplo:
            limite = cliente.get_limite_credito()
            print(limite)  # 500000.0
        """
        return self._limite_credito
    
    def get_credito_utilizado(self):
        """
        Obtiene el crédito ya utilizado por la empresa.
        
        Retorna:
            float: El crédito utilizado
            
        Ejemplo:
            utilizado = cliente.get_credito_utilizado()
            print(utilizado)  # 150000.0
        """
        return self._credito_utilizado
    
    def get_credito_disponible(self):
        """
        Calcula el crédito disponible (límite - utilizado).
        
        Retorna:
            float: El crédito disponible
            
        Ejemplo:
            disponible = cliente.get_credito_disponible()
            print(disponible)  # 350000.0 (si límite=500000 y utilizado=150000)
        """
        return self._limite_credito - self._credito_utilizado
    
    # ========== MÉTODOS SETTER ==========
    
    def set_nombre_empresa(self, nombre):
        """
        Establece el nombre de la empresa.
        
        Parámetros:
            nombre (str): Nuevo nombre de la empresa
            
        Ejemplo:
            cliente.set_nombre_empresa("Tech Solutions Chile SpA")
        """
        if not nombre or len(nombre.strip()) < 3:
            raise ValidacionError("El nombre de la empresa debe tener al menos 3 caracteres")
        self._nombre_empresa = nombre.strip()
    
    def set_rut_empresa(self, rut):
        """
        Establece el RUT de la empresa.
        
        Parámetros:
            rut (str): Nuevo RUT de la empresa
            
        Ejemplo:
            cliente.set_rut_empresa("76.123.456-7")
        """
        if not rut or len(rut.strip()) < 5:
            raise ValidacionError("El RUT de la empresa no es válido")
        self._rut_empresa = rut.strip()
    
    def set_contacto_principal(self, contacto):
        """
        Establece el contacto principal.
        
        Parámetros:
            contacto (str): Nuevo nombre del contacto
            
        Ejemplo:
            cliente.set_contacto_principal("María González")
        """
        if not contacto or len(contacto.strip()) < 3:
            raise ValidacionError("El contacto principal debe tener al menos 3 caracteres")
        self._contacto_principal = contacto.strip()
    
    def set_limite_credito(self, limite):
        """
        Establece el límite de crédito.
        
        Parámetros:
            limite (float): Nuevo límite de crédito
            
        Lanza:
            ValidacionError: Si el límite no es válido
            
        Ejemplo:
            cliente.set_limite_credito(750000.0)
        """
        # Validamos que el límite sea un monto válido
        validar_monto(limite)
        self._limite_credito = limite
    
    # ========== MÉTODOS ESPECÍFICOS DE CLIENTE CORPORATIVO ==========
    
    def verificar_credito_disponible(self, monto):
        """
        Verifica si hay crédito disponible para un monto dado.
        
        Parámetros:
            monto (float): Monto a verificar
            
        Retorna:
            bool: True si hay crédito disponible, False si no
            
        Ejemplo:
            if cliente.verificar_credito_disponible(50000):
                print("Hay crédito disponible")
            else:
                print("No hay suficiente crédito")
        """
        # Validamos que el monto sea válido
        validar_monto(monto)
        
        # Calculamos el crédito disponible
        disponible = self.get_credito_disponible()
        
        # Verificamos si hay suficiente crédito
        if monto <= disponible:
            print(f"✓ Crédito disponible: ${disponible:,.2f}")
            return True
        else:
            print(f"✗ Crédito insuficiente. Disponible: ${disponible:,.2f}, Requerido: ${monto:,.2f}")
            return False
    
    def utilizar_credito(self, monto):
        """
        Utiliza una cantidad del crédito disponible.
        
        Parámetros:
            monto (float): Monto a utilizar
            
        Retorna:
            bool: True si se pudo utilizar, False si no hay suficiente crédito
            
        Ejemplo:
            if cliente.utilizar_credito(50000):
                print("Crédito utilizado exitosamente")
        """
        # Verificamos si hay crédito disponible
        if self.verificar_credito_disponible(monto):
            # Si hay suficiente, lo utilizamos
            self._credito_utilizado += monto
            print(f"Crédito utilizado: ${monto:,.2f}")
            print(f"Crédito restante: ${self.get_credito_disponible():,.2f}")
            return True
        else:
            return False
    
    def pagar_credito(self, monto):
        """
        Paga (reduce) el crédito utilizado.
        
        Parámetros:
            monto (float): Monto a pagar
            
        Ejemplo:
            cliente.pagar_credito(25000)
        """
        # Validamos el monto
        validar_monto(monto)
        
        # No podemos pagar más de lo que debemos
        if monto > self._credito_utilizado:
            print(f"Advertencia: El monto a pagar (${monto:,.2f}) es mayor que la deuda (${self._credito_utilizado:,.2f})")
            print(f"Se pagará solo ${self._credito_utilizado:,.2f}")
            monto = self._credito_utilizado
        
        # Restamos el pago del crédito utilizado
        self._credito_utilizado -= monto
        print(f"Pago registrado: ${monto:,.2f}")
        print(f"Deuda restante: ${self._credito_utilizado:,.2f}")
        print(f"Crédito disponible: ${self.get_credito_disponible():,.2f}")
    
    def actualizar_limite_credito(self, nuevo_limite):
        """
        Actualiza el límite de crédito de la empresa.
        
        Parámetros:
            nuevo_limite (float): Nuevo límite de crédito
            
        Lanza:
            ValidacionError: Si el nuevo límite no es válido
            
        Ejemplo:
            cliente.actualizar_limite_credito(1000000.0)
        """
        limite_anterior = self._limite_credito
        self.set_limite_credito(nuevo_limite)
        print(f"Límite de crédito actualizado: ${limite_anterior:,.2f} → ${nuevo_limite:,.2f}")
    
    # ========== MÉTODOS SOBRESCRITOS (POLIMORFISMO) ==========
    
    def calcular_descuento(self, monto):
        """
        Calcula el descuento para un cliente corporativo.
        
        Los clientes corporativos tienen un descuento fijo del 15%.
        
        Parámetros:
            monto (float): El monto de la compra
            
        Retorna:
            float: El monto del descuento
            
        Ejemplo:
            descuento = cliente.calcular_descuento(1000)
            print(descuento)  # 150.0
        """
        # Descuento fijo del 15% para clientes corporativos
        descuento_corporativo = 15.0
        descuento_calculado = monto * (descuento_corporativo / 100)
        return descuento_calculado
    
    def mostrar_informacion(self):
        """
        Muestra la información del cliente corporativo.
        
        POLIMORFISMO: Este método sobrescribe el de la clase padre.
        Muestra información específica de clientes corporativos.
        """
        print("=" * 60)
        print("INFORMACIÓN DEL CLIENTE CORPORATIVO")
        print("=" * 60)
        print(f"Empresa:           {self._nombre_empresa}")
        print(f"RUT:               {self._rut_empresa}")
        print(f"Contacto:          {self._contacto_principal}")
        print(f"Email:             {self.get_email()}")
        print(f"Teléfono:          {self.get_telefono()}")
        print(f"Dirección:         {self.get_direccion()}")
        print("-" * 60)
        print(f"Límite Crédito:    ${self._limite_credito:,.2f}")
        print(f"Crédito Utilizado: ${self._credito_utilizado:,.2f}")
        print(f"Crédito Disponible: ${self.get_credito_disponible():,.2f}")
        print("=" * 60)
    
    def obtener_resumen(self):
        """
        Retorna un diccionario con todos los datos del cliente corporativo.
        
        POLIMORFISMO: Sobrescribe el método del padre.
        
        Retorna:
            dict: Diccionario con todos los datos
        """
        # Obtenemos el resumen base del padre
        resumen = super().obtener_resumen()
        # Agregamos la información específica de cliente corporativo
        resumen['tipo_cliente'] = 'Corporativo'
        resumen['nombre_empresa'] = self._nombre_empresa
        resumen['rut_empresa'] = self._rut_empresa
        resumen['contacto_principal'] = self._contacto_principal
        resumen['limite_credito'] = self._limite_credito
        resumen['credito_utilizado'] = self._credito_utilizado
        resumen['credito_disponible'] = self.get_credito_disponible()
        return resumen
    
    # ========== MÉTODOS ESPECIALES ==========
    
    def __str__(self):
        """
        Retorna una representación en texto del cliente corporativo.
        
        Retorna:
            str: Información del cliente en una línea
        """
        return (f"Cliente Corporativo: {self._nombre_empresa} | "
                f"RUT: {self._rut_empresa} | Contacto: {self._contacto_principal} | "
                f"Crédito Disponible: ${self.get_credito_disponible():,.2f}")
