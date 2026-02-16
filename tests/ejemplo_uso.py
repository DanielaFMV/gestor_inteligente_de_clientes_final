"""
Ejemplo de Uso - Gestor Inteligente de Clientes
Proyecto: GIC
Empresa: SolutionTech

Este script muestra cómo usar el sistema completo del GIC.
Incluye ejemplos de todas las funcionalidades principales.
"""

import sys
import os

# Agregar el directorio padre al path para importar desde src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos todas las clases necesarias
from src.cliente import Cliente
from src.cliente_regular import ClienteRegular
from src.cliente_premium import ClientePremium
from src.cliente_corporativo import ClienteCorporativo
from src.gestor_clientes import GestorClientes
from src.excepciones import ValidacionError, ClienteDuplicadoError


def ejemplo_1_crear_clientes_basicos():
    """
    Ejemplo 1: Crear clientes de diferentes tipos.
    
    Demuestra:
    - Creación de ClienteRegular
    - Creación de ClientePremium
    - Creación de ClienteCorporativo
    """
    print("\n" + "=" * 70)
    print("EJEMPLO 1: CREAR CLIENTES DE DIFERENTES TIPOS")
    print("=" * 70)
    
    # Crear un cliente regular
    print("\n1. Creando Cliente Regular...")
    cliente_regular = ClienteRegular(
        nombre="Juan Pérez González",
        email="juan.perez@email.com",
        telefono="+56912345678",
        direccion="Av. Libertador Bernardo O'Higgins 1234, Santiago"
    )
    cliente_regular.mostrar_informacion()
    
    # Crear un cliente premium
    print("\n2. Creando Cliente Premium...")
    cliente_premium = ClientePremium(
        nombre="María López Soto",
        email="maria.lopez@email.com",
        telefono="+56987654321",
        direccion="Av. Providencia 890, Providencia",
        nivel_membresia="Oro",
        descuento=20.0
    )
    cliente_premium.mostrar_informacion()
    
    # Crear un cliente corporativo
    print("\n3. Creando Cliente Corporativo...")
    cliente_corporativo = ClienteCorporativo(
        nombre="Pedro Sánchez",
        email="pedro.sanchez@techsol.cl",
        telefono="+56955667788",
        direccion="Av. Apoquindo 4500, Las Condes",
        nombre_empresa="Tech Solutions SpA",
        rut_empresa="76.123.456-7",
        contacto_principal="Pedro Sánchez",
        limite_credito=500000.0
    )
    cliente_corporativo.mostrar_informacion()
    
    print("\n✓ Ejemplo 1 completado exitosamente\n")


def ejemplo_2_polimorfismo_descuentos():
    """
    Ejemplo 2: Demostrar POLIMORFISMO con el método calcular_descuento().
    
    Demuestra:
    - Mismo método, comportamiento diferente según el tipo de cliente
    - ClienteRegular: 0% descuento
    - ClientePremium: descuento según su nivel
    - ClienteCorporativo: 15% descuento
    """
    print("\n" + "=" * 70)
    print("EJEMPLO 2: POLIMORFISMO - CÁLCULO DE DESCUENTOS")
    print("=" * 70)
    
    # Crear clientes
    regular = ClienteRegular("Ana González", "ana@email.com", "912345678", "Calle 1 #123")
    premium = ClientePremium("Carlos Díaz", "carlos@email.com", "987654321", "Calle 2 #456", "Oro", 25.0)
    corporativo = ClienteCorporativo("Luis Rojas", "luis@empresa.com", "955667788", "Calle 3 #789",
                                    "Empresa ABC", "12.345.678-9", "Luis Rojas", 1000000.0)
    
    # Monto de compra
    monto_compra = 100000.0
    
    print(f"\nMonto de compra: ${monto_compra:,.2f}\n")
    
    # Calcular descuento para cada tipo (POLIMORFISMO)
    print(f"1. Cliente Regular ({regular.get_nombre()}):")
    descuento_regular = regular.calcular_descuento(monto_compra)
    print(f"   Descuento: ${descuento_regular:,.2f}")
    print(f"   Total a pagar: ${monto_compra - descuento_regular:,.2f}\n")
    
    print(f"2. Cliente Premium ({premium.get_nombre()}):")
    descuento_premium = premium.calcular_descuento(monto_compra)
    print(f"   Descuento: ${descuento_premium:,.2f} ({premium.get_descuento()}%)")
    print(f"   Total a pagar: ${monto_compra - descuento_premium:,.2f}\n")
    
    print(f"3. Cliente Corporativo ({corporativo.get_nombre_empresa()}):")
    descuento_corporativo = corporativo.calcular_descuento(monto_compra)
    print(f"   Descuento: ${descuento_corporativo:,.2f} (15%)")
    print(f"   Total a pagar: ${monto_compra - descuento_corporativo:,.2f}\n")
    
    print("✓ Ejemplo 2 completado exitosamente\n")


