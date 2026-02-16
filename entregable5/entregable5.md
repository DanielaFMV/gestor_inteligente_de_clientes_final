# Entregable 5: Manejo de Errores y Excepciones

**Estudiante:** [Tu Nombre]  
**Proyecto:** Gestor Inteligente de Clientes (GIC)  
**Empresa:** SolutionTech  
**Fecha:** Febrero 2026

---

## 1. Introducción

Este entregable implementa un sistema robusto de **manejo de errores** en el proyecto GIC, utilizando excepciones personalizadas, validaciones de datos y un sistema de logging para rastrear eventos y errores del sistema.

## 2. Excepciones en Python

### 2.1 ¿Qué son las Excepciones?

Las excepciones son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de instrucciones. Python utiliza excepciones para manejar errores de manera controlada.

**Tipos de errores:**
- **SyntaxError:** Error en la sintaxis del código
- **NameError:** Variable no definida
- **TypeError:** Tipo de dato incorrecto
- **ValueError:** Valor incorrecto
- **KeyError:** Clave no existe en diccionario
- **IndexError:** Índice fuera de rango

### 2.2 Estructura try-except

```python
try:
    # Código que puede generar un error
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si hay error
    print("Error: División por cero")
```

### 2.3 Múltiples Excepciones

```python
try:
    valor = int(input("Ingrese un número: "))
    resultado = 100 / valor
except ValueError:
    print("Error: Debe ingresar un número válido")
except ZeroDivisionError:
    print("Error: No puede dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
```

### 2.4 Bloques else y finally

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
else:
    # Se ejecuta si NO hay excepciones
    print("Archivo leído correctamente")
finally:
    # Se ejecuta SIEMPRE (haya o no excepción)
    if 'archivo' in locals():
        archivo.close()
```

## 3. Excepciones Personalizadas en GIC

### 3.1 ¿Por qué Crear Excepciones Personalizadas?

Las excepciones personalizadas permiten:
- **Claridad:** Errores específicos del dominio del problema
- **Mantenibilidad:** Más fácil identificar y corregir problemas
- **Control:** Manejo diferenciado según el tipo de error
- **Documentación:** El nombre de la excepción describe el problema

### 3.2 Definición de Excepciones Personalizadas

En el archivo `excepciones.py`:

```python
class ValidacionError(Exception):
    """
    Excepción que se lanza cuando falla la validación de datos.
    
    Uso:
        raise ValidacionError("El email no es válido")
    """
    pass


class ClienteNoEncontradoError(Exception):
    """
    Excepción que se lanza cuando no se encuentra un cliente.
    
    Uso:
        raise ClienteNoEncontradoError("Cliente con email juan@email.com no encontrado")
    """
    pass


class ClienteDuplicadoError(Exception):
    """
    Excepción que se lanza cuando se intenta agregar un cliente duplicado.
    
    Uso:
        raise ClienteDuplicadoError("Ya existe un cliente con este email")
    """
    pass


class PersistenciaError(Exception):
    """
    Excepción que se lanza cuando hay problemas con la persistencia de datos.
    
    Uso:
        raise PersistenciaError("No se pudo guardar el archivo clientes.json")
    """
    pass
```

### 3.3 Herencia de Excepciones

Las excepciones personalizadas heredan de `Exception`:

```python
# Jerarquía de excepciones
Exception (clase base de Python)
    |
    +-- ValidacionError
    |
    +-- ClienteNoEncontradoError
    |
    +-- ClienteDuplicadoError
    |
    +-- PersistenciaError
```

### 3.4 Excepciones con Información Adicional

```python
class ValidacionError(Exception):
    def __init__(self, campo, mensaje):
        self.campo = campo
        self.mensaje = mensaje
        super().__init__(f"Error en {campo}: {mensaje}")

# Uso
raise ValidacionError("email", "El formato no es válido")
```

## 4. Sistema de Validaciones

### 4.1 Validación de Email

```python
import re

def validar_email(email):
    """
    Valida que el email tenga formato correcto.
    
    Raises:
        ValidacionError: Si el email no es válido
    """
    if not email or not isinstance(email, str):
        raise ValidacionError("El email no puede estar vacío")
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(patron, email):
        raise ValidacionError(f"El email '{email}' no tiene un formato válido")
    
    return True
