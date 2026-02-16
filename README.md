# Gestor Inteligente de Clientes (GIC)

**Proyecto:** Sistema de Gestión de Clientes  
**Empresa:** SolutionTech  
**Fecha:** Febrero 2026

---

## 📋 Descripción

Sistema de gestión de clientes orientado a objetos que implementa los principios fundamentales de la POO en Python.

- ✅ Código bien estructurado y documentado
- ✅ Cumple todos los entregables académicos
- ✅ 34 tests unitarios (100% pasan)
- ✅ 6 ejemplos funcionales

---

## �� Estructura del Proyecto

```
gestor_inteligente_de_clientes/
├── entregable1/              # Entregable 1: POO
├── entregable2/              # Entregable 2: Encapsulación
├── entregable3/              # Entregable 3: Diagramas UML
├── entregable4/              # Entregable 4: Herencia y Polimorfismo
├── entregable5/              # Entregable 5: Manejo de Errores
├── src/                      # Código fuente (10 archivos)
├── tests/                    # Pruebas y ejemplos (2 archivos)
└── README.md                 # Este archivo
```

---

## 🚀 Uso del Sistema

### Ejecutar Ejemplos

```bash
cd tests
python3 ejemplo_uso.py
```

### Ejecutar Tests

```bash
cd tests
python3 test_unitarias.py
```

### Usar en Código

```python
import sys
sys.path.append('..')

from src import ClienteRegular, ClientePremium, ClienteCorporativo, GestorClientes

# Crear clientes
cliente1 = ClienteRegular("Juan Pérez", "juan@email.com", "912345678", 
                          "Av. Libertador 1234, Santiago")

cliente2 = ClientePremium("María López", "maria@email.com", "987654321",
                          "Av. Providencia 890", "Oro", 20.0)

# Usar gestor
gestor = GestorClientes()
gestor.agregar_cliente(cliente1)
gestor.agregar_cliente(cliente2)
```

---

## 🎓 Entregables

### ✅ Entregable 1: POO
- Carpeta: `entregable1/`
- Clase `Cliente` con atributos y métodos básicos
- Ejemplos de instanciación

### ✅ Entregable 2: Encapsulación
- Carpeta: `entregable2/`
- Validaciones de datos (email, teléfono, dirección)
- Getters y setters como métodos

### ✅ Entregable 3: Diagramas UML
- Carpeta: `entregable3/`
- Diagramas de clases con relaciones de herencia

### ✅ Entregable 4: Herencia y Polimorfismo
- Carpeta: `entregable4/`
- 3 tipos de clientes heredando de Cliente
- Método `calcular_descuento()` polimórfico
- Uso de `super()` en constructores

### ✅ Entregable 5: Manejo de Errores
- Carpeta: `entregable5/`
- 4 excepciones personalizadas
- 7 funciones de validación
- Sistema de logs en archivos

---

## 💡 Características del Sistema

### Tipos de Clientes

**ClienteRegular:**
- Cliente estándar sin beneficios especiales
- Registra fecha de ingreso
- Sin descuentos

**ClientePremium:**
- Sistema de puntos acumulables
- Niveles de membresía (Bronce, Plata, Oro)
- Descuentos configurables

**ClienteCorporativo:**
- Cliente empresarial
- Sistema de crédito corporativo
- Descuento fijo del 15%

### Funcionalidades

- ✅ Validación de datos (email, teléfono, dirección)
- ✅ Sistema de excepciones personalizadas
- ✅ Logging de operaciones
- ✅ Persistencia en JSON
- ✅ Gestión de múltiples clientes

---

## 📊 Diagrama de Clases

```
                Cliente (Base)
                     △
                     │
     ┌───────────────┼───────────────┐
     │               │               │
ClienteRegular  ClientePremium  ClienteCorporativo
```

Ver `entregable3/diagramas_uml.md` para detalles completos.

---

## 🧪 Tests

- **34 tests unitarios** (100% pasan)
- **6 ejemplos funcionales** (100% funcionan)

```bash
cd tests
python3 test_unitarias.py
# Resultado: OK (34 tests)
```

---

## 📚 Documentación

Consulta los entregables para documentación detallada:

1. **entregable1/** - Conceptos de POO
2. **entregable2/** - Encapsulación y validaciones
3. **entregable3/** - Diagramas de clases
4. **entregable4/** - Herencia y polimorfismo
5. **entregable5/** - Manejo de errores

---


