# Entregable 5: Manejo de Errores y Excepciones

**Proyecto:** Gestor Inteligente de Clientes (GIC)
**Empresa:** SolutionTech
**Fecha:** Febrero 2026

---

## 1. Introducción

En este entregable implementé el manejo de errores en el proyecto GIC. Cuando el sistema recibe datos incorrectos o algo falla al guardar información, en vez de que el programa se caiga, ahora muestra un mensaje claro y sigue funcionando. Para eso creé excepciones personalizadas, funciones de validación y un sistema de logs.

---

## 2. ¿Qué son las excepciones?

Una excepción es un error que ocurre mientras el programa está ejecutándose. Python tiene excepciones propias como `ValueError`, `TypeError` o `FileNotFoundError`, pero también se pueden crear excepciones propias para el proyecto.

Para manejar una excepción se usa el bloque `try-except`:

```python
try:
    # código que puede fallar
    numero = int("abc")
except ValueError:
    print("Error: eso no es un número")
```

Si la instrucción dentro del `try` falla, Python salta al `except` y ejecuta ese bloque en vez de terminar el programa con un error.

---

## 3. Excepciones personalizadas del proyecto

Creé 4 excepciones propias en el archivo `excepciones.py`. Todas heredan de `Exception`, que es la clase base de Python para errores:

```python
class ValidacionError(Exception):
    """Se lanza cuando un dato ingresado no es válido."""
    pass

class ClienteNoEncontradoError(Exception):
    """Se lanza cuando no se encuentra un cliente en el sistema."""
    pass

class ClienteDuplicadoError(Exception):
    """Se lanza cuando se intenta agregar un cliente que ya existe."""
    pass

class PersistenciaError(Exception):
    """Se lanza cuando hay problemas al guardar o cargar datos del archivo."""
    pass
```

Usar excepciones con nombres propios hace que sea más fácil entender qué salió mal. Si veo `ClienteNoEncontradoError` sé exactamente cuál fue el problema, sin necesidad de leer el mensaje de error completo.

---

## 4. Funciones de validación

Para asegurarme de que los datos que ingresa el usuario sean correctos antes de guardarlos, creé funciones de validación en `validaciones.py`. Cada una revisa un tipo de dato distinto y lanza `ValidacionError` si algo está mal.

### validar_email

```python
def validar_email(email):
    if not email or not isinstance(email, str):
        raise ValidacionError("El email no puede estar vacío")

    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(patron, email.strip()):
        raise ValidacionError(f"El email '{email}' no tiene formato válido")

    return True
```

### validar_telefono

```python
def validar_telefono(telefono):
    if not telefono or not isinstance(telefono, str):
        raise ValidacionError("El teléfono no puede estar vacío")

    telefono_limpio = telefono.replace(" ", "").replace("-", "")

    # Acepta formatos: +56912345678 o 912345678
    patron = r'^(\+?56)?[9][0-9]{8}$'

    if not re.match(patron, telefono_limpio):
        raise ValidacionError(f"Teléfono inválido '{telefono}'")

    return True
```

Todas las validaciones siguen el mismo patrón: revisar el dato y lanzar una excepción si no cumple las reglas.

---

## 5. Cómo se usan las validaciones en las clases

Las funciones de validación se llaman dentro de los setters de la clase `Cliente`. De esa forma, cada vez que se intenta guardar un dato incorrecto, se lanza automáticamente la excepción:

```python
def set_email(self, email):
    validar_email(email)           # puede lanzar ValidacionError
    self._email = email.lower().strip()
```

Y al crear un cliente se puede manejar el error así:

```python
try:
    cliente = ClienteRegular(
        "Juan Pérez",
        "juan@email.com",
        "912345678",
        "Av. Los Leones 123, Santiago"
    )
    print("Cliente creado correctamente")

except ValidacionError as e:
    print(f"Error de validación: {e}")
```

Si el email no tiene el formato correcto, el programa muestra el mensaje de error en vez de terminar abruptamente.

---

## 6. Sistema de logs

Los logs son registros de lo que va pasando en el sistema, guardados en un archivo de texto. Sirven para revisar después si hubo algún error o qué operaciones se realizaron.

Implementé la clase `SistemaLogs` en `logs.py` usando el módulo `logging` de Python:

```python
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

    def info(self, mensaje):
        self.logger.info(mensaje)
        print(f"[INFO] {mensaje}")

    def error(self, mensaje):
        self.logger.error(mensaje)
        print(f"[ERROR] {mensaje}")

    def warning(self, mensaje):
        self.logger.warning(mensaje)
        print(f"[WARNING] {mensaje}")
```

El sistema guarda los mensajes en `gic_logs.txt` con la fecha y hora. Por ejemplo:

```
2026-02-16 10:30:15 - INFO - Sistema de logs iniciado
2026-02-16 10:30:17 - INFO - Operacion: Crear | Cliente: juan@email.com
2026-02-16 10:30:19 - ERROR - Error en Validar Email: El email 'abc' no tiene formato válido
```

---

## 7. Ejemplo completo de manejo de errores

Este es un ejemplo de cómo funciona todo junto: validaciones, excepciones y logs:

```python
from src import ClienteRegular, GestorClientes
from src.excepciones import ValidacionError, ClienteDuplicadoError
from src.logs import SistemaLogs

logs = SistemaLogs()
gestor = GestorClientes()

# Intentar crear un cliente con datos inválidos
try:
    cliente = ClienteRegular("Juan Pérez", "email_sin_arroba", "912345678",
                              "Av. Los Leones 123, Santiago")
except ValidacionError as e:
    logs.registrar_error("Crear cliente", str(e))
    print(f"No se pudo crear el cliente: {e}")

# Intentar agregar un cliente duplicado
try:
    c1 = ClienteRegular("Juan Pérez", "juan@email.com", "912345678",
                         "Av. Los Leones 123, Santiago")
    gestor.agregar_cliente(c1)
    gestor.agregar_cliente(c1)  # esto lanza ClienteDuplicadoError

except ClienteDuplicadoError as e:
    logs.registrar_error("Agregar cliente", str(e))
    print(f"Cliente duplicado: {e}")
```

---

## 8. Conclusión

El manejo de errores hace que el sistema sea más robusto. En vez de que el programa explote con un error genérico, ahora da mensajes claros sobre qué salió mal. Las excepciones personalizadas ayudan a identificar rápidamente el tipo de problema, y los logs permiten revisar el historial de lo que pasó en el sistema.
