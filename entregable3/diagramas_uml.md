# Diagramas UML - Gestor Inteligente de Clientes

**Proyecto:** GIC Sistema de Gestión  
**Empresa:** SolutionTech  
**Fecha:** Febrero 2026

---

## 1. ¿Qué es un Diagrama de Clases UML?

Un **Diagrama de Clases UML** es una representación visual de las clases que componen un sistema y cómo se relacionan entre sí. Es como un "mapa" del código que muestra:

- **Clases**: Los "moldes" para crear objetos
- **Atributos**: Los datos que guarda cada clase
- **Métodos**: Las acciones que puede hacer cada clase
- **Relaciones**: Cómo las clases se conectan entre sí

### ¿Por qué es importante?

- 📋 **Planificación**: Te ayuda a diseñar antes de programar
- 📖 **Documentación**: Explica el sistema visualmente
- 👥 **Comunicación**: Facilita el trabajo en equipo
- 🔧 **Mantenimiento**: Ayuda a entender el código existente

---

## 2. Estructura del Sistema GIC

Nuestro sistema tiene **4 clases principales** organizadas con HERENCIA:

```
                    Cliente (Clase Base)
                         △
                         │
         ┌───────────────┼───────────────┐
         │               │               │
   ClienteRegular  ClientePremium  ClienteCorporativo
```

### 2.1 Cliente (Clase Base)

Es la clase **PADRE** de la cual heredan todas las demás.

**Atributos:**
```
- _nombre: str          # Nombre del cliente (privado)
- _email: str           # Email del cliente (privado)
- _telefono: str        # Teléfono del cliente (privado)
- _direccion: str       # Dirección del cliente (privado)
```

**Métodos principales:**
```
+ __init__(nombre, email, telefono, direccion)  # Constructor
+ get_nombre(): str                              # Obtener nombre
+ get_email(): str                               # Obtener email
+ get_telefono(): str                            # Obtener teléfono
+ get_direccion(): str                           # Obtener dirección
+ set_nombre(nombre: str)                        # Cambiar nombre
+ set_email(email: str)                          # Cambiar email
+ set_telefono(telefono: str)                    # Cambiar teléfono
+ set_direccion(direccion: str)                  # Cambiar dirección
+ mostrar_informacion()                          # Mostrar datos
+ obtener_resumen(): dict                        # Datos como diccionario
```

**Características:**
- ✅ Sin decoradores `@property` (código simple)
- ✅ Getters y setters como métodos normales
- ✅ Validaciones en cada setter
- ✅ Comentarios línea por línea

---

### 2.2 ClienteRegular (Hereda de Cliente)

Representa un **cliente estándar** sin beneficios especiales.

**Atributos adicionales:**
```
- _fecha_registro: date     # Fecha de registro del cliente
```

**Métodos adicionales:**
```
+ get_fecha_registro(): date        # Obtener fecha
+ set_fecha_registro(fecha: date)   # Cambiar fecha
```

**Métodos sobrescritos (POLIMORFISMO):**
```
+ calcular_descuento(monto: float): float   # Retorna 0 (sin descuento)
+ mostrar_informacion()                      # Muestra info + fecha
```

**Características:**
- 🔄 **HEREDA** todos los atributos y métodos de Cliente
- ➕ **AGREGA** fecha de registro
- 🔁 **SOBRESCRIBE** algunos métodos (polimorfismo)

---

### 2.3 ClientePremium (Hereda de Cliente)

Representa un **cliente premium** con beneficios y descuentos.

**Atributos adicionales:**
```
- _nivel_membresia: str      # "Bronce", "Plata", "Oro"
- _descuento: float          # Porcentaje de descuento (0-100)
- _puntos_acumulados: int    # Puntos por compras
```

**Métodos adicionales:**
```
+ get_nivel_membresia(): str             # Obtener nivel
+ get_descuento(): float                 # Obtener descuento
+ get_puntos_acumulados(): int           # Obtener puntos
+ set_nivel_membresia(nivel: str)        # Cambiar nivel
+ set_descuento(descuento: float)        # Cambiar descuento
+ agregar_puntos(puntos: int)            # Sumar puntos
+ canjear_puntos(puntos: int): bool      # Canjear puntos
```

