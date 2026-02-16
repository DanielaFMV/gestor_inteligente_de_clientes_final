# Entregable 4: Herencia y Polimorfismo

**Estudiante:** [Tu Nombre]  
**Proyecto:** Gestor Inteligente de Clientes (GIC)  
**Empresa:** SolutionTech  
**Fecha:** Febrero 2026

---

## 1. Introducción

Este entregable implementa los conceptos de **Herencia** y **Polimorfismo** en el sistema GIC, creando una jerarquía de clases de clientes que heredan de una clase base y demuestran comportamientos polimórficos.

## 2. Herencia en Python

### 2.1 ¿Qué es la Herencia?

La herencia es un mecanismo de la POO que permite crear nuevas clases basadas en clases existentes. La clase derivada (hija) hereda atributos y métodos de la clase base (padre), pudiendo además agregar nuevos atributos y métodos o sobrescribir los existentes.

**Ventajas:**
- **Reutilización de código:** Evita duplicación
- **Jerarquías lógicas:** Organiza clases relacionadas
- **Extensibilidad:** Facilita agregar nuevas funcionalidades
- **Mantenibilidad:** Cambios en la clase base se propagan

### 2.2 Sintaxis en Python

```python
class ClaseBase:
    def __init__(self, atributo1):
        self.atributo1 = atributo1
    
    def metodo_base(self):
        return "Método de la clase base"

class ClaseDerivada(ClaseBase):
    def __init__(self, atributo1, atributo2):
        super().__init__(atributo1)  # Llama al constructor del padre
        self.atributo2 = atributo2
    
    def metodo_derivado(self):
        return "Método de la clase derivada"
```

### 2.3 La función super()

La función `super()` permite acceder a métodos y atributos de la clase padre:

```python
class Cliente:
    def __init__(self, nombre, email):
        self._nombre = nombre
        self._email = email

class ClientePremium(Cliente):
    def __init__(self, nombre, email, descuento):
        super().__init__(nombre, email)  # Llama al __init__ del padre
        self._descuento = descuento
```

**Usos comunes de super():**
- Llamar al constructor de la clase padre
- Extender métodos del padre sin duplicar código
- Acceder a versiones sobrescritas de métodos

## 3. Jerarquía de Clases en GIC

### 3.1 Diseño de la Jerarquía

En el proyecto GIC, implementamos la siguiente jerarquía:

```
                    Cliente (Clase Base)
                         |
         +---------------+---------------+
         |               |               |
   ClienteRegular  ClientePremium  ClienteCorporativo
```

### 3.2 Clase Base: Cliente

La clase `Cliente` define los atributos y métodos comunes a todos los tipos de clientes:

**Atributos:**
- `_nombre`: Nombre del cliente
- `_email`: Correo electrónico
- `_telefono`: Número de teléfono
- `_direccion`: Dirección física

**Métodos:**
- `get_nombre()`, `set_nombre()`: Acceso al nombre
- `get_email()`, `set_email()`: Acceso al email
- `mostrar_informacion()`: Mostrar datos del cliente
- `obtener_resumen()`: Retornar datos como diccionario

### 3.3 Clase Derivada: ClienteRegular

```python
class ClienteRegular(Cliente):
    def __init__(self, nombre, email, telefono, direccion, fecha_registro=None):
        super().__init__(nombre, email, telefono, direccion)
        self._fecha_registro = fecha_registro or date.today()
    
    def get_fecha_registro(self):
        return self._fecha_registro
```

**Características:**
- Hereda todos los atributos y métodos de `Cliente`
- Agrega el atributo `_fecha_registro`
- No tiene descuentos ni beneficios especiales

### 3.4 Clase Derivada: ClientePremium

```python
class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion, 
                 nivel_membresia="Bronce", descuento=10.0):
        super().__init__(nombre, email, telefono, direccion)
        self._nivel_membresia = nivel_membresia
        self._descuento = descuento
        self._puntos_acumulados = 0
    
    def agregar_puntos(self, puntos):
        self._puntos_acumulados += puntos
    
    def canjear_puntos(self, puntos):
        if self._puntos_acumulados >= puntos:
            self._puntos_acumulados -= puntos
            return True
        return False
```

**Características:**
- Hereda de `Cliente`
- Agrega sistema de puntos
- Tiene niveles de membresía (Bronce, Plata, Oro)
- Ofrece descuentos variables

### 3.5 Clase Derivada: ClienteCorporativo

