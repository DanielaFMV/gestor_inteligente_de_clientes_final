# Estructura del Proyecto GIC

## Organización de Archivos

```
gestor_inteligente_de_clientes/
│
├── entregable1/              # Entregable 1: Paradigma de POO
│   ├── README.md
│   └── entregable1_poo.md
│
├── entregable2/              # Entregable 2: Encapsulación
│   ├── README.md
│   └── entregable2.md
│
├── entregable3/              # Entregable 3: Diagramas UML
│   ├── README.md
│   ├── entregable3.md
│   └── diagramas_uml.md
│
├── entregable4/              # Entregable 4: Herencia y Polimorfismo
│   ├── README.md
│   └── entregable4.md
│
├── entregable5/              # Entregable 5: Manejo de Errores
│   ├── README.md
│   └── entregable5.md
│
├── src/                      # Código fuente del sistema
│   ├── __init__.py
│   ├── cliente.py
│   ├── cliente_regular.py
│   ├── cliente_premium.py
│   ├── cliente_corporativo.py
│   ├── validaciones.py
│   ├── excepciones.py
│   ├── logs.py
│   ├── persistencia.py
│   └── gestor_clientes.py
│
├── tests/                    # Pruebas y ejemplos
│   ├── ejemplo_uso.py
│   └── test_unitarias.py
│
├── README.md
├── ESTRUCTURA.md
└── .gitignore
```

## Descripción de Carpetas

### entregable1/ - entregable5/
Cada carpeta contiene la documentación de un entregable específico del módulo.
Los archivos .md explican los conceptos teóricos y muestran ejemplos prácticos.

### src/
Contiene todo el código fuente del sistema. Los archivos están organizados por funcionalidad:
- Clases de clientes (base y especializadas)
- Validaciones y excepciones
- Sistemas de soporte (logs, persistencia, gestor)

### tests/
Contiene las pruebas unitarias y ejemplos de uso del sistema.

## Uso

Para trabajar con el código:

```bash
# Ver ejemplos
cd tests
python3 ejemplo_uso.py

# Ejecutar tests
python3 test_unitarias.py

# Importar en código propio
import sys
sys.path.append('..')
from src import Cliente, ClienteRegular, ClientePremium
```

## Dependencias

El proyecto usa solo la biblioteca estándar de Python 3.
No requiere instalación de paquetes adicionales.
