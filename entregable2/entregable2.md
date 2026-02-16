# Entregable 2: POO en Python - Encapsulación y Validaciones

**Estudiante:** [Tu Nombre]  
**Proyecto:** Gestor Inteligente de Clientes (GIC)  
**Empresa:** SolutionTech  
**Fecha:** Febrero 2026

---

## 1. Introducción

En este entregable se implementa la clase Cliente utilizando los principios avanzados de la Programación Orientada a Objetos en Python, específicamente:

- **Encapsulación:** Protección de datos mediante atributos privados
- **Validaciones:** Verificación de datos para garantizar integridad
- **Métodos especiales:** Implementación de `__str__`, `__eq__`, `__repr__`, `__hash__`

## 2. Encapsulación en Python

### 2.1 ¿Qué es la Encapsulación?

La encapsulación es el principio de POO que consiste en ocultar los detalles internos de implementación de una clase y exponer solo lo necesario mediante una interfaz pública. Esto protege los datos de accesos no autorizados o modificaciones incorrectas.

### 2.2 Atributos Privados

En Python, los atributos privados se indican con un guión bajo al inicio del nombre:

```python
class Cliente:
    def __init__(self, nombre, email):
        self._nombre = nombre    # Atributo privado
        self._email = email      # Atributo privado
```

**Convención:**
- Un guión bajo (`_atributo`): Indica que es privado por convención
- Dos guiones bajos (`__atributo`): Python aplica name mangling para mayor protección

### 2.3 Propiedades (Properties)

Las propiedades permiten acceder a atributos privados de forma controlada:

```python
@property
def nombre(self):
    """Obtiene el nombre del cliente."""
    return self._nombre

@nombre.setter
def nombre(self, valor):
    """Establece el nombre con validación."""
    if len(valor) < 3:
        raise ValueError("Nombre muy corto")
    self._nombre = valor
```

**Ventajas de las propiedades:**
- Control total sobre el acceso a los datos
- Validación automática al asignar valores
- Sintaxis limpia (como si fueran atributos normales)
- Facilitan el mantenimiento del código

## 3. Validaciones de Datos

### 3.1 Importancia de las Validaciones

Las validaciones garantizan que los datos almacenados en el sistema cumplan con requisitos específicos:

- **Integridad:** Los datos son correctos y consistentes
- **Seguridad:** Previene inyección de datos maliciosos
- **Calidad:** Mantiene estándares de formato
- **Experiencia de usuario:** Retroalimentación inmediata sobre errores

### 3.2 Validación de Email

El email debe cumplir con el formato estándar de correo electrónico:

```python
import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        raise ValidacionError(f"Email inválido: {email}")
    return True
```

**Características validadas:**
- Presencia de @ único
- Dominio válido
- Extensión de dominio (.com, .cl, etc.)

### 3.3 Validación de Teléfono

Para el contexto chileno, se validan números móviles:

```python
def validar_telefono(telefono):
    # Acepta: +56912345678, 912345678, +56 9 1234 5678
    telefono_limpio = telefono.replace(" ", "").replace("-", "")
    patron = r'^(\+?56)?[9][0-9]{8}$'
    
    if not re.match(patron, telefono_limpio):
        raise ValidacionError(f"Teléfono inválido: {telefono}")
    return True
```

**Características validadas:**
- Código de país opcional (+56)
- Comienza con 9 (móviles en Chile)
- 9 dígitos en total después del código de país

### 3.4 Validación de Dirección

La dirección debe tener información suficiente:

```python
def validar_direccion(direccion):
    if len(direccion.strip()) < 10:
        raise ValidacionError("Dirección debe tener al menos 10 caracteres")
    return True
```

**Características validadas:**
- No está vacía
- Longitud mínima de 10 caracteres
- Es un texto válido

### 3.5 Excepciones Personalizadas

Se crea una excepción específica para errores de validación:

```python
class ValidacionError(Exception):
    """Excepción para errores de validación de datos."""
    pass
```

**Ventajas:**
- Permite capturar específicamente errores de validación
- Diferencia de otros tipos de errores
- Mejora la legibilidad del código

## 4. Métodos Especiales (Dunder Methods)

