"""
Gestor de Clientes - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Este módulo proporciona una clase SIMPLE para gestionar múltiples clientes.
Permite agregar, buscar, listar, actualizar y eliminar clientes.
Código comentado línea por línea para principiantes.
"""

# Importamos las clases de clientes
from .cliente import Cliente
from .cliente_regular import ClienteRegular
from .cliente_premium import ClientePremium
from .cliente_corporativo import ClienteCorporativo

# Importamos el sistema de persistencia
from .persistencia import PersistenciaJSON

# Importamos el sistema de logs
from .logs import SistemaLogs

# Importamos las excepciones
from .excepciones import ClienteNoEncontradoError, ClienteDuplicadoError


class GestorClientes:
    """
    Clase que gestiona una colección de clientes.
    
    Esta clase permite:
    - Agregar nuevos clientes
    - Buscar clientes por email
    - Listar todos los clientes
    - Eliminar clientes
    - Guardar y cargar datos desde archivo
    
    Usa una lista interna para almacenar los clientes en memoria.
    """
    
    def __init__(self, usar_persistencia=True, usar_logs=True):
        """
        Inicializa el gestor de clientes.
        
        Parámetros:
            usar_persistencia (bool): Si True, guarda/carga desde archivo JSON
            usar_logs (bool): Si True, registra operaciones en archivo de logs
            
        Ejemplo:
            gestor = GestorClientes()
        """
        # Lista para almacenar los clientes en memoria
        self._clientes = []
        
        # Configuración de persistencia
        self.usar_persistencia = usar_persistencia
        if usar_persistencia:
            # Creamos el sistema de persistencia
            self.persistencia = PersistenciaJSON("clientes.json")
            # Intentamos cargar clientes existentes
            self._cargar_clientes()
        
        # Configuración de logs
        self.usar_logs = usar_logs
        if usar_logs:
            # Creamos el sistema de logs
            self.logs = SistemaLogs("gic_logs.txt")
            self.logs.info("Gestor de Clientes iniciado")
    
    # ========== MÉTODOS PARA AGREGAR CLIENTES ==========
    
    def agregar_cliente(self, cliente):
        """
        Agrega un cliente al gestor.
        
        Parámetros:
            cliente: Instancia de Cliente (o sus subclases)
            
        Lanza:
            ClienteDuplicadoError: Si ya existe un cliente con ese email
            
        Ejemplo:
            gestor.agregar_cliente(cliente1)
        """
        # Verificamos que el cliente no exista ya (por email)
        if self._buscar_por_email_interno(cliente.get_email()):
            raise ClienteDuplicadoError(f"Ya existe un cliente con email {cliente.get_email()}")
        
        # Agregamos el cliente a la lista
        self._clientes.append(cliente)
        
        # Registramos en logs
        if self.usar_logs:
            tipo = cliente.obtener_resumen().get('tipo_cliente', 'Regular')
            self.logs.registrar_operacion("Agregar", cliente.get_email(), f"Tipo: {tipo}")
        
        # Guardamos en archivo si está habilitada la persistencia
        if self.usar_persistencia:
            self.persistencia.guardar_cliente(cliente)
        
        print(f"✓ Cliente {cliente.get_nombre()} agregado exitosamente")
    
    # ========== MÉTODOS PARA BUSCAR CLIENTES ==========
    
    def buscar_por_email(self, email):
        """
        Busca un cliente por su email.
        
        Parámetros:
            email (str): Email del cliente a buscar
            
        Retorna:
            Cliente: El objeto cliente encontrado
            
        Lanza:
            ClienteNoEncontradoError: Si no se encuentra el cliente
            
        Ejemplo:
            cliente = gestor.buscar_por_email("juan@email.com")
            cliente.mostrar_informacion()
        """
        # Buscamos el cliente
        cliente = self._buscar_por_email_interno(email)
        
        if cliente:
            return cliente
        else:
            raise ClienteNoEncontradoError(f"No se encontró cliente con email: {email}")
    
    def buscar_por_nombre(self, nombre):
        """
        Busca clientes por nombre (búsqueda parcial).
        
        Parámetros:
            nombre (str): Nombre o parte del nombre a buscar
            
        Retorna:
            list: Lista de clientes que coinciden
            
        Ejemplo:
            clientes = gestor.buscar_por_nombre("Juan")
            for cliente in clientes:
                print(cliente.get_nombre())
        """
        # Convertimos a minúsculas para búsqueda insensible a mayúsculas
        nombre_buscar = nombre.lower().strip()
        
        # Lista para almacenar clientes encontrados
        encontrados = []
        
        # Buscamos en todos los clientes
        for cliente in self._clientes:
            # Si el nombre del cliente contiene el texto buscado
            if nombre_buscar in cliente.get_nombre().lower():
                encontrados.append(cliente)
        
        print(f"Se encontraron {len(encontrados)} cliente(s) con nombre '{nombre}'")
        return encontrados
    
    # ========== MÉTODOS PARA LISTAR CLIENTES ==========
    
    def listar_todos(self):
        """
        Retorna la lista completa de clientes.
        
        Retorna:
            list: Lista con todos los clientes
            
        Ejemplo:
            clientes = gestor.listar_todos()
            print(f"Total: {len(clientes)} clientes")
        """
        return self._clientes
    
    def listar_por_tipo(self, tipo_cliente):
        """
        Lista solo los clientes de un tipo específico.
        
        Parámetros:
            tipo_cliente (str): Tipo a buscar ("Regular", "Premium", "Corporativo")
            
        Retorna:
            list: Lista de clientes del tipo especificado
            
        Ejemplo:
            premium = gestor.listar_por_tipo("Premium")
            print(f"Clientes premium: {len(premium)}")
        """
        # Lista para almacenar clientes del tipo buscado
        filtrados = []
        
        # Filtramos por tipo
        for cliente in self._clientes:
            tipo = cliente.obtener_resumen().get('tipo_cliente', 'Regular')
            if tipo == tipo_cliente:
                filtrados.append(cliente)
        
        print(f"Se encontraron {len(filtrados)} cliente(s) de tipo '{tipo_cliente}'")
        return filtrados
    
    def mostrar_resumen(self):
        """
        Muestra un resumen de todos los clientes registrados.
        
        Ejemplo:
            gestor.mostrar_resumen()
        """
        print("\n" + "=" * 70)
        print("RESUMEN DEL GESTOR DE CLIENTES")
        print("=" * 70)
        print(f"Total de clientes: {len(self._clientes)}")
        
        # Contamos por tipo
        tipos = {'Regular': 0, 'Premium': 0, 'Corporativo': 0}
        for cliente in self._clientes:
            tipo = cliente.obtener_resumen().get('tipo_cliente', 'Regular')
            tipos[tipo] = tipos.get(tipo, 0) + 1
        
        print(f"  - Clientes Regular:     {tipos['Regular']}")
        print(f"  - Clientes Premium:     {tipos['Premium']}")
        print(f"  - Clientes Corporativo: {tipos['Corporativo']}")
        print("=" * 70)
        
        # Mostramos lista de todos
        if self._clientes:
            print("\nLISTA DE CLIENTES:")
            for i, cliente in enumerate(self._clientes, 1):
                print(f"{i}. {cliente}")
        else:
            print("\nNo hay clientes registrados")
        print("=" * 70 + "\n")
    
    # ========== MÉTODOS PARA ACTUALIZAR CLIENTES ==========
    
    def actualizar_cliente(self, email, **kwargs):
        """
        Actualiza los datos de un cliente.
        
        Parámetros:
            email (str): Email del cliente a actualizar
            **kwargs: Pares clave=valor con los datos a actualizar
                     (nombre, telefono, direccion, etc.)
            
        Ejemplo:
            gestor.actualizar_cliente("juan@email.com", 
                                     telefono="+56987654321",
                                     direccion="Nueva Calle 123")
        """
        # Buscamos el cliente
        cliente = self.buscar_por_email(email)
        
        # Actualizamos los campos proporcionados
        if 'nombre' in kwargs:
            cliente.set_nombre(kwargs['nombre'])
        if 'telefono' in kwargs:
            cliente.actualizar_telefono(kwargs['telefono'])
        if 'direccion' in kwargs:
            cliente.actualizar_direccion(kwargs['direccion'])
        
        # Registramos en logs
        if self.usar_logs:
            self.logs.registrar_operacion("Actualizar", email, f"Campos: {list(kwargs.keys())}")
        
        # Guardamos cambios
        if self.usar_persistencia:
            self.guardar_todos()
        
        print(f"✓ Cliente {email} actualizado exitosamente")
    
    # ========== MÉTODOS PARA ELIMINAR CLIENTES ==========
    
    def eliminar_cliente(self, email):
        """
        Elimina un cliente por su email.
        
        Parámetros:
            email (str): Email del cliente a eliminar
            
        Retorna:
            bool: True si se eliminó, False si no se encontró
            
        Ejemplo:
            if gestor.eliminar_cliente("juan@email.com"):
                print("Cliente eliminado")
        """
        # Buscamos el cliente
        email_buscar = email.lower().strip()
        
        # Buscamos y eliminamos
        for i, cliente in enumerate(self._clientes):
            if cliente.get_email().lower() == email_buscar:
                # Eliminamos de la lista
                eliminado = self._clientes.pop(i)
                
                # Registramos en logs
                if self.usar_logs:
                    self.logs.registrar_operacion("Eliminar", email, f"Cliente: {eliminado.get_nombre()}")
                
                # Guardamos cambios
                if self.usar_persistencia:
                    self.guardar_todos()
                
                print(f"✓ Cliente {eliminado.get_nombre()} eliminado exitosamente")
                return True
        
        # Si no lo encontramos
        print(f"✗ No se encontró cliente con email: {email}")
        return False
    
    # ========== MÉTODOS DE PERSISTENCIA ==========
    
    def guardar_todos(self):
        """
        Guarda todos los clientes en el archivo JSON.
        
        Ejemplo:
            gestor.guardar_todos()
        """
        if self.usar_persistencia:
            self.persistencia.guardar_multiples(self._clientes)
            if self.usar_logs:
                self.logs.info(f"Se guardaron {len(self._clientes)} clientes en archivo")
        else:
            print("Persistencia deshabilitada")
    
    def _cargar_clientes(self):
        """
        Método privado para cargar clientes del archivo al iniciar.
        """
        try:
            # Cargamos objetos desde el archivo
            self._clientes = self.persistencia.cargar_objetos()
            if self.usar_logs:
                self.logs.info(f"Se cargaron {len(self._clientes)} clientes desde archivo")
        except Exception as e:
            print(f"Error al cargar clientes: {e}")
            self._clientes = []
    
    # ========== MÉTODOS PRIVADOS (HELPER) ==========
    
    def _buscar_por_email_interno(self, email):
        """
        Método privado para buscar un cliente por email.
        
        Retorna el objeto o None si no se encuentra.
        """
        email_buscar = email.lower().strip()
        
        for cliente in self._clientes:
            if cliente.get_email().lower() == email_buscar:
                return cliente
        
        return None
    
    # ========== MÉTODOS ESPECIALES ==========
    
    def __len__(self):
        """
        Retorna la cantidad de clientes.
        
        Permite usar len(gestor) para obtener el número de clientes.
        
        Ejemplo:
            print(f"Total: {len(gestor)} clientes")
        """
        return len(self._clientes)
    
    def __str__(self):
        """
        Retorna una representación en texto del gestor.
        
        Ejemplo:
            print(gestor)
        """
        return f"GestorClientes(total={len(self._clientes)} clientes)"