```python
class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, telefono, direccion,
                 nombre_empresa, rut_empresa, contacto_principal,
                 limite_credito=100000.0):
        super().__init__(nombre, email, telefono, direccion)
        self._nombre_empresa = nombre_empresa
        self._rut_empresa = rut_empresa
        self._contacto_principal = contacto_principal
        self._limite_credito = limite_credito
        self._credito_utilizado = 0.0
    
    def utilizar_credito(self, monto):
        disponible = self._limite_credito - self._credito_utilizado
        if monto <= disponible:
            self._credito_utilizado += monto
            return True
        return False
    
    def pagar_credito(self, monto):
        self._credito_utilizado = max(0, self._credito_utilizado - monto)
```

**Características:**
- Hereda de `Cliente`
- Representa empresas, no personas individuales
- Maneja crédito corporativo
- Tiene descuento fijo del 15%

## 4. Polimorfismo en Python

### 4.1 ¿Qué es el Polimorfismo?

El polimorfismo permite que objetos de diferentes clases respondan al mismo mensaje (método) de formas distintas. Es la capacidad de un método de comportarse de manera diferente según el objeto que lo invoque.

**Tipos de polimorfismo:**
- **Polimorfismo de sobrecarga:** Mismo método, diferentes parámetros
- **Polimorfismo de sobrescritura:** Mismo método, diferente implementación en clases derivadas

### 4.2 Sobrescritura de Métodos

En Python, las clases derivadas pueden sobrescribir métodos de la clase base:

```python
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau miau"
```

### 4.3 Polimorfismo en GIC: calcular_descuento()

El método `calcular_descuento()` es polimórfico en nuestro sistema:

```python
# En Cliente (clase base)
class Cliente:
    def calcular_descuento(self, monto):
        return 0.0  # Sin descuento por defecto

# En ClienteRegular
class ClienteRegular(Cliente):
    def calcular_descuento(self, monto):
        return 0.0  # Clientes regulares no tienen descuento

# En ClientePremium
class ClientePremium(Cliente):
    def calcular_descuento(self, monto):
        return monto * (self._descuento / 100)  # Descuento variable

# En ClienteCorporativo
class ClienteCorporativo(Cliente):
    def calcular_descuento(self, monto):
        return monto * 0.15  # 15% de descuento fijo
```

**Uso polimórfico:**

```python
clientes = [
    ClienteRegular("Juan", "juan@email.com", "123", "Dir1"),
    ClientePremium("María", "maria@email.com", "456", "Dir2", "Oro", 20.0),
    ClienteCorporativo("Pedro", "pedro@corp.com", "789", "Dir3",
                       "TechCorp", "12345", "Pedro", 500000)
]

monto_compra = 10000

for cliente in clientes:
    # El mismo método, diferentes resultados según el tipo
    descuento = cliente.calcular_descuento(monto_compra)
    total = monto_compra - descuento
    print(f"{type(cliente).__name__}: Descuento ${descuento}, Total ${total}")
```

**Salida:**
```
ClienteRegular: Descuento $0.0, Total $10000.0
ClientePremium: Descuento $2000.0, Total $8000.0
ClienteCorporativo: Descuento $1500.0, Total $8500.0
```

### 4.4 Sobrescritura de mostrar_informacion()

Otro ejemplo de polimorfismo es el método `mostrar_informacion()`:

```python
# En Cliente
def mostrar_informacion(self):
    print("INFORMACIÓN DEL CLIENTE")
    print(f"Nombre: {self._nombre}")
    print(f"Email: {self._email}")

# En ClientePremium (sobrescrito)
def mostrar_informacion(self):
    print("INFORMACIÓN DEL CLIENTE PREMIUM")
    print(f"Nombre: {self._nombre}")
    print(f"Email: {self._email}")
    print(f"Nivel: {self._nivel_membresia}")
    print(f"Descuento: {self._descuento}%")
    print(f"Puntos: {self._puntos_acumulados}")

# En ClienteCorporativo (sobrescrito)
def mostrar_informacion(self):
    print("INFORMACIÓN DEL CLIENTE CORPORATIVO")
    print(f"Empresa: {self._nombre_empresa}")
    print(f"RUT: {self._rut_empresa}")
    print(f"Contacto: {self._contacto_principal}")
    print(f"Crédito disponible: ${self._limite_credito - self._credito_utilizado}")
```

## 5. Ventajas de Herencia y Polimorfismo en GIC

### 5.1 Reutilización de Código

```python
# Sin herencia (código duplicado)
class ClienteRegular:
    def __init__(self, nombre, email, telefono, direccion):
        self._nombre = nombre
        self._email = email
        # ... métodos get/set duplicados

class ClientePremium:
    def __init__(self, nombre, email, telefono, direccion, descuento):
        self._nombre = nombre  # DUPLICADO
        self._email = email    # DUPLICADO
        # ... métodos get/set duplicados

# Con herencia (código reutilizado)
class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self._nombre = nombre
        self._email = email
        # ... métodos get/set UNA SOLA VEZ

class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion, descuento):
        super().__init__(nombre, email, telefono, direccion)  # REUTILIZA
        self._descuento = descuento
```