**Métodos sobrescritos (POLIMORFISMO):**
```
+ calcular_descuento(monto: float): float   # Calcula descuento según %
+ mostrar_informacion()                      # Muestra info + nivel/descuento/puntos
```

**Características:**
- 🔄 **HEREDA** de Cliente
- ➕ **AGREGA** sistema de puntos y descuentos
- 🔁 **SOBRESCRIBE** métodos para comportamiento específico

---

### 2.4 ClienteCorporativo (Hereda de Cliente)

Representa un **cliente corporativo** (empresa) con crédito.

**Atributos adicionales:**
```
- _nombre_empresa: str          # Nombre de la empresa
- _rut_empresa: str             # RUT de la empresa
- _contacto_principal: str      # Persona de contacto
- _limite_credito: float        # Límite de crédito
- _credito_utilizado: float     # Crédito ya usado
```

**Métodos adicionales:**
```
+ get_nombre_empresa(): str                           # Obtener nombre empresa
+ get_rut_empresa(): str                              # Obtener RUT
+ get_contacto_principal(): str                       # Obtener contacto
+ get_limite_credito(): float                         # Obtener límite
+ get_credito_utilizado(): float                      # Obtener usado
+ get_credito_disponible(): float                     # Calcular disponible
+ verificar_credito_disponible(monto: float): bool    # Verificar si hay crédito
+ utilizar_credito(monto: float): bool                # Usar crédito
+ pagar_credito(monto: float)                         # Pagar crédito
```

**Métodos sobrescritos (POLIMORFISMO):**
```
+ calcular_descuento(monto: float): float   # 15% fijo para corporativos
+ mostrar_informacion()                      # Muestra info corporativa
```

**Características:**
- 🔄 **HEREDA** de Cliente
- ➕ **AGREGA** sistema de crédito corporativo
- 🔁 **SOBRESCRIBE** métodos para lógica empresarial

---

## 3. Clases de Soporte

### 3.1 SistemaLogs

Gestiona el registro de eventos del sistema.

**Métodos principales:**
```
+ info(mensaje: str)                    # Log informativo
+ error(mensaje: str)                   # Log de error
+ warning(mensaje: str)                 # Log de advertencia
+ registrar_operacion(op, email, det)   # Registra operación
+ leer_logs(ultimas_lineas: int)        # Lee logs
```

### 3.2 PersistenciaJSON

Guarda y carga datos en formato JSON.

**Métodos principales:**
```
+ guardar_cliente(cliente)              # Guarda 1 cliente
+ guardar_multiples(lista)              # Guarda varios
+ cargar_todos(): list                  # Carga todos
+ cargar_objetos(): list                # Carga como objetos
+ buscar_por_email(email): dict         # Busca cliente
+ eliminar_por_email(email): bool       # Elimina cliente
```

### 3.3 GestorClientes

Administra la colección de clientes.

**Métodos principales:**
```
+ agregar_cliente(cliente)              # Agregar cliente
+ buscar_por_email(email): Cliente      # Buscar por email
+ buscar_por_nombre(nombre): list       # Buscar por nombre
+ listar_todos(): list                  # Listar todos
+ listar_por_tipo(tipo): list           # Listar por tipo
+ eliminar_cliente(email): bool         # Eliminar cliente
+ mostrar_resumen()                     # Mostrar resumen
```

---

## 4. Relaciones entre Clases

### 4.1 HERENCIA

```
Cliente (Padre)
   △
   │ hereda
   │
ClienteRegular (Hijo)
```

**Significado**: ClienteRegular "**ES UN**" Cliente.

**Beneficios**:
- ✅ Reutiliza código de la clase padre
- ✅ Puede agregar nuevos atributos y métodos
- ✅ Puede sobrescribir métodos (polimorfismo)

### 4.2 COMPOSICIÓN

```
GestorClientes ◆────── Cliente
```

**Significado**: GestorClientes "**CONTIENE**" Clientes.

**Beneficios**:
- ✅ Organiza múltiples clientes
- ✅ Centraliza operaciones
- ✅ Facilita gestión del sistema

### 4.3 DEPENDENCIA

```
Cliente ┄┄┄┄> validaciones_simple
```

**Significado**: Cliente "**USA**" las funciones de validación.

