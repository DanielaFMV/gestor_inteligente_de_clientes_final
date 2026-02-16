# Entregable 3: Diagramas de Clase UML

**Estudiante:** Daniela Muñoz Vásquez 
**Proyecto:** Gestor Inteligente de Clientes (GIC)  
**Empresa:** SolutionTech  
**Fecha:** Febrero 2026

---

## 1. ¿Qué es UML?

**UML (Unified Modeling Language)** es un lenguaje de modelado visual estándar utilizado para especificar, visualizar, construir y documentar los artefactos de un sistema de software. Fue creado para proporcionar una forma común de representar sistemas orientados a objetos.

### 1.1 Propósito de UML

- **Visualización:** Permite ver el sistema de manera gráfica
- **Especificación:** Define la estructura y comportamiento del sistema
- **Construcción:** Guía la implementación del código
- **Documentación:** Sirve como referencia para el equipo de desarrollo

### 1.2 Tipos de Diagramas UML

UML incluye varios tipos de diagramas, clasificados en:

**Diagramas Estructurales:**
- Diagrama de Clases (el que usaremos)
- Diagrama de Objetos
- Diagrama de Componentes
- Diagrama de Despliegue

**Diagramas de Comportamiento:**
- Diagrama de Casos de Uso
- Diagrama de Secuencia
- Diagrama de Actividades
- Diagrama de Estados

## 2. Diagrama de Clases

El **Diagrama de Clases** es el diagrama UML más utilizado y muestra la estructura estática del sistema mediante clases, atributos, métodos y relaciones.

### 2.1 Componentes de una Clase

Una clase en UML se representa con un rectángulo dividido en tres secciones:

```
┌─────────────────────┐
│   NombreClase       │  ← Nombre de la clase
├─────────────────────┤
│ - atributo1: tipo   │  ← Atributos
│ - atributo2: tipo   │
├─────────────────────┤
│ + metodo1(): tipo   │  ← Métodos
│ + metodo2(): tipo   │
└─────────────────────┘
```

### 2.2 Visibilidad de Atributos y Métodos

Los símbolos indican el nivel de acceso:

- `+` **Público:** Accesible desde cualquier parte
- `-` **Privado:** Solo accesible dentro de la clase
- `#` **Protegido:** Accesible en la clase y sus subclases
- `~` **Paquete:** Accesible dentro del mismo paquete

### 2.3 Tipos de Datos

Los atributos y métodos especifican su tipo:

```
- nombre: str
- edad: int
- activo: bool
+ calcular_descuento(): float
```

## 3. Relaciones entre Clases

Las relaciones definen cómo las clases interactúan entre sí.

### 3.1 Herencia (Generalización)

Representa una relación "es un" donde una clase hija hereda de una clase padre.

**Notación:** Flecha con punta triangular blanca apuntando al padre

```
    Cliente
       △
       │
   ┌───┴───┐
   │       │
ClienteReg ClientePrem
```

**Características:**
- La subclase hereda todos los atributos y métodos del padre
- Permite especialización y reutilización de código
- La flecha apunta de la clase hija hacia la clase padre

**Ejemplo en el GIC:**
- `ClienteRegular` es un `Cliente`
- `ClientePremium` es un `Cliente`
- `ClienteCorporativo` es un `Cliente`

### 3.2 Composición

Representa una relación "contiene" donde una clase es parte fundamental de otra. Si el todo se destruye, las partes también.

**Notación:** Rombo negro en el lado del "todo"

```
Pedido ◆─────── LineaPedido
```

**Características:**
- Relación fuerte de pertenencia
- Las partes no existen sin el todo
- Rombo negro indica la propiedad

**Ejemplo:**
- Un `Pedido` tiene `LineaPedido`
- Si se elimina el pedido, las líneas también se eliminan

### 3.3 Agregación

Representa una relación "tiene un" donde una clase contiene a otra, pero pueden existir independientemente.

**Notación:** Rombo blanco en el lado del contenedor

```
Empresa ◇─────── Empleado
```

**Características:**
- Relación débil de pertenencia
- Las partes pueden existir sin el todo
- Rombo blanco indica la asociación

**Ejemplo:**
- Una `Empresa` tiene `Empleados`
- Si se cierra la empresa, los empleados siguen existiendo

### 3.4 Asociación

Representa una relación general entre clases.

**Notación:** Línea simple

```
Cliente ─────── Pedido
```

**Multiplicidad:**
Se indica cuántos objetos participan en la relación:

- `1` : Exactamente uno
- `0..1` : Cero o uno
- `*` : Cero o más
- `1..*` : Uno o más
- `n..m` : Entre n y m

**Ejemplo:**
```
Cliente 1 ─────── 0..* Pedido
```
Un cliente tiene cero o más pedidos.

### 3.5 Dependencia

Indica que una clase usa a otra temporalmente.

**Notación:** Flecha punteada

```
Cliente ┄┄┄> ValidacionEmail
```

**Características:**
- Relación temporal
- Una clase depende de otra para funcionar
- Cambios en una clase pueden afectar a la otra

## 4. Diagrama del Sistema GIC

### 4.1 Estructura de Clases

El sistema GIC tiene la siguiente jerarquía:

