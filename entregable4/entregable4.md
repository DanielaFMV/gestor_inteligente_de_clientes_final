# Entregable 4: Herencia y Polimorfismo

**Proyecto:** Gestor Inteligente de Clientes (GIC)
**Empresa:** SolutionTech
**Fecha:** Febrero 2026

---

## 1. Introducción

En este entregable implementé herencia y polimorfismo en el sistema GIC. La idea es crear tipos de clientes distintos que compartan características en común, pero que también tengan sus propias características específicas. Para eso usé la clase `Cliente` como base y creé tres subclases que heredan de ella.

---

## 2. ¿Qué es la herencia?

La herencia permite crear una clase nueva basada en otra que ya existe. La clase nueva (hija) hereda todos los atributos y métodos de la clase original (padre), y además puede agregar los suyos propios o modificar los que hereda.

Por ejemplo, en la vida real: un `ClientePremium` sigue siendo un `Cliente`, pero con beneficios adicionales. Esa relación "es un tipo de" es exactamente lo que modela la herencia.

En Python, para indicar que una clase hereda de otra se escribe el nombre de la clase padre entre paréntesis:

```python
class ClienteRegular(Cliente):  # ClienteRegular hereda de Cliente
    pass
```

---

## 3. La función super()

Cuando una clase hija tiene su propio `__init__`, necesita llamar al constructor del padre para que los atributos del padre también se inicialicen. Para eso se usa `super()`.

```python
class ClienteRegular(Cliente):
    def __init__(self, nombre, email, telefono, direccion, fecha_registro=None):
        super().__init__(nombre, email, telefono, direccion)  # llama al __init__ de Cliente
        self._fecha_registro = fecha_registro
```

Sin el `super().__init__()`, el cliente no tendría nombre, email ni ninguno de los atributos de la clase padre.

---

## 4. Jerarquía de clases en el proyecto

En el GIC hay una clase base y tres clases que heredan de ella:

```
            Cliente (clase base)
                 |
    +------------+------------+
    |            |            |
ClienteRegular  ClientePremium  ClienteCorporativo
```

### 4.1 Clase base: Cliente

Tiene los atributos y métodos comunes a todos los tipos de clientes: nombre, email, teléfono y dirección, con sus getters, setters y validaciones.

### 4.2 ClienteRegular

Hereda todo de `Cliente` y agrega solo la fecha de registro. No tiene descuentos ni beneficios.

```python
class ClienteRegular(Cliente):
    def __init__(self, nombre, email, telefono, direccion, fecha_registro=None):
        super().__init__(nombre, email, telefono, direccion)
        if fecha_registro is None:
            self._fecha_registro = date.today()
        else:
            self._fecha_registro = fecha_registro
```

### 4.3 ClientePremium

Hereda de `Cliente` y agrega nivel de membresía, descuento y puntos acumulados. Tiene métodos para agregar y canjear puntos.

```python
class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion, nivel_membresia="Bronce", descuento=10.0):
        super().__init__(nombre, email, telefono, direccion)
        self._nivel_membresia = nivel_membresia
        self._descuento = descuento
        self._puntos_acumulados = 0
```

### 4.4 ClienteCorporativo

Hereda de `Cliente` y agrega datos de empresa (nombre, RUT, contacto) y un sistema de crédito corporativo.

```python
class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, telefono, direccion,
                 nombre_empresa, rut_empresa, contacto_principal, limite_credito=100000.0):
        super().__init__(nombre, email, telefono, direccion)
        self._nombre_empresa = nombre_empresa
        self._rut_empresa = rut_empresa
        self._contacto_principal = contacto_principal
        self._limite_credito = limite_credito
        self._credito_utilizado = 0.0
```

---

## 5. ¿Qué es el polimorfismo?

El polimorfismo significa que distintos tipos de objetos pueden responder al mismo método, pero cada uno lo hace de forma diferente. Es decir, el mismo nombre de método tiene comportamientos distintos según la clase.

En el GIC usé polimorfismo con el método `calcular_descuento()`. Todas las clases de clientes tienen ese método, pero cada una lo implementa distinto:

```python
# En ClienteRegular: no hay descuento
def calcular_descuento(self, monto):
    return 0.0

# En ClientePremium: descuento según el porcentaje del cliente
def calcular_descuento(self, monto):
    return monto * (self._descuento / 100)

# En ClienteCorporativo: descuento fijo del 15%
def calcular_descuento(self, monto):
    return monto * 0.15
```

Lo interesante es que puedo hacer esto:

```python
clientes = [
    ClienteRegular("Juan Pérez", "juan@email.com", "912345678", "Av. Los Leones 123, Santiago"),
    ClientePremium("María López", "maria@email.com", "987654321", "Calle Principal 456, Providencia", "Oro", 20.0),
    ClienteCorporativo("Pedro Soto", "pedro@empresa.com", "912233445", "Av. Apoquindo 789, Las Condes",
                       "Tech Solutions SpA", "76.123.456-7", "Pedro Soto", 500000.0)
]

monto = 10000

for cliente in clientes:
    descuento = cliente.calcular_descuento(monto)
    print(f"{type(cliente).__name__}: descuento = ${descuento}")
```

**Resultado:**
```
ClienteRegular: descuento = $0
ClientePremium: descuento = $2000
ClienteCorporativo: descuento = $1500
```

Aunque todos los clientes de la lista son distintos, el código los trata igual. Eso es polimorfismo.

---

## 6. Sobrescritura de métodos

Otra forma de polimorfismo es sobrescribir un método del padre para que haga algo diferente en la clase hija. Por ejemplo, `mostrar_informacion()` está definido en `Cliente`, pero cada subclase lo sobrescribe para mostrar también sus datos propios:

```python
# En ClientePremium
def mostrar_informacion(self):
    print("--- Cliente Premium ---")
    print(f"Nombre:    {self.get_nombre()}")
    print(f"Email:     {self.get_email()}")
    print(f"Nivel:     {self._nivel_membresia}")
    print(f"Descuento: {self._descuento}%")
    print(f"Puntos:    {self._puntos_acumulados}")
```

---

## 7. Ventaja principal de usar herencia

Sin herencia tendría que repetir el mismo código de nombre, email, teléfono y dirección en las tres clases. Con herencia lo escribo una sola vez en `Cliente` y las subclases lo heredan automáticamente. Si mañana necesito cambiar cómo se valida el email, lo cambio en un solo lugar y afecta a todas las clases.

---

## 8. Conclusión

Implementar herencia y polimorfismo en el GIC me ayudó a organizar mejor el código. La clase `Cliente` tiene todo lo común, y cada subclase agrega solo lo que la diferencia de las demás. El polimorfismo me permite escribir código que funciona con cualquier tipo de cliente sin necesidad de usar if/else para saber de qué tipo es.
