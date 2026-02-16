"""
Sistema de Logs - Gestor Inteligente de Clientes
Proyecto: GIC Simplificado para Principiantes
Empresa: SolutionTech

Este módulo proporciona un sistema SIMPLE de logs (registros) para
guardar eventos del sistema en un archivo de texto.
Código comentado línea por línea para principiantes.
"""

# Importamos los módulos necesarios
import logging  # Módulo estándar de Python para logs
from datetime import datetime  # Para obtener la fecha y hora actual
import os  # Para trabajar con rutas de archivos


class SistemaLogs:
    """
    Clase simple para manejar logs (registros) del sistema.
    
    Los logs son registros de lo que sucede en el sistema:
    - Creación de clientes
    - Errores que ocurren
    - Operaciones importantes
    
    Guarda todo en un archivo de texto para poder revisar después.
    """
    
    def __init__(self, nombre_archivo="gic_logs.txt"):
        """
        Inicializa el sistema de logs.
        
        Parámetros:
            nombre_archivo (str): Nombre del archivo donde se guardarán los logs
            
        Ejemplo:
            logs = SistemaLogs("mi_sistema.txt")
        """
        # Guardamos el nombre del archivo
        self.nombre_archivo = nombre_archivo
        
        # Configuramos el sistema de logging de Python
        # logging.basicConfig configura el logger principal
        logging.basicConfig(
            # filename: donde se guardarán los logs
            filename=self.nombre_archivo,
            # level: nivel mínimo de mensajes a guardar (INFO guarda INFO, WARNING, ERROR, CRITICAL)
            level=logging.INFO,
            # format: cómo se verá cada línea de log
            # %(asctime)s = fecha y hora
            # %(levelname)s = nivel (INFO, ERROR, etc.)
            # %(message)s = el mensaje
            format='%(asctime)s - %(levelname)s - %(message)s',
            # datefmt: formato de la fecha
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Obtenemos una referencia al logger
        self.logger = logging.getLogger()
        
        # Registramos que el sistema de logs se inició
        self.info("Sistema de logs iniciado")
    
    def info(self, mensaje):
        """
        Registra un mensaje de información (eventos normales).
        
        Parámetros:
            mensaje (str): El mensaje a registrar
            
        Ejemplo:
            logs.info("Cliente Juan Pérez creado exitosamente")
        """
        # logging.INFO es para eventos normales e informativos
        self.logger.info(mensaje)
        # También lo mostramos en consola para que el usuario lo vea
        print(f"[INFO] {mensaje}")
    
    def error(self, mensaje):
        """
        Registra un mensaje de error (cuando algo sale mal).
        
        Parámetros:
            mensaje (str): El mensaje de error a registrar
            
        Ejemplo:
            logs.error("Error al validar email: formato inválido")
        """
        # logging.ERROR es para errores
        self.logger.error(mensaje)
        # También lo mostramos en consola
        print(f"[ERROR] {mensaje}")
    
    def warning(self, mensaje):
        """
        Registra un mensaje de advertencia (situaciones que merecen atención).
        
        Parámetros:
            mensaje (str): El mensaje de advertencia a registrar
            
        Ejemplo:
            logs.warning("Cliente intentó canjear más puntos de los disponibles")
        """
        # logging.WARNING es para advertencias
        self.logger.warning(mensaje)
        # También lo mostramos en consola
        print(f"[WARNING] {mensaje}")
    
    def registrar_operacion(self, operacion, cliente_email, detalles=""):
        """
        Registra una operación realizada sobre un cliente.
        
        Parámetros:
            operacion (str): Tipo de operación (Crear, Actualizar, Eliminar, etc.)
            cliente_email (str): Email del cliente afectado
            detalles (str): Detalles adicionales de la operación
            
        Ejemplo:
            logs.registrar_operacion("Crear", "juan@email.com", "Cliente Regular")
        """
        # Creamos el mensaje con todos los detalles
        if detalles:
            mensaje = f"OPERACIÓN: {operacion} | Cliente: {cliente_email} | Detalles: {detalles}"
        else:
            mensaje = f"OPERACIÓN: {operacion} | Cliente: {cliente_email}"
        
        # Registramos como información
        self.info(mensaje)
    
    def registrar_error(self, operacion, error_descripcion):
        """
        Registra un error que ocurrió durante una operación.
        
        Parámetros:
            operacion (str): Operación que se estaba realizando
            error_descripcion (str): Descripción del error
            
        Ejemplo:
            logs.registrar_error("Validar Email", "Email sin formato correcto")
        """
        # Creamos el mensaje de error
        mensaje = f"ERROR en {operacion}: {error_descripcion}"
        # Registramos como error
        self.error(mensaje)
    
    def leer_logs(self, ultimas_lineas=50):
        """
        Lee y muestra las últimas líneas del archivo de logs.
        
        Parámetros:
            ultimas_lineas (int): Cuántas líneas mostrar (default: 50)
            
        Retorna:
            list: Lista con las líneas del log
            
        Ejemplo:
            logs.leer_logs(10)  # Muestra las últimas 10 líneas
        """
        # Verificamos que el archivo exista
        if not os.path.exists(self.nombre_archivo):
            print(f"El archivo de logs '{self.nombre_archivo}' no existe aún")
            return []
        
        # Abrimos el archivo y leemos todas las líneas
        with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
            # readlines() lee todas las líneas del archivo
            lineas = archivo.readlines()
        
        # Obtenemos solo las últimas N líneas
        # [-ultimas_lineas:] toma los últimos elementos de la lista
        lineas_a_mostrar = lineas[-ultimas_lineas:]
        
        # Mostramos las líneas
        print("\n" + "=" * 70)
        print(f"ÚLTIMAS {len(lineas_a_mostrar)} LÍNEAS DEL LOG")
        print("=" * 70)
        for linea in lineas_a_mostrar:
            # strip() elimina el salto de línea al final
            print(linea.strip())
        print("=" * 70 + "\n")
        
        return lineas_a_mostrar
    
    def limpiar_logs(self):
        """
        Limpia (borra) todo el contenido del archivo de logs.
        
        ¡ADVERTENCIA! Esta operación no se puede deshacer.
        
        Ejemplo:
            logs.limpiar_logs()
        """
        # Abrimos el archivo en modo 'w' (write), lo cual lo vacía
        with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
            # No escribimos nada, el archivo queda vacío
            pass
        
        # Registramos que se limpió el log
        self.info("Archivo de logs limpiado")
        print(f"Archivo de logs '{self.nombre_archivo}' limpiado")


# Función helper para crear un logger global
def crear_logger(nombre_archivo="gic_logs.txt"):
    """
    Función auxiliar para crear un sistema de logs.
    
    Parámetros:
        nombre_archivo (str): Nombre del archivo de logs
        
    Retorna:
        SistemaLogs: Instancia del sistema de logs
        
    Ejemplo:
        logs = crear_logger("mi_sistema.txt")
        logs.info("Sistema iniciado")
    """
    return SistemaLogs(nombre_archivo)