```

**Ejemplos:**
- ✅ `juan.perez@email.com` → Válido
- ✅ `maria_lopez123@empresa.cl` → Válido
- ❌ `email_sin_arroba` → ValidacionError
- ❌ `@sinusuario.com` → ValidacionError

### 4.2 Validación de Teléfono

```python
def validar_telefono(telefono):
    """
    Valida que el teléfono sea un número chileno válido.
    
    Formatos aceptados:
    - +56912345678
    - 912345678
    - +56 9 1234 5678
    
    Raises:
        ValidacionError: Si el teléfono no es válido
    """
    if not telefono or not isinstance(telefono, str):
        raise ValidacionError("El teléfono no puede estar vacío")
    
    # Eliminar espacios y guiones
    telefono_limpio = telefono.replace(" ", "").replace("-", "")
    
    # Patrón para teléfono chileno
    patron = r'^(\+?56)?[9][0-9]{8}$'
    
    if not re.match(patron, telefono_limpio):
        raise ValidacionError(
            f"El teléfono '{telefono}' no es válido. "
            "Debe ser un número chileno que empiece con 9"
        )
    
    return True
```

### 4.3 Validación de Dirección

```python
def validar_direccion(direccion):
    """
    Valida que la dirección tenga al menos 10 caracteres.
    
    Raises:
        ValidacionError: Si la dirección no es válida
    """
    if not direccion or not isinstance(direccion, str):
        raise ValidacionError("La dirección no puede estar vacía")
    
    if len(direccion.strip()) < 10:
        raise ValidacionError("La dirección debe tener al menos 10 caracteres")
    
    return True
```

### 4.4 Validación de Nombre

```python
def validar_nombre(nombre):
    """
    Valida que el nombre solo contenga letras y espacios.
    
    Raises:
        ValidacionError: Si el nombre no es válido
    """
    if not nombre or not isinstance(nombre, str):
        raise ValidacionError("El nombre no puede estar vacío")
    
    if len(nombre.strip()) < 3:
        raise ValidacionError("El nombre debe tener al menos 3 caracteres")
    
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
        raise ValidacionError("El nombre solo puede contener letras y espacios")
    
    return True
```

### 4.5 Validaciones Numéricas

```python
def validar_descuento(descuento):
    """
    Valida que el descuento esté entre 0 y 100.
    
    Raises:
        ValidacionError: Si el descuento no es válido
    """
    if not isinstance(descuento, (int, float)):
        raise ValidacionError("El descuento debe ser un número")
    
    if descuento < 0 or descuento > 100:
        raise ValidacionError(
            f"El descuento debe estar entre 0 y 100. Valor recibido: {descuento}"
        )
    
    return True


def validar_monto(monto):
    """
    Valida que el monto sea positivo.
    
    Raises:
        ValidacionError: Si el monto no es válido
    """
    if not isinstance(monto, (int, float)):
        raise ValidacionError("El monto debe ser un número")
    
    if monto <= 0:
        raise ValidacionError(f"El monto debe ser mayor a 0. Valor recibido: {monto}")
    
    return True
```

## 5. Uso de Excepciones en las Clases

### 5.1 En la Clase Cliente

```python
class Cliente:
    def set_email(self, email):
        """
        Establece el email del cliente con validación.
        
        Raises:
            ValidacionError: Si el email no es válido
        """
        validar_email(email)  # Puede lanzar ValidacionError
        self._email = email.lower().strip()
    
    def set_telefono(self, telefono):
        """
        Establece el teléfono del cliente con validación.
        
        Raises:
            ValidacionError: Si el teléfono no es válido
        """
        validar_telefono(telefono)  # Puede lanzar ValidacionError
        self._telefono = telefono.strip()
```

### 5.2 En el Gestor de Clientes

```python
class GestorClientes:
    def agregar_cliente(self, cliente):
        """
        Agrega un cliente al gestor.
        
        Raises:
            ClienteDuplicadoError: Si ya existe un cliente con ese email
        """
        if self._buscar_por_email_interno(cliente.get_email()):
            raise ClienteDuplicadoError(
                f"Ya existe un cliente con email {cliente.get_email()}"
            )
        
        self._clientes.append(cliente)
    
    def buscar_por_email(self, email):
        """
        Busca un cliente por email.
        
        Raises:
            ClienteNoEncontradoError: Si no se encuentra el cliente
        """
        cliente = self._buscar_por_email_interno(email)
        
        if not cliente:
            raise ClienteNoEncontradoError(
                f"No se encontró cliente con email: {email}"
            )
        
        return cliente
```

### 5.3 Manejo de Excepciones en el Código Cliente

```python
# Crear cliente con manejo de errores
try:
    cliente = ClienteRegular(
        nombre="Juan Pérez",
        email="juan@email.com",
        telefono="912345678",
        direccion="Av. Libertador 1234, Santiago"
    )
    print("✓ Cliente creado exitosamente")
    
except ValidacionError as e:
    print(f"✗ Error de validación: {e}")
    
except Exception as e:
    print(f"✗ Error inesperado: {e}")
