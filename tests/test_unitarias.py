"""
Tests Unitarios - Gestor Inteligente de Clientes
Proyecto: GIC
Empresa: SolutionTech

Este archivo contiene pruebas unitarias para verificar
que todas las funcionalidades del sistema funcionan correctamente.
"""

# Importamos el módulo unittest (sistema de tests de Python)
import unittest
import sys
import os

# Agregar el directorio padre al path para importar desde src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos las clases a probar
from src.cliente import Cliente
from src.cliente_regular import ClienteRegular
from src.cliente_premium import ClientePremium
from src.cliente_corporativo import ClienteCorporativo
from src.gestor_clientes import GestorClientes

# Importamos las excepciones
from src.excepciones import ValidacionError, ClienteDuplicadoError

# Importamos validaciones
from src.validaciones import (
    validar_email,
    validar_telefono,
    validar_nombre,
    validar_direccion
)


class TestValidaciones(unittest.TestCase):
    """
    Tests para las funciones de validación.
    
    unittest.TestCase es la clase base para crear tests.
    Cada método que empiece con 'test_' será ejecutado como un test.
    """
    
    def test_validar_email_correcto(self):
        """Test: Email válido debe pasar la validación."""
        # assertTrue verifica que el resultado sea True
        self.assertTrue(validar_email("juan@email.com"))
        self.assertTrue(validar_email("maria.lopez@empresa.cl"))
    
    def test_validar_email_incorrecto(self):
        """Test: Email inválido debe lanzar excepción."""
        # assertRaises verifica que se lance la excepción esperada
        with self.assertRaises(ValidacionError):
            validar_email("email_sin_arroba")
        with self.assertRaises(ValidacionError):
            validar_email("@sinusuario.com")
    
    def test_validar_telefono_correcto(self):
        """Test: Teléfono válido debe pasar la validación."""
        self.assertTrue(validar_telefono("+56912345678"))
        self.assertTrue(validar_telefono("912345678"))
        self.assertTrue(validar_telefono("+56 9 1234 5678"))
    
    def test_validar_telefono_incorrecto(self):
        """Test: Teléfono inválido debe lanzar excepción."""
        with self.assertRaises(ValidacionError):
            validar_telefono("123")  # Muy corto
        with self.assertRaises(ValidacionError):
            validar_telefono("812345678")  # No empieza con 9
    
    def test_validar_nombre_correcto(self):
        """Test: Nombre válido debe pasar la validación."""
        self.assertTrue(validar_nombre("Juan Pérez"))
        self.assertTrue(validar_nombre("María González Soto"))
    
    def test_validar_nombre_incorrecto(self):
        """Test: Nombre inválido debe lanzar excepción."""
        with self.assertRaises(ValidacionError):
            validar_nombre("AB")  # Muy corto
        with self.assertRaises(ValidacionError):
            validar_nombre("Juan123")  # Tiene números
    
    def test_validar_direccion_correcta(self):
        """Test: Dirección válida debe pasar la validación."""
        self.assertTrue(validar_direccion("Av. Libertador 1234, Santiago"))
    
    def test_validar_direccion_incorrecta(self):
        """Test: Dirección inválida debe lanzar excepción."""
        with self.assertRaises(ValidacionError):
            validar_direccion("Calle 1")  # Muy corta


class TestClienteSimple(unittest.TestCase):
    """Tests para la clase Cliente base."""
    
    def setUp(self):
        """
        Método especial que se ejecuta ANTES de cada test.
        Prepara los datos de prueba.
        """
        self.cliente = Cliente(
            nombre="Juan Pérez",
            email="juan@email.com",
            telefono="912345678",
            direccion="Av. Libertador 1234, Santiago"
        )
    
    def test_crear_cliente(self):
        """Test: Crear un cliente correctamente."""
        # assertEqual verifica que dos valores sean iguales
        self.assertEqual(self.cliente.get_nombre(), "Juan Pérez")
        self.assertEqual(self.cliente.get_email(), "juan@email.com")
        self.assertEqual(self.cliente.get_telefono(), "912345678")
    
    def test_actualizar_email(self):
        """Test: Actualizar email de un cliente."""
        self.cliente.set_email("nuevo@email.com")
        self.assertEqual(self.cliente.get_email(), "nuevo@email.com")
    
    def test_actualizar_telefono(self):
        """Test: Actualizar teléfono de un cliente."""
        self.cliente.set_telefono("987654321")
        self.assertEqual(self.cliente.get_telefono(), "987654321")
    
    def test_obtener_resumen(self):
        """Test: Obtener resumen del cliente como diccionario."""
        resumen = self.cliente.obtener_resumen()
        # assertIsInstance verifica que sea del tipo correcto
        self.assertIsInstance(resumen, dict)
        # assertIn verifica que una clave esté en el diccionario
        self.assertIn('nombre', resumen)
        self.assertIn('email', resumen)


