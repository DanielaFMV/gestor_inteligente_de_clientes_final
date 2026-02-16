# Sistema de logs para el proyecto GIC

import logging
import os


class SistemaLogs:
    """Clase para registrar eventos del sistema en un archivo de texto."""

    def __init__(self, nombre_archivo="gic_logs.txt"):
        self.nombre_archivo = nombre_archivo

        logging.basicConfig(
            filename=self.nombre_archivo,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        self.logger = logging.getLogger()
        self.info("Sistema de logs iniciado")

    def info(self, mensaje):
        self.logger.info(mensaje)
        print(f"[INFO] {mensaje}")

    def error(self, mensaje):
        self.logger.error(mensaje)
        print(f"[ERROR] {mensaje}")

    def warning(self, mensaje):
        self.logger.warning(mensaje)
        print(f"[WARNING] {mensaje}")

    def registrar_operacion(self, operacion, cliente_email, detalles=""):
        if detalles:
            mensaje = f"Operacion: {operacion} | Cliente: {cliente_email} | {detalles}"
        else:
            mensaje = f"Operacion: {operacion} | Cliente: {cliente_email}"
        self.info(mensaje)

    def registrar_error(self, operacion, descripcion_error):
        self.error(f"Error en {operacion}: {descripcion_error}")

    def leer_logs(self, ultimas_lineas=20):
        if not os.path.exists(self.nombre_archivo):
            print("No hay archivo de logs todavía")
            return []

        with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        ultimas = lineas[-ultimas_lineas:]
        print("\n--- Últimas líneas del log ---")
        for linea in ultimas:
            print(linea.strip())
        return ultimas

    def limpiar_logs(self):
        with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
            pass
        print("Logs limpiados")