### 5.2 Extensibilidad

Agregar nuevos tipos de clientes es sencillo:

```python
class ClienteVIP(ClientePremium):
    def __init__(self, nombre, email, telefono, direccion):
        super().__init__(nombre, email, telefono, direccion, "Platino", 30.0)
        self._asistente_personal = None
    
    def asignar_asistente(self, nombre_asistente):
        self._asistente_personal = nombre_asistente
```

### 5.3 Mantenibilidad

Cambios en la clase base se propagan automáticamente:

```python
# Si agregamos un método en Cliente
class Cliente:
    def enviar_notificacion(self, mensaje):
        print(f"Enviando email a {self._email}: {mensaje}")

# TODAS las clases derivadas lo heredan automáticamente
cliente_regular.enviar_notificacion("Bienvenido")
cliente_premium.enviar_notificacion("Nuevos beneficios")
cliente_corporativo.enviar_notificacion("Reporte mensual")
```

### 5.4 Polimorfismo para Código Genérico

```python
def procesar_compra(cliente, monto):
    """Función que funciona con cualquier tipo de cliente"""
    descuento = cliente.calcular_descuento(monto)
    total = monto - descuento
    
    print(f"Cliente: {cliente.get_nombre()}")
    print(f"Monto original: ${monto}")
    print(f"Descuento: ${descuento}")
    print(f"Total a pagar: ${total}")
    
    return total

# Funciona con cualquier tipo de cliente
procesar_compra(cliente_regular, 5000)
procesar_compra(cliente_premium, 5000)
procesar_compra(cliente_corporativo, 5000)
```

## 6. Verificación de Tipos

Python proporciona funciones para verificar tipos y herencia:

### 6.1 isinstance()

Verifica si un objeto es instancia de una clase o sus derivadas:

```python
cliente_premium = ClientePremium("Ana", "ana@email.com", "123", "Dir")

print(isinstance(cliente_premium, ClientePremium))  # True
print(isinstance(cliente_premium, Cliente))         # True (hereda)
print(isinstance(cliente_premium, ClienteRegular))  # False
```

### 6.2 issubclass()

Verifica si una clase es subclase de otra:

```python
print(issubclass(ClientePremium, Cliente))      # True
print(issubclass(ClienteRegular, Cliente))      # True
print(issubclass(Cliente, ClientePremium))      # False
```

### 6.3 type()

Retorna el tipo exacto del objeto:

```python
cliente = ClientePremium("Juan", "juan@email.com", "123", "Dir")

print(type(cliente))              # <class 'ClientePremium'>
print(type(cliente).__name__)     # 'ClientePremium'
```

## 7. Buenas Prácticas

### 7.1 Uso de super()

✅ **Correcto:**
```python
class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion, descuento):
        super().__init__(nombre, email, telefono, direccion)
        self._descuento = descuento
```

❌ **Incorrecto:**
```python
class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion, descuento):
        Cliente.__init__(self, nombre, email, telefono, direccion)  # Evitar
        self._descuento = descuento
```

### 7.2 Llamar a Métodos del Padre

```python
class ClientePremium(Cliente):
    def mostrar_informacion(self):
        super().mostrar_informacion()  # Llama al método del padre
        print(f"Descuento: {self._descuento}%")  # Agrega información adicional
```

### 7.3 Diseño de Jerarquías

- Mantener jerarquías simples (evitar herencia múltiple cuando sea posible)
- La clase base debe contener solo lo común a todas las derivadas
- Cada clase derivada debe agregar características específicas
- Evitar jerarquías muy profundas (más de 3-4 niveles)

## 8. Conclusión

La implementación de **Herencia** y **Polimorfismo** en el proyecto GIC proporciona:

✅ **Código reutilizable:** La clase `Cliente` base evita duplicación  
✅ **Extensibilidad:** Fácil agregar nuevos tipos de clientes  
✅ **Mantenibilidad:** Cambios centralizados en la clase base  
✅ **Flexibilidad:** Polimorfismo permite código genérico  
✅ **Organización:** Jerarquía clara y lógica de clases  

Estos principios son fundamentales para construir sistemas orientados a objetos robustos y escalables.

---

## Referencias

- Python Documentation: https://docs.python.org/3/tutorial/classes.html
- Real Python - Inheritance and Composition: https://realpython.com/inheritance-composition-python/
- Python OOP Tutorial: https://www.programiz.com/python-programming/object-oriented-programming