class TestClienteRegular(unittest.TestCase):
    """Tests para la clase ClienteRegular."""
    
    def setUp(self):
        """Preparar datos de prueba."""
        self.cliente = ClienteRegular(
            nombre="Ana González",
            email="ana@email.com",
            telefono="911223344",
            direccion="Calle Principal 123, Santiago"
        )
    
    def test_herencia(self):
        """Test: ClienteRegular hereda de Cliente."""
        # assertIsInstance verifica que sea instancia de la clase
        self.assertIsInstance(self.cliente, Cliente)
        self.assertIsInstance(self.cliente, ClienteRegular)
    
    def test_descuento_cero(self):
        """Test: Cliente regular no tiene descuento."""
        descuento = self.cliente.calcular_descuento(1000)
        self.assertEqual(descuento, 0.0)
    
    def test_fecha_registro(self):
        """Test: Cliente regular tiene fecha de registro."""
        fecha = self.cliente.get_fecha_registro()
        # assertIsNotNone verifica que no sea None
        self.assertIsNotNone(fecha)


class TestClientePremium(unittest.TestCase):
    """Tests para la clase ClientePremium."""
    
    def setUp(self):
        """Preparar datos de prueba."""
        self.cliente = ClientePremium(
            nombre="Carlos Díaz",
            email="carlos@email.com",
            telefono="922334455",
            direccion="Av. Brasil 456, Santiago",
            nivel_membresia="Oro",
            descuento=20.0
        )
    
    def test_herencia(self):
        """Test: ClientePremium hereda de Cliente."""
        self.assertIsInstance(self.cliente, Cliente)
        self.assertIsInstance(self.cliente, ClientePremium)
    
    def test_descuento_correcto(self):
        """Test: Cliente premium tiene descuento correcto."""
        descuento = self.cliente.calcular_descuento(1000)
        # 20% de 1000 = 200
        self.assertEqual(descuento, 200.0)
    
    def test_agregar_puntos(self):
        """Test: Agregar puntos funciona correctamente."""
        self.cliente.agregar_puntos(100)
        self.assertEqual(self.cliente.get_puntos_acumulados(), 100)
        self.cliente.agregar_puntos(50)
        self.assertEqual(self.cliente.get_puntos_acumulados(), 150)
    
    def test_canjear_puntos_exitoso(self):
        """Test: Canjear puntos cuando hay suficientes."""
        self.cliente.agregar_puntos(500)
        exito = self.cliente.canjear_puntos(300)
        # assertTrue verifica que sea True
        self.assertTrue(exito)
        self.assertEqual(self.cliente.get_puntos_acumulados(), 200)
    
    def test_canjear_puntos_insuficientes(self):
        """Test: Canjear puntos cuando no hay suficientes."""
        self.cliente.agregar_puntos(100)
        exito = self.cliente.canjear_puntos(200)
        # assertFalse verifica que sea False
        self.assertFalse(exito)
        self.assertEqual(self.cliente.get_puntos_acumulados(), 100)


class TestClienteCorporativo(unittest.TestCase):
    """Tests para la clase ClienteCorporativo."""
    
    def setUp(self):
        """Preparar datos de prueba."""
        self.cliente = ClienteCorporativo(
            nombre="Luis Rojas",
            email="luis@empresa.com",
            telefono="933445566",
            direccion="Av. Kennedy 5000, Vitacura",
            nombre_empresa="Empresa XYZ",
            rut_empresa="76.543.210-9",
            contacto_principal="Luis Rojas",
            limite_credito=500000.0
        )
    
    def test_herencia(self):
        """Test: ClienteCorporativo hereda de Cliente."""
        self.assertIsInstance(self.cliente, Cliente)
        self.assertIsInstance(self.cliente, ClienteCorporativo)
    
    def test_descuento_corporativo(self):
        """Test: Cliente corporativo tiene 15% de descuento."""
        descuento = self.cliente.calcular_descuento(1000)
        # 15% de 1000 = 150
        self.assertEqual(descuento, 150.0)
    
    def test_credito_disponible_inicial(self):
        """Test: Crédito disponible inicial es igual al límite."""
        disponible = self.cliente.get_credito_disponible()
        self.assertEqual(disponible, 500000.0)
    
    def test_utilizar_credito(self):
        """Test: Utilizar crédito reduce el disponible."""
        exito = self.cliente.utilizar_credito(100000.0)
        self.assertTrue(exito)
        self.assertEqual(self.cliente.get_credito_disponible(), 400000.0)
    
    def test_pagar_credito(self):
        """Test: Pagar crédito aumenta el disponible."""
        self.cliente.utilizar_credito(200000.0)
        self.cliente.pagar_credito(50000.0)
        self.assertEqual(self.cliente.get_credito_disponible(), 350000.0)
    
    def test_verificar_credito_suficiente(self):
        """Test: Verificar crédito cuando hay suficiente."""
        resultado = self.cliente.verificar_credito_disponible(100000.0)
        self.assertTrue(resultado)
    
    def test_verificar_credito_insuficiente(self):
        """Test: Verificar crédito cuando no hay suficiente."""
        self.cliente.utilizar_credito(450000.0)
        resultado = self.cliente.verificar_credito_disponible(100000.0)
        self.assertFalse(resultado)