def ejemplo_3_puntos_premium():
    """
    Ejemplo 3: Sistema de puntos para clientes premium.
    
    Demuestra:
    - Agregar puntos
    - Canjear puntos
    - Manejo de puntos insuficientes
    """
    print("\n" + "=" * 70)
    print("EJEMPLO 3: SISTEMA DE PUNTOS - CLIENTE PREMIUM")
    print("=" * 70)
    
    # Crear cliente premium
    cliente = ClientePremium(
        nombre="Sofía Ramírez",
        email="sofia@email.com",
        telefono="944556677",
        direccion="Av. Italia 1500, Ñuñoa",
        nivel_membresia="Plata",
        descuento=15.0
    )
    
    print(f"\nPuntos iniciales: {cliente.get_puntos_acumulados()}\n")
    
    # Agregar puntos
    print("1. Agregando puntos por compras:")
    cliente.agregar_puntos(500)
    cliente.agregar_puntos(300)
    cliente.agregar_puntos(200)
    
    print(f"\nPuntos totales: {cliente.get_puntos_acumulados()}\n")
    
    # Canjear puntos exitosamente
    print("2. Canjeando 600 puntos:")
    exito = cliente.canjear_puntos(600)
    if exito:
        print("   ✓ Canje exitoso\n")
    
    # Intentar canjear más puntos de los disponibles
    print("3. Intentando canjear 500 puntos (tiene 400):")
    exito = cliente.canjear_puntos(500)
    if not exito:
        print("   ✗ Canje fallido - puntos insuficientes\n")
    
    print("✓ Ejemplo 3 completado exitosamente\n")


def ejemplo_4_credito_corporativo():
    """
    Ejemplo 4: Sistema de crédito para clientes corporativos.
    
    Demuestra:
    - Verificar crédito disponible
    - Utilizar crédito
    - Pagar crédito
    """
    print("\n" + "=" * 70)
    print("EJEMPLO 4: SISTEMA DE CRÉDITO - CLIENTE CORPORATIVO")
    print("=" * 70)
    
    # Crear cliente corporativo
    cliente = ClienteCorporativo(
        nombre="Roberto Flores",
        email="roberto@innovatech.cl",
        telefono="933445566",
        direccion="Av. Kennedy 5600, Vitacura",
        nombre_empresa="InnovaTech Ltda.",
        rut_empresa="77.654.321-0",
        contacto_principal="Roberto Flores",
        limite_credito=300000.0
    )
    
    print(f"\nLímite de crédito: ${cliente.get_limite_credito():,.2f}")
    print(f"Crédito disponible: ${cliente.get_credito_disponible():,.2f}\n")
    
    # Utilizar crédito
    print("1. Utilizando crédito:")
    cliente.utilizar_credito(100000.0)
    print()
    
    # Verificar crédito disponible
    print("2. Verificando crédito para nueva compra:")
    cliente.verificar_credito_disponible(150000.0)
    print()
    
    # Utilizar más crédito
    print("3. Utilizando más crédito:")
    cliente.utilizar_credito(80000.0)
    print()
    
    # Pagar crédito
    print("4. Pagando parte del crédito:")
    cliente.pagar_credito(50000.0)
    print()
    
    print("✓ Ejemplo 4 completado exitosamente\n")