**Beneficios**:
- ✅ Reutiliza lógica de validación
- ✅ Mantiene código organizado
- ✅ Facilita mantenimiento

---

## 5. Ejemplo de POLIMORFISMO

El **polimorfismo** permite que diferentes clases respondan al mismo método de formas distintas:

```python
# Mismo método, diferentes resultados según la clase

# Cliente Regular
regular = ClienteRegular(...)
descuento = regular.calcular_descuento(1000)
# Resultado: 0 (sin descuento)

# Cliente Premium
premium = ClientePremium(..., descuento=20.0)
descuento = premium.calcular_descuento(1000)
# Resultado: 200 (20% de 1000)

# Cliente Corporativo
corporativo = ClienteCorporativo(...)
descuento = corporativo.calcular_descuento(1000)
# Resultado: 150 (15% fijo)
```

**Ventaja**: Podemos tratar a todos como "Cliente" pero cada uno se comporta según su tipo.

---

## 6. Diagrama Completo en Texto

```
┌─────────────────────────────────────┐
│          Cliente                     │
├─────────────────────────────────────┤
│ - _nombre: str                       │
│ - _email: str                        │
│ - _telefono: str                     │
│ - _direccion: str                    │
├─────────────────────────────────────┤
│ + get_nombre(): str                  │
│ + set_nombre(nombre: str)            │
│ + mostrar_informacion()              │
│ + obtener_resumen(): dict            │
└─────────────────────────────────────┘
                △
                │ hereda
        ┌───────┼───────┐
        │       │       │
┌───────┴──┐ ┌──┴──────┴──┐ ┌─────────┴────────┐
│Cliente   │ │Cliente      │ │Cliente           │
│Regular   │ │Premium      │ │Corporativo       │
├──────────┤ ├─────────────┤ ├──────────────────┤
│-_fecha   │ │-_nivel      │ │-_nombre_empresa  │
│          │ │-_descuento  │ │-_rut_empresa     │
│          │ │-_puntos     │ │-_limite_credito  │
├──────────┤ ├─────────────┤ ├──────────────────┤
│+calcular │ │+agregar     │ │+utilizar_credito │
│_descuento│ │_puntos()    │ │()                │
│(): 0     │ │+calcular    │ │+calcular         │
│          │ │_descuento() │ │_descuento(): 15% │
└──────────┘ └─────────────┘ └──────────────────┘
```

---

## 7. Cómo Leer el Diagrama

1. **Clases**: Cada rectángulo es una clase
2. **Atributos**: Primera sección (con `-` si son privados)
3. **Métodos**: Segunda sección (con `+` si son públicos)
4. **Herencia**: Flecha con △ apuntando al padre
5. **Tipos de datos**: Después del `:` (str, int, float, bool)

---

## 8. Verificación de Conceptos

### ✅ Entregable 1: POO
- [x] Clase Cliente como base
- [x] Atributos: nombre, email, telefono, direccion
- [x] Métodos de instanciación y actualización

### ✅ Entregable 2: Encapsulación
- [x] Atributos privados (con `_`)
- [x] Getters y setters simples (sin @property)
- [x] Validaciones en setters

### ✅ Entregable 3: Diagramas UML
- [x] Diagrama de clases completo
- [x] Muestra relaciones de herencia
- [x] Documentación clara

### ✅ Entregable 4: Herencia y Polimorfismo
- [x] Tres clases que heredan de Cliente
- [x] Uso de super() en constructores
- [x] Método calcular_descuento() polimórfico

### ✅ Entregable 5: Manejo de Errores
- [x] Excepciones personalizadas
- [x] Validaciones con manejo de errores
- [x] Sistema de logs

---

## 9. Conclusión

Este diagrama UML muestra:

- 📊 **Estructura**: 4 clases principales con herencia
- 🔄 **Polimorfismo**: Mismo método, diferentes comportamientos
- 🔒 **Encapsulación**: Datos protegidos con getters/setters
- 📝 **Simplicidad**: Diseño que facilita el entendimiento del sistema

El sistema está diseñado para ser **educativo y funcional**, cumpliendo todos los requisitos del módulo mientras mantiene el código accesible para estudiantes.

---

**Autor:** Sistema GIC  
**Última actualización:** Febrero 2026