Los métodos especiales en Python permiten que las clases interactúen con operadores y funciones integradas.

### 4.1 Método `__str__`

Proporciona una representación en texto legible para humanos:

```python
def __str__(self):
    return f"Cliente: {self.nombre} | Email: {self.email}"
```

**Uso:**
```python
cliente = Cliente("Juan Pérez", "juan@email.com", "+56912345678", "Av. Principal 123")
print(cliente)  # Cliente: Juan Pérez | Email: juan@email.com
```

### 4.2 Método `__repr__`

Proporciona una representación técnica, idealmente que permita recrear el objeto:

```python
def __repr__(self):
    return f"Cliente(nombre='{self.nombre}', email='{self.email}', ...)"
```

**Diferencia con `__str__`:**
- `__str__`: Para usuarios finales (legible)
- `__repr__`: Para desarrolladores (técnico)

### 4.3 Método `__eq__`

Define cómo se comparan dos objetos de la clase:

```python
def __eq__(self, otro):
    if not isinstance(otro, Cliente):
        return False
    return self.email == otro.email
```

**Uso:**
```python
cliente1 = Cliente("Juan", "juan@email.com", "+56912345678", "Dir 1")
cliente2 = Cliente("Juan P.", "juan@email.com", "+56987654321", "Dir 2")

print(cliente1 == cliente2)  # True (mismo email)
```

**Criterio de igualdad:** Dos clientes son iguales si tienen el mismo email.

### 4.4 Método `__hash__`

Permite usar objetos en sets y como claves de diccionarios:

```python
def __hash__(self):
    return hash(self.email)
```

**Uso:**
```python
clientes = {cliente1, cliente2, cliente3}  # Set de clientes únicos
```

**Nota importante:** Si se implementa `__eq__`, también se debe implementar `__hash__` para mantener la consistencia.

## 5. Beneficios de la Implementación

### 5.1 Protección de Datos

La encapsulación previene:
- Asignación de valores inválidos
- Acceso no autorizado a datos sensibles
- Modificaciones que rompan la lógica del negocio

### 5.2 Mantenimiento

Las validaciones centralizadas facilitan:
- Cambios en reglas de negocio
- Actualización de formatos
- Corrección de errores en un solo lugar

### 5.3 Reutilización

El módulo de validaciones puede:
- Usarse en otras clases del sistema
- Exportarse a otros proyectos
- Extenderse con nuevas validaciones

### 5.4 Claridad

Los métodos especiales permiten:
- Código más intuitivo y legible
- Interacción natural con el lenguaje
- Mejor experiencia para otros desarrolladores

## 6. Patrones de Uso

### 6.1 Creación con Validación Automática

```python
try:
    cliente = Cliente(
        nombre="Ana Torres",
        email="ana.torres@email.com",
        telefono="+56912345678",
        direccion="Av. Providencia 1234, Santiago"
    )
    print("Cliente creado exitosamente")
except ValidacionError as e:
    print(f"Error al crear cliente: {e}")
```

### 6.2 Actualización Segura

```python
try:
    cliente.email = "nuevo.email@empresa.cl"
    print("Email actualizado")
except ValidacionError as e:
    print(f"Error: {e}")
    # El email original se mantiene intacto
```

### 6.3 Comparación de Clientes

```python
if cliente1 == cliente2:
    print("Los clientes tienen el mismo email")
else:
    print("Son clientes diferentes")
```

## 7. Conclusión

La implementación de encapsulación y validaciones en la clase Cliente proporciona una base sólida para el Gestor Inteligente de Clientes. Este enfoque garantiza la integridad de los datos, facilita el mantenimiento y establece un estándar de calidad para el resto del sistema.

Los métodos especiales permiten que los objetos Cliente se comporten de manera natural dentro del lenguaje Python, mejorando la experiencia de desarrollo y la legibilidad del código.

---

## 8. Archivos del Entregable

- `validaciones.py`: Módulo con funciones de validación
- `cliente_encapsulado.py`: Clase Cliente con encapsulación
- `ejemplo_encapsulacion.py`: Ejemplos de uso completos
- `entregable2_documento.md`: Este documento explicativo