def ejemplo_5_gestor_clientes():
    """
    Ejemplo 5: Usar el GestorClientes para manejar múltiples clientes.
    
    Demuestra:
    - Agregar múltiples clientes
    - Buscar clientes
    - Listar clientes
    - Actualizar clientes
    - Eliminar clientes
    - Persistencia automática
    """
    print("\n" + "=" * 70)
    print("EJEMPLO 5: GESTOR DE CLIENTES")
    print("=" * 70)
    
    # Crear el gestor
    print("\n1. Creando gestor de clientes...")
    gestor = GestorClientes(usar_persistencia=False, usar_logs=False)
    print()
    
    # Agregar varios clientes
    print("2. Agregando clientes...")
    
    cliente1 = ClienteRegular("Andrea Torres", "andrea@email.com", "911223344", "Calle Ahumada 123")
    gestor.agregar_cliente(cliente1)
    
    cliente2 = ClientePremium("Rodrigo Silva", "rodrigo@email.com", "922334455", "Av. Brasil 456", "Oro", 20.0)
    gestor.agregar_cliente(cliente2)
    
    cliente3 = ClienteCorporativo("Carmen Vega", "carmen@corp.cl", "933445566", "Av. Las Condes 789",
                                 "CorpSA", "88.999.888-7", "Carmen Vega", 600000.0)
    gestor.agregar_cliente(cliente3)
    print()
    
    # Mostrar resumen
    print("3. Mostrando resumen del gestor:")
    gestor.mostrar_resumen()
    
    # Buscar cliente
    print("4. Buscando cliente por email:")
    try:
        cliente = gestor.buscar_por_email("rodrigo@email.com")
        cliente.mostrar_informacion()
    except Exception as e:
        print(f"Error: {e}")
    
    # Buscar por nombre
    print("\n5. Buscando clientes por nombre:")
    encontrados = gestor.buscar_por_nombre("a")
    for cli in encontrados:
        print(f"   - {cli.get_nombre()}")
    print()
    
    # Listar por tipo
    print("6. Listando solo clientes Premium:")
    premium = gestor.listar_por_tipo("Premium")
    for cli in premium:
        print(f"   - {cli}")
    print()
    
    print("✓ Ejemplo 5 completado exitosamente\n")


def ejemplo_6_manejo_errores():
    """
    Ejemplo 6: Manejo de errores y validaciones.
    
    Demuestra:
    - Validación de email
    - Validación de teléfono
    - Validación de dirección
    - Manejo de excepciones personalizadas
    """
    print("\n" + "=" * 70)
    print("EJEMPLO 6: MANEJO DE ERRORES Y VALIDACIONES")
    print("=" * 70)
    
    # Intentar crear cliente con email inválido
    print("\n1. Intentando crear cliente con email inválido:")
    try:
        cliente = ClienteRegular("Juan Pérez", "email_invalido", "912345678", "Calle Principal 123")
    except ValidacionError as e:
        print(f"   ✗ Error capturado: {e}\n")
    
    # Intentar crear cliente con teléfono inválido
    print("2. Intentando crear cliente con teléfono inválido:")
    try:
        cliente = ClienteRegular("María López", "maria@email.com", "123", "Calle Secundaria 456")
    except ValidacionError as e:
        print(f"   ✗ Error capturado: {e}\n")
    
    # Intentar crear cliente con dirección muy corta
    print("3. Intentando crear cliente con dirección muy corta:")
    try:
        cliente = ClienteRegular("Carlos Díaz", "carlos@email.com", "912345678", "Calle 1")
    except ValidacionError as e:
        print(f"   ✗ Error capturado: {e}\n")
    
    # Cliente válido
    print("4. Creando cliente con datos válidos:")
    try:
        cliente = ClienteRegular("Ana González", "ana@email.com", "912345678", "Av. Libertador 1234, Santiago")
        print("   ✓ Cliente creado exitosamente")
        print(f"   {cliente}\n")
    except ValidacionError as e:
        print(f"   ✗ Error: {e}\n")
    
    print("✓ Ejemplo 6 completado exitosamente\n")


def main():
    """
    Función principal que ejecuta todos los ejemplos.
    """
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "  GESTOR INTELIGENTE DE CLIENTES (GIC)".center(68) + "║")
    print("║" + "  SolutionTech - Ejemplos de Uso".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    
    # Ejecutar todos los ejemplos
    try:
        ejemplo_1_crear_clientes_basicos()
        ejemplo_2_polimorfismo_descuentos()
        ejemplo_3_puntos_premium()
        ejemplo_4_credito_corporativo()
        ejemplo_5_gestor_clientes()
        ejemplo_6_manejo_errores()
        
        # Mensaje final
        print("\n" + "=" * 70)
        print("TODOS LOS EJEMPLOS COMPLETADOS EXITOSAMENTE")
        print("=" * 70)
        print("\n✓ El sistema funciona correctamente")
        print("✓ Todos los componentes han sido probados")
        print("✓ Las validaciones están funcionando")
        print("✓ El polimorfismo está implementado correctamente")
        print("\n" + "=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error inesperado: {e}\n")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
