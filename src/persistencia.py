"""
Sistema de Persistencia - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Este módulo proporciona funciones SIMPLES para guardar y cargar
datos de clientes en formato JSON.
Código comentado línea por línea para principiantes.
"""

# Importamos los módulos necesarios
import json  # Para trabajar con archivos JSON
import os  # Para verificar si archivos existen

# Importamos nuestras clases de cliente
from .cliente import Cliente
from .cliente_regular import ClienteRegular
from .cliente_premium import ClientePremium
from .cliente_corporativo import ClienteCorporativo

# Importamos las excepciones
from .excepciones import PersistenciaError

# Importamos datetime para manejar fechas
from datetime import date


class PersistenciaJSON:
    """
    Clase simple para guardar y cargar clientes en formato JSON.
    
    JSON es un formato de texto que permite guardar datos estructurados.
    Es fácil de leer tanto para humanos como para computadoras.
    
    Ejemplo de JSON:
    {
        "nombre": "Juan Pérez",
        "email": "juan@email.com"
    }
    """
    
    def __init__(self, nombre_archivo="clientes.json"):
        """
        Inicializa el sistema de persistencia.
        
        Parámetros:
            nombre_archivo (str): Nombre del archivo JSON donde guardar los datos
            
        Ejemplo:
            persistencia = PersistenciaJSON("mi_base_datos.json")
        """
        # Guardamos el nombre del archivo
        self.nombre_archivo = nombre_archivo
    
    def guardar_cliente(self, cliente):
        """
        Guarda UN cliente en el archivo JSON.
        
        Si el archivo ya existe, agrega el cliente a la lista existente.
        Si el archivo no existe, lo crea.
        
        Parámetros:
            cliente: Instancia de Cliente (o sus subclases)
            
        Lanza:
            PersistenciaError: Si hay problemas al guardar
            
        Ejemplo:
            persistencia.guardar_cliente(cliente1)
        """
        try:
            # Primero cargamos los clientes existentes (si hay)
            clientes_existentes = self.cargar_todos()
            
            # Convertimos el cliente a diccionario
            cliente_dict = cliente.obtener_resumen()
            
            # Verificamos si el cliente ya existe (por email)
            # Recorremos la lista de clientes existentes
            for i, cli in enumerate(clientes_existentes):
                # Si encontramos un cliente con el mismo email
                if cli.get('email') == cliente_dict['email']:
                    # Lo actualizamos (reemplazamos)
                    clientes_existentes[i] = cliente_dict
                    print(f"Cliente {cliente_dict['email']} actualizado en archivo")
                    # Guardamos y salimos
                    self._guardar_lista(clientes_existentes)
                    return
            
            # Si llegamos aquí, el cliente no existía, lo agregamos
            clientes_existentes.append(cliente_dict)
            print(f"Cliente {cliente_dict['email']} guardado en archivo")
            
            # Guardamos la lista actualizada
            self._guardar_lista(clientes_existentes)
            
        except Exception as e:
            # Si hay algún error, lanzamos excepción personalizada
            raise PersistenciaError(f"Error al guardar cliente: {str(e)}")
    
    def guardar_multiples(self, lista_clientes):
        """
        Guarda MÚLTIPLES clientes en el archivo JSON.
        
        Parámetros:
            lista_clientes (list): Lista de objetos Cliente
            
        Lanza:
            PersistenciaError: Si hay problemas al guardar
            
        Ejemplo:
            persistencia.guardar_multiples([cliente1, cliente2, cliente3])
        """
        try:
            # Convertimos cada cliente a diccionario
            clientes_dict = []
            for cliente in lista_clientes:
                # Obtenemos el resumen (diccionario) de cada cliente
                cliente_dict = cliente.obtener_resumen()
                clientes_dict.append(cliente_dict)
            
            # Guardamos la lista completa
            self._guardar_lista(clientes_dict)
            print(f"{len(clientes_dict)} clientes guardados en archivo")
            
        except Exception as e:
            raise PersistenciaError(f"Error al guardar múltiples clientes: {str(e)}")
    
    def cargar_todos(self):
        """
        Carga TODOS los clientes del archivo JSON.
        
        Retorna:
            list: Lista de diccionarios con datos de clientes
            
        Ejemplo:
            clientes = persistencia.cargar_todos()
            for cliente in clientes:
                print(cliente['nombre'])
        """
        try:
            # Verificamos si el archivo existe
            if not os.path.exists(self.nombre_archivo):
                # Si no existe, retornamos lista vacía
                print(f"Archivo {self.nombre_archivo} no existe. Retornando lista vacía.")
                return []
            
            # Abrimos el archivo y leemos el JSON
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                # json.load() convierte el JSON en lista de Python
                clientes = json.load(archivo)
                return clientes
            
        except json.JSONDecodeError:
            # Si el archivo JSON está corrupto
            print(f"Advertencia: El archivo {self.nombre_archivo} está corrupto. Retornando lista vacía.")
            return []
        except Exception as e:
            raise PersistenciaError(f"Error al cargar clientes: {str(e)}")
    
    def cargar_objetos(self):
        """
        Carga todos los clientes y los convierte en objetos (instancias de clases).
        
        Retorna:
            list: Lista de objetos Cliente, ClienteRegular, ClientePremium, etc.
            
        Ejemplo:
            objetos = persistencia.cargar_objetos()
            for cliente in objetos:
                cliente.mostrar_informacion()
        """
        try:
            # Cargamos los diccionarios
            clientes_dict = self.cargar_todos()
            
            # Lista para almacenar los objetos
            objetos = []
            
            # Convertimos cada diccionario en objeto
            for cli_dict in clientes_dict:
                # Creamos el objeto según el tipo
                objeto = self._dict_a_objeto(cli_dict)
                if objeto:
                    objetos.append(objeto)
            
            print(f"{len(objetos)} clientes cargados como objetos")
            return objetos
            
        except Exception as e:
            raise PersistenciaError(f"Error al cargar objetos: {str(e)}")
    
    def buscar_por_email(self, email):
        """
        Busca un cliente por su email.
        
        Parámetros:
            email (str): Email del cliente a buscar
            
        Retorna:
            dict o None: Diccionario con datos del cliente o None si no se encuentra
            
        Ejemplo:
            cliente = persistencia.buscar_por_email("juan@email.com")
            if cliente:
                print(f"Cliente encontrado: {cliente['nombre']}")
        """
        # Cargamos todos los clientes
        clientes = self.cargar_todos()
        
        # Convertimos el email a minúsculas para comparar
        email_buscar = email.lower().strip()
        
        # Buscamos el cliente
        for cliente in clientes:
            if cliente.get('email', '').lower() == email_buscar:
                print(f"Cliente encontrado: {cliente.get('nombre')}")
                return cliente
        
        # Si no lo encontramos
        print(f"No se encontró cliente con email: {email}")
        return None
    
    def eliminar_por_email(self, email):
        """
        Elimina un cliente por su email.
        
        Parámetros:
            email (str): Email del cliente a eliminar
            
        Retorna:
            bool: True si se eliminó, False si no se encontró
            
        Ejemplo:
            if persistencia.eliminar_por_email("juan@email.com"):
                print("Cliente eliminado")
        """
        try:
            # Cargamos todos los clientes
            clientes = self.cargar_todos()
            
            # Convertimos el email a minúsculas
            email_buscar = email.lower().strip()
            
            # Buscamos y eliminamos el cliente
            for i, cliente in enumerate(clientes):
                if cliente.get('email', '').lower() == email_buscar:
                    # Eliminamos el cliente de la lista
                    eliminado = clientes.pop(i)
                    # Guardamos la lista actualizada
                    self._guardar_lista(clientes)
                    print(f"Cliente {eliminado.get('nombre')} eliminado")
                    return True
            
            # Si no lo encontramos
            print(f"No se encontró cliente con email: {email}")
            return False
            
        except Exception as e:
            raise PersistenciaError(f"Error al eliminar cliente: {str(e)}")
    
    def limpiar_archivo(self):
        """
        Limpia (elimina todos) los clientes del archivo.
        
        ¡ADVERTENCIA! Esta operación no se puede deshacer.
        
        Ejemplo:
            persistencia.limpiar_archivo()
        """
        self._guardar_lista([])
        print(f"Archivo {self.nombre_archivo} limpiado")
    
    # ========== MÉTODOS PRIVADOS (HELPER) ==========
    
    def _guardar_lista(self, lista_clientes):
        """
        Método privado para guardar una lista en el archivo JSON.
        
        Parámetros:
            lista_clientes (list): Lista de diccionarios a guardar
        """
        # Abrimos el archivo en modo escritura
        with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
            # json.dump() convierte la lista a JSON y lo guarda
            # indent=2 hace que el JSON sea más legible (con sangrías)
            # ensure_ascii=False permite caracteres especiales (tildes, ñ)
            json.dump(lista_clientes, archivo, indent=2, ensure_ascii=False)
    
    def _dict_a_objeto(self, cliente_dict):
        """
        Método privado para convertir un diccionario en objeto Cliente.
        
        Parámetros:
            cliente_dict (dict): Diccionario con datos del cliente
            
        Retorna:
            Cliente: Objeto de la clase correspondiente
        """
        try:
            # Obtenemos el tipo de cliente
            tipo = cliente_dict.get('tipo_cliente', 'Regular')
            
            # Datos comunes
            nombre = cliente_dict['nombre']
            email = cliente_dict['email']
            telefono = cliente_dict['telefono']
            direccion = cliente_dict['direccion']
            
            # Creamos el objeto según el tipo
            if tipo == 'Premium':
                # Cliente Premium
                nivel = cliente_dict.get('nivel_membresia', 'Bronce')
                descuento = cliente_dict.get('descuento', 10.0)
                cliente = ClientePremium(nombre, email, telefono, direccion, nivel, descuento)
                # Restauramos los puntos
                puntos = cliente_dict.get('puntos_acumulados', 0)
                cliente.set_puntos_acumulados(puntos)
                return cliente
                
            elif tipo == 'Corporativo':
                # Cliente Corporativo
                nombre_empresa = cliente_dict.get('nombre_empresa', 'Sin nombre')
                rut_empresa = cliente_dict.get('rut_empresa', '00.000.000-0')
                contacto = cliente_dict.get('contacto_principal', nombre)
                limite = cliente_dict.get('limite_credito', 100000.0)
                cliente = ClienteCorporativo(nombre, email, telefono, direccion,
                                            nombre_empresa, rut_empresa, contacto, limite)
                # Restauramos el crédito utilizado
                utilizado = cliente_dict.get('credito_utilizado', 0.0)
                cliente._credito_utilizado = utilizado
                return cliente
                
            else:
                # Cliente Regular (por defecto)
                cliente = ClienteRegular(nombre, email, telefono, direccion)
                # Restauramos la fecha de registro si existe
                if 'fecha_registro' in cliente_dict:
                    # Convertimos el string de fecha a objeto date
                    fecha_str = cliente_dict['fecha_registro']
                    # Formato: "2026-02-15" -> date(2026, 2, 15)
                    fecha_parts = fecha_str.split('-')
                    if len(fecha_parts) == 3:
                        fecha = date(int(fecha_parts[0]), int(fecha_parts[1]), int(fecha_parts[2]))
                        cliente.set_fecha_registro(fecha)
                return cliente
                
        except Exception as e:
            print(f"Error al convertir diccionario a objeto: {e}")
            return None