class TestGestorClientes(unittest.TestCase):
    """Tests para la clase GestorClientes."""
    
    def setUp(self):
        """Preparar datos de prueba."""
        # Creamos gestor sin persistencia ni logs para tests
        self.gestor = GestorClientes(usar_persistencia=False, usar_logs=False)
        
        # Agregamos algunos clientes de prueba
        self.cliente1 = ClienteRegular("Test Uno", "test1@email.com", "911111111", "Dirección Test Uno Santiago")
        self.cliente2 = ClientePremium("Test Dos", "test2@email.com", "922222222", "Dirección Test Dos Santiago", "Oro", 20.0)
        self.cliente3 = ClienteCorporativo("Test Tres", "test3@email.com", "933333333", "Dirección Test Tres Santiago",
                                          "Empresa Test", "11.111.111-1", "Test Tres", 1000000.0)
    
    def test_agregar_cliente(self):
        """Test: Agregar un cliente al gestor."""
        self.gestor.agregar_cliente(self.cliente1)
        # len() retorna la cantidad de clientes
        self.assertEqual(len(self.gestor), 1)
    
    def test_agregar_cliente_duplicado(self):
        """Test: No se puede agregar cliente con email duplicado."""
        self.gestor.agregar_cliente(self.cliente1)
        with self.assertRaises(ClienteDuplicadoError):
            self.gestor.agregar_cliente(self.cliente1)
    
    def test_buscar_por_email(self):
        """Test: Buscar cliente por email."""
        self.gestor.agregar_cliente(self.cliente1)
        encontrado = self.gestor.buscar_por_email("test1@email.com")
        self.assertEqual(encontrado, self.cliente1)
    
    def test_buscar_por_nombre(self):
        """Test: Buscar clientes por nombre."""
        self.gestor.agregar_cliente(self.cliente1)
        self.gestor.agregar_cliente(self.cliente2)
        encontrados = self.gestor.buscar_por_nombre("Test")
        self.assertEqual(len(encontrados), 2)
    
    def test_listar_todos(self):
        """Test: Listar todos los clientes."""
        self.gestor.agregar_cliente(self.cliente1)
        self.gestor.agregar_cliente(self.cliente2)
        self.gestor.agregar_cliente(self.cliente3)
        todos = self.gestor.listar_todos()
        self.assertEqual(len(todos), 3)
    
    def test_listar_por_tipo(self):
        """Test: Listar clientes por tipo."""
        self.gestor.agregar_cliente(self.cliente1)
        self.gestor.agregar_cliente(self.cliente2)
        self.gestor.agregar_cliente(self.cliente3)
        
        premium = self.gestor.listar_por_tipo("Premium")
        self.assertEqual(len(premium), 1)
        
        corporativo = self.gestor.listar_por_tipo("Corporativo")
        self.assertEqual(len(corporativo), 1)
    
    def test_eliminar_cliente(self):
        """Test: Eliminar un cliente."""
        self.gestor.agregar_cliente(self.cliente1)
        exito = self.gestor.eliminar_cliente("test1@email.com")
        self.assertTrue(exito)
        self.assertEqual(len(self.gestor), 0)


def ejecutar_tests():
    """
    Función para ejecutar todos los tests.
    """
    print("\n" + "=" * 70)
    print("EJECUTANDO TESTS UNITARIOS - GIC")
    print("=" * 70 + "\n")
    
    # unittest.main() ejecuta todos los tests
    # verbosity=2 muestra información detallada
    # exit=False evita que cierre el programa
    unittest.main(verbosity=2, exit=False)


if __name__ == "__main__":
    # Si ejecutamos este archivo directamente, correr los tests
    ejecutar_tests()
