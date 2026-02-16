"""
Clase Cliente Base - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Esta es la clase BASE de la cual heredarán otros tipos de clientes.
Código SIMPLE sin decoradores @property, con getters y setters como métodos normales.
TODO comentado línea por línea para principiantes.
"""

# Importamos las funciones de validación
from .validaciones import (
    validar_nombre,
    validar_email,
    validar_telefono,
    validar_direccion
)

# Importamos las excepciones personalizadas
from .excepciones import ValidacionError


class Cliente:
    """
    Clase que representa un cliente básico del sistema.
    
    Esta clase almacena la información de un cliente y proporciona
    métodos para acceder y modificar sus datos de forma segura.
    
    Atributos:
        _nombre: Nombre completo del cliente (privado)
        _email: Correo electrónico del cliente (privado)
        _telefono: Número de teléfono del cliente (privado)
        _direccion: Dirección física del cliente (privado)
    
    Nota: Los atributos empiezan con _ para indicar que son "privados"
    (no se debe acceder directamente desde fuera de la clase)
    """
    
    def __init__(self, nombre, email, telefono, direccion):
        """
        Constructor: Inicializa un nuevo cliente con sus datos.
        
        Este método se ejecuta automáticamente cuando creamos un cliente:
        cliente1 = Cliente("Juan", "juan@email.com", "912345678", "Calle 123")
        
        Parámetros:
            nombre (str): Nombre completo del cliente
            email (str): Correo electrónico del cliente
            telefono (str): Número de teléfono del cliente
            direccion (str): Dirección física del cliente
            
        Lanza:
            ValidacionError: Si algún dato no pasa las validaciones
        """
        # Llamamos a los métodos setter para asignar los valores
        # Esto asegura que se validen los datos al crear el objeto
        self.set_nombre(nombre)
        self.set_email(email)
        self.set_telefono(telefono)
        self.set_direccion(direccion)
    
    # ========== MÉTODOS GETTER (para obtener valores) ==========
    
    def get_nombre(self):
        """
        Obtiene el nombre del cliente.
        
        Retorna:
            str: El nombre del cliente
            
        Ejemplo:
            nombre = cliente.get_nombre()
            print(nombre)  # "Juan Pérez"
        """
        return self._nombre
    
    def get_email(self):
        """
        Obtiene el email del cliente.
        
        Retorna:
            str: El email del cliente
            
        Ejemplo:
            email = cliente.get_email()
            print(email)  # "juan@email.com"
        """
        return self._email
    
    def get_telefono(self):
        """
        Obtiene el teléfono del cliente.
        
        Retorna:
            str: El teléfono del cliente
            
        Ejemplo:
            telefono = cliente.get_telefono()
            print(telefono)  # "+56912345678"
        """
        return self._telefono
    
    def get_direccion(self):
        """
        Obtiene la dirección del cliente.
        
        Retorna:
            str: La dirección del cliente
            
        Ejemplo:
            direccion = cliente.get_direccion()
            print(direccion)  # "Av. Libertador 1234"
        """
        return self._direccion
    
    # ========== MÉTODOS SETTER (para modificar valores) ==========
    
    def set_nombre(self, nombre):
        """
        Establece el nombre del cliente con validación.
        
        Valida que el nombre sea correcto antes de guardarlo.
        
        Parámetros:
            nombre (str): El nuevo nombre del cliente
            
        Lanza:
            ValidacionError: Si el nombre no es válido
            
        Ejemplo:
            cliente.set_nombre("María González")
        """
        # Primero validamos el nombre
        validar_nombre(nombre)
        # Si la validación pasa, guardamos el nombre (limpio, sin espacios extra)
        self._nombre = nombre.strip()
    
    def set_email(self, email):
        """
        Establece el email del cliente con validación.
        
        Valida que el email tenga formato correcto antes de guardarlo.
        
        Parámetros:
            email (str): El nuevo email del cliente
            
        Lanza:
            ValidacionError: Si el email no es válido
            
        Ejemplo:
            cliente.set_email("maria@email.com")
        """
        # Primero validamos el email
        validar_email(email)
        # Si la validación pasa, guardamos el email en minúsculas
        self._email = email.lower().strip()
    
    def set_telefono(self, telefono):
        """
        Establece el teléfono del cliente con validación.
        
        Valida que el teléfono sea correcto antes de guardarlo.
        
        Parámetros:
            telefono (str): El nuevo teléfono del cliente
            
        Lanza:
            ValidacionError: Si el teléfono no es válido
            
        Ejemplo:
            cliente.set_telefono("+56987654321")
        """
        # Primero validamos el teléfono
        validar_telefono(telefono)
        # Si la validación pasa, guardamos el teléfono
        self._telefono = telefono.strip()
    
    def set_direccion(self, direccion):
        """
        Establece la dirección del cliente con validación.
        
        Valida que la dirección sea correcta antes de guardarla.
        
        Parámetros:
            direccion (str): La nueva dirección del cliente
            
        Lanza:
            ValidacionError: Si la dirección no es válida
            
        Ejemplo:
            cliente.set_direccion("Av. Providencia 890, Santiago")
        """
        # Primero validamos la dirección
        validar_direccion(direccion)
        # Si la validación pasa, guardamos la dirección
        self._direccion = direccion.strip()
    
    # ========== MÉTODOS PÚBLICOS (operaciones del cliente) ==========
    
    def mostrar_informacion(self):
        """
        Muestra toda la información del cliente en pantalla.
        
        Este método imprime los datos del cliente de forma organizada.
        
        Ejemplo:
            cliente.mostrar_informacion()
            # Imprime:
            # ==================================================
            # INFORMACIÓN DEL CLIENTE
            # ==================================================
            # Nombre:    Juan Pérez
            # Email:     juan@email.com
            # ...
        """
        print("=" * 60)
        print("INFORMACIÓN DEL CLIENTE")
        print("=" * 60)
        print(f"Nombre:    {self._nombre}")
        print(f"Email:     {self._email}")
        print(f"Teléfono:  {self._telefono}")
        print(f"Dirección: {self._direccion}")
        print("=" * 60)
    
    def actualizar_email(self, nuevo_email):
        """
        Actualiza el email del cliente y muestra un mensaje de confirmación.
        
        Parámetros:
            nuevo_email (str): El nuevo email
            
        Lanza:
            ValidacionError: Si el email no es válido
            
        Ejemplo:
            cliente.actualizar_email("juan.nuevo@email.com")
            # Imprime: "Email actualizado: juan@email.com → juan.nuevo@email.com"
        """
        # Guardamos el email anterior para mostrar el mensaje
        email_anterior = self._email
        # Actualizamos el email (esto ya valida automáticamente)
        self.set_email(nuevo_email)
        # Mostramos mensaje de confirmación
        print(f"Email actualizado: {email_anterior} → {self._email}")
    
    def actualizar_telefono(self, nuevo_telefono):
        """
        Actualiza el teléfono del cliente y muestra un mensaje de confirmación.
        
        Parámetros:
            nuevo_telefono (str): El nuevo teléfono
            
        Lanza:
            ValidacionError: Si el teléfono no es válido
            
        Ejemplo:
            cliente.actualizar_telefono("+56987654321")
            # Imprime: "Teléfono actualizado: +56912345678 → +56987654321"
        """
        # Guardamos el teléfono anterior para mostrar el mensaje
        telefono_anterior = self._telefono
        # Actualizamos el teléfono (esto ya valida automáticamente)
        self.set_telefono(nuevo_telefono)
        # Mostramos mensaje de confirmación
        print(f"Teléfono actualizado: {telefono_anterior} → {self._telefono}")
    
    def actualizar_direccion(self, nueva_direccion):
        """
        Actualiza la dirección del cliente y muestra un mensaje de confirmación.
        
        Parámetros:
            nueva_direccion (str): La nueva dirección
            
        Lanza:
            ValidacionError: Si la dirección no es válida
            
        Ejemplo:
            cliente.actualizar_direccion("Nueva Calle 456, Santiago")
            # Imprime: "Dirección actualizada correctamente"
        """
        # Actualizamos la dirección (esto ya valida automáticamente)
        self.set_direccion(nueva_direccion)
        # Mostramos mensaje de confirmación
        print("Dirección actualizada correctamente")
    
    def obtener_resumen(self):
        """
        Retorna un diccionario con todos los datos del cliente.
        
        Este método es útil para:
        - Guardar datos en archivos JSON
        - Enviar información a otras partes del sistema
        - Generar reportes
        
        Retorna:
            dict: Diccionario con las claves: nombre, email, telefono, direccion
            
        Ejemplo:
            resumen = cliente.obtener_resumen()
            print(resumen)
            # {'nombre': 'Juan Pérez', 'email': 'juan@email.com', ...}
        """
        return {
            'nombre': self._nombre,
            'email': self._email,
            'telefono': self._telefono,
            'direccion': self._direccion
        }
    
    # ========== MÉTODOS ESPECIALES DE PYTHON ==========
    
    def __str__(self):
        """
        Retorna una representación en texto del cliente.
        
        Este método se llama automáticamente cuando hacemos print(cliente)
        o str(cliente).
        
        Retorna:
            str: Información básica del cliente en una línea
            
        Ejemplo:
            print(cliente)
            # Cliente: Juan Pérez | Email: juan@email.com | Teléfono: +56912345678
        """
        return f"Cliente: {self._nombre} | Email: {self._email} | Teléfono: {self._telefono}"
    
    def __repr__(self):
        """
        Retorna una representación técnica del cliente.
        
        Este método se usa para debugging y en la consola interactiva.
        
        Retorna:
            str: Representación que podría usarse para recrear el objeto
            
        Ejemplo:
            cliente
            # Cliente(nombre='Juan Pérez', email='juan@email.com', ...)
        """
        return (f"Cliente(nombre='{self._nombre}', email='{self._email}', "
                f"telefono='{self._telefono}', direccion='{self._direccion}')")