**Clase Base:**
- `Cliente`: Clase principal con atributos y métodos comunes

**Clases Derivadas:**
- `ClienteRegular`: Cliente estándar sin beneficios especiales
- `ClientePremium`: Cliente con descuentos y beneficios
- `ClienteCorporativo`: Cliente empresarial con condiciones especiales

**Clases de Soporte:**
- `Validaciones`: Funciones para validar datos
- `GestorClientes`: Gestiona la colección de clientes

### 4.2 Atributos por Clase

**Cliente (clase base):**
```
- _nombre: str
- _email: str
- _telefono: str
- _direccion: str
```

**ClienteRegular:**
```
- fecha_registro: date
```

**ClientePremium:**
```
- nivel_membresia: str
- descuento: float
- puntos_acumulados: int
```

**ClienteCorporativo:**
```
- nombre_empresa: str
- rut_empresa: str
- contacto_principal: str
- limite_credito: float
```

### 4.3 Métodos por Clase

**Cliente:**
```
+ mostrar_informacion(): void
+ actualizar_email(email: str): void
+ actualizar_telefono(telefono: str): void
+ actualizar_direccion(direccion: str): void
+ obtener_resumen(): dict
```

**ClientePremium:**
```
+ calcular_descuento(monto: float): float
+ agregar_puntos(puntos: int): void
+ canjear_puntos(puntos: int): bool
```

**ClienteCorporativo:**
```
+ verificar_credito_disponible(monto: float): bool
+ actualizar_limite_credito(nuevo_limite: float): void
```

### 4.4 Relaciones en el GIC

1. **Herencia:**
   - `ClienteRegular` hereda de `Cliente`
   - `ClientePremium` hereda de `Cliente`
   - `ClienteCorporativo` hereda de `Cliente`

2. **Composición:**
   - `GestorClientes` contiene una lista de `Cliente`
   - Si el gestor se destruye, la colección también

3. **Dependencia:**
   - Todas las clases de cliente dependen de `Validaciones`
   - `GestorClientes` depende de las clases de cliente

## 5. Beneficios del Diagrama de Clases

### 5.1 Para el Desarrollo

- **Planificación:** Permite diseñar antes de programar
- **Comunicación:** Facilita el entendimiento entre el equipo
- **Documentación:** Sirve como referencia permanente

### 5.2 Para el Mantenimiento

- **Claridad:** Muestra la estructura completa del sistema
- **Modificaciones:** Ayuda a identificar impactos de cambios
- **Escalabilidad:** Facilita agregar nuevas funcionalidades

### 5.3 Para Nuevos Desarrolladores

- **Comprensión rápida:** Entienden el sistema visualmente
- **Onboarding:** Reducen el tiempo de adaptación
- **Referencia:** Consultan el diagrama cuando tienen dudas

## 6. Buenas Prácticas

### 6.1 Al Diseñar Diagramas

1. **Simplicidad:** No incluir todo en un solo diagrama
2. **Claridad:** Nombres descriptivos y concisos
3. **Consistencia:** Usar convenciones estándar
4. **Actualización:** Mantener sincronizado con el código

### 6.2 Al Implementar

1. **Seguir el diseño:** El código debe reflejar el diagrama
2. **Documentar cambios:** Actualizar el diagrama cuando se modifica el código
3. **Validar relaciones:** Verificar que las relaciones sean correctas

## 7. Herramientas para UML

### 7.1 Herramientas de Diagramación

- **PlantUML:** Basada en texto, integración con código, generación de imágenes
- **Draw.io (diagrams.net):** Gratuita, basada en web, interfaz visual
- **Lucidchart:** Colaborativa, plantillas predefinidas
- **StarUML:** Profesional, muchas funcionalidades

### 7.2 Formato del Proyecto

Para este proyecto utilizamos **PlantUML** porque:
- Sintaxis estándar de UML
- Puede versionarse como código fuente
- Genera imágenes de alta calidad (PNG, SVG, PDF)
- Ampliamente usado en la industria
- Integración con múltiples editores y IDEs

## 8. Lectura del Diagrama GIC

Para entender el diagrama del GIC:

1. **Identificar la jerarquía:** Cliente es la clase base
2. **Observar herencias:** Las tres subclases heredan de Cliente
3. **Revisar atributos:** Cada clase tiene sus propios atributos
4. **Analizar métodos:** Métodos comunes en la base, específicos en subclases
5. **Entender relaciones:** Composición con GestorClientes, dependencia con Validaciones

## 9. Conclusión

El Diagrama de Clases UML es una herramienta fundamental para diseñar y documentar sistemas orientados a objetos. Para el proyecto GIC, el diagrama muestra claramente la estructura de herencia que permite reutilizar código mientras se especializan comportamientos para diferentes tipos de clientes.

Este diseño facilita la implementación del código, el mantenimiento del sistema y la comprensión por parte de todo el equipo de desarrollo.

---

## 10. Referencias

- OMG UML Specification: https://www.omg.org/spec/UML/
- Martin Fowler - UML Distilled
- PlantUML Documentation: https://plantuml.com/
- Diagrama PlantUML del GIC: `diagrama_clases_gic.puml`