```

## 6. Sistema de Logging

### 6.1 ¿Qué es el Logging?

El logging es el proceso de registrar eventos que ocurren durante la ejecución de un programa. Es fundamental para:
- **Debugging:** Identificar problemas
- **Auditoría:** Rastrear operaciones
- **Monitoreo:** Vigilar el estado del sistema
- **Análisis:** Entender el comportamiento del sistema

### 6.2 Niveles de Log

Python define 5 niveles de severidad:

| Nivel | Valor | Uso |
|-------|-------|-----|
| DEBUG | 10 | Información detallada para debugging |
| INFO | 20 | Confirmación de que todo funciona |
| WARNING | 30 | Advertencia, pero el programa continúa |
| ERROR | 40 | Error, alguna funcionalidad no funciona |
| CRITICAL | 50 | Error grave, el programa puede terminar |

### 6.3 Implementación del Sistema de Logs

```python
import logging
from datetime import datetime

class SistemaLogs:
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
        """Registra un mensaje informativo."""
        self.logger.info(mensaje)
        print(f"[INFO] {mensaje}")
    
    def error(self, mensaje):
        """Registra un mensaje de error."""
        self.logger.error(mensaje)
        print(f"[ERROR] {mensaje}")
    
    def warning(self, mensaje):
        """Registra una advertencia."""
        self.logger.warning(mensaje)
        print(f"[WARNING] {mensaje}")
    
    def registrar_operacion(self, operacion, cliente_email, detalles=""):
        """Registra una operación sobre un cliente."""
        if detalles:
            mensaje = f"OPERACIÓN: {operacion} | Cliente: {cliente_email} | Detalles: {detalles}"
        else:
            mensaje = f"OPERACIÓN: {operacion} | Cliente: {cliente_email}"
        
        self.info(mensaje)
    
    def registrar_error(self, operacion, error_descripcion):
        """Registra un error durante una operación."""
        mensaje = f"ERROR en {operacion}: {error_descripcion}"
        self.error(mensaje)
```

### 6.4 Uso del Sistema de Logs

```python
# Inicializar el sistema
logs = SistemaLogs("gic_logs.txt")

# Registrar operaciones normales
logs.info("Aplicación iniciada")
logs.registrar_operacion("Crear", "juan@email.com", "Cliente Regular")

# Registrar advertencias
logs.warning("Cliente intentó canjear más puntos de los disponibles")

# Registrar errores
try:
    validar_email("email_invalido")
except ValidacionError as e:
    logs.registrar_error("Validar Email", str(e))
```

### 6.5 Ejemplo de Archivo de Log

```
2026-02-16 10:30:15 - INFO - Sistema de logs iniciado
2026-02-16 10:30:16 - INFO - Aplicación iniciada
2026-02-16 10:30:17 - INFO - OPERACIÓN: Crear | Cliente: juan@email.com | Detalles: Cliente Regular
2026-02-16 10:30:18 - WARNING - Cliente intentó canjear más puntos de los disponibles
2026-02-16 10:30:19 - ERROR - ERROR en Validar Email: El email 'email_invalido' no tiene un formato válido
2026-02-16 10:30:20 - INFO - OPERACIÓN: Actualizar | Cliente: maria@email.com
```

## 7. Manejo de Errores en Persistencia

### 7.1 Excepciones en Archivos JSON

```python
import json

class PersistenciaJSON:
    def guardar_cliente(self, cliente):
        """
        Guarda un cliente en archivo JSON.
        
        Raises:
            PersistenciaError: Si hay problemas al guardar
        """
        try:
            clientes_existentes = self.cargar_todos()
            cliente_dict = cliente.obtener_resumen()
            clientes_existentes.append(cliente_dict)
            
            with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(clientes_existentes, archivo, indent=2, ensure_ascii=False)
                
        except IOError as e:
            raise PersistenciaError(f"Error al escribir archivo: {str(e)}")
        except Exception as e:
            raise PersistenciaError(f"Error al guardar cliente: {str(e)}")
    
    def cargar_todos(self):
        """
        Carga todos los clientes del archivo JSON.
        
        Returns:
            list: Lista de diccionarios con datos de clientes
            
        Raises:
            PersistenciaError: Si hay problemas al cargar
        """
        try:
            if not os.path.exists(self.nombre_archivo):
                return []
            
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
                
        except json.JSONDecodeError:
            raise PersistenciaError("El archivo JSON está corrupto")
        except IOError as e:
            raise PersistenciaError(f"Error al leer archivo: {str(e)}")
        except Exception as e:
            raise PersistenciaError(f"Error al cargar clientes: {str(e)}")
```

### 7.2 Manejo de Errores de Persistencia

```python
# Guardar con manejo de errores
try:
    persistencia = PersistenciaJSON("clientes.json")
    persistencia.guardar_cliente(cliente)
    print("✓ Cliente guardado exitosamente")
    
except PersistenciaError as e:
    print(f"✗ Error de persistencia: {e}")
    logs.registrar_error("Guardar Cliente", str(e))
    
except Exception as e:
    print(f"✗ Error inesperado: {e}")
    logs.registrar_error("Guardar Cliente", f"Error inesperado: {str(e)}")
```

## 8. Buenas Prácticas

### 8.1 Ser Específico con las Excepciones

✅ **Correcto:**
```python
try:
    validar_email(email)
except ValidacionError as e:
    print(f"Email inválido: {e}")
```

❌ **Evitar:**
```python
try:
    validar_email(email)
except:  # Captura TODAS las excepciones (muy genérico)
    print("Error")
```

### 8.2 No Silenciar Excepciones

❌ **Mal:**
```python
try:
    cliente = crear_cliente(datos)
except:
    pass  # Silencia el error, no sabemos qué pasó
```

✅ **Bien:**
```python
try:
    cliente = crear_cliente(datos)
except ValidacionError as e:
    logs.error(f"Error al crear cliente: {e}")
    raise  # Re-lanza la excepción
```

### 8.3 Usar finally para Limpieza

```python
archivo = None
try:
    archivo = open("datos.txt", "w")
    archivo.write("contenido")
except IOError as e:
    print(f"Error: {e}")
finally:
    if archivo:
        archivo.close()  # Se ejecuta siempre
```

### 8.4 Documentar Excepciones

```python
def buscar_cliente(email):
    """
    Busca un cliente por email.
    
    Args:
        email (str): Email del cliente a buscar
        
    Returns:
        Cliente: El cliente encontrado
        
    Raises:
        ValidacionError: Si el email no es válido
        ClienteNoEncontradoError: Si el cliente no existe
    """
    validar_email(email)
    # ...
```

## 9. Ejemplo Completo de Manejo de Errores

```python
def procesar_nuevo_cliente(datos):
    """
    Procesa y crea un nuevo cliente con manejo completo de errores.
    """
    logs = SistemaLogs()
    
    try:
        # 1. Validar datos
        logs.info("Iniciando validación de datos")
        validar_nombre(datos['nombre'])
        validar_email(datos['email'])
        validar_telefono(datos['telefono'])
        validar_direccion(datos['direccion'])
        
        # 2. Crear cliente
        logs.info(f"Creando cliente: {datos['email']}")
        cliente = ClienteRegular(
            nombre=datos['nombre'],
            email=datos['email'],
            telefono=datos['telefono'],
            direccion=datos['direccion']
        )
        
        # 3. Agregar al gestor
        gestor = GestorClientes()
        gestor.agregar_cliente(cliente)
        
        # 4. Guardar en archivo
        persistencia = PersistenciaJSON()
        persistencia.guardar_cliente(cliente)
        
        logs.registrar_operacion("Crear", datos['email'], "Cliente creado exitosamente")
        print("✓ Cliente procesado correctamente")
        
        return cliente
        
    except ValidacionError as e:
        logs.registrar_error("Validación", str(e))
        print(f"✗ Error de validación: {e}")
        return None
        
    except ClienteDuplicadoError as e:
        logs.registrar_error("Cliente Duplicado", str(e))
        print(f"✗ Cliente duplicado: {e}")
        return None
        
    except PersistenciaError as e:
        logs.registrar_error("Persistencia", str(e))
        print(f"✗ Error al guardar: {e}")
        return None
        
    except Exception as e:
        logs.registrar_error("Error Inesperado", str(e))
        print(f"✗ Error inesperado: {e}")
        return None
```

## 10. Conclusión

El sistema de manejo de errores del proyecto GIC proporciona:

✅ **Robustez:** Manejo controlado de situaciones excepcionales  
✅ **Claridad:** Excepciones específicas que describen el problema  
✅ **Trazabilidad:** Sistema de logs para auditoría y debugging  
✅ **Mantenibilidad:** Código más fácil de entender y corregir  
✅ **Confiabilidad:** El sistema no falla inesperadamente  

El uso correcto de excepciones y logging es fundamental para crear aplicaciones profesionales y confiables.

---

## Referencias

- Python Exceptions: https://docs.python.org/3/tutorial/errors.html
- Python Logging: https://docs.python.org/3/library/logging.html
- Real Python - Exception Handling: https://realpython.com/python-exceptions/
- PEP 8 - Style Guide: https://www.python.org/dev/peps/pep-0008/
