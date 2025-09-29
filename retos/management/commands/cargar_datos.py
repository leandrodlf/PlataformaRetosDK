from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from retos.models import Categoria, Reto, Alternativa, PerfilUsuario
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="inacap").exists():
    User.objects.create_superuser(
        username="inacap",
        email="inacap@example.com",
        password="inacap"
    )
    print("Superusuario 'inacap' creado exitosamente.")
else:
    print("Superusuario 'inacap' ya existe.")

class Command(BaseCommand):
    help = 'Carga datos de ejemplo para la plataforma'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos de ejemplo...')
        
        categorias_data = [
            {'nombre': 'Matemáticas Básicas', 'descripcion': 'Problemas de aritmética y conceptos fundamentales'},
            {'nombre': 'Álgebra', 'descripcion': 'Ecuaciones y expresiones algebraicas'},
            {'nombre': 'Geometría', 'descripcion': 'Figuras y propiedades espaciales'},
            {'nombre': 'Lógica', 'descripcion': 'Problemas de razonamiento lógico'},
            {'nombre': 'Trigonometría', 'descripcion': 'Funciones trigonométricas y aplicaciones'},
            {'nombre': 'Probabilidad', 'descripcion': 'Problemas de probabilidad y estadística'},
            {'nombre': 'Aritmética', 'descripcion': 'Operaciones numéricas básicas'},
        ]
        
        categorias = {}
        for cat_data in categorias_data:
            categoria, created = Categoria.objects.get_or_create(
                nombre=cat_data['nombre'],
                defaults={'descripcion': cat_data['descripcion']}
            )
            categorias[cat_data['nombre']] = categoria
            if created:
                self.stdout.write(f'Categoría creada: {cat_data["nombre"]}')
        
        retos_data = [
            {
                'titulo': 'El acertijo del pastor',
                'descripcion': 'Un clásico problema de lógica sobre cómo cruzar un río',
                'contenido': 'Un pastor tiene que cruzar un lobo, una cabra y una lechuga a la otra orilla de un río. Dispone de una barca en la que solo caben él y uno de los otros tres. Si el lobo se queda solo con la cabra se la come, si la cabra se queda sola con la lechuga se la come. ¿Cómo puede hacer para cruzar a los tres?',
                'dificultad': 'F',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '3',
                'puntos': 10,
                'alternativas': [
                    {'texto': 'Primero cruza la cabra, luego el lobo, y finalmente la lechuga', 'es_correcta': False},
                    {'texto': 'Primero cruza el lobo, luego la cabra, y finalmente la lechuga', 'es_correcta': False},
                    {'texto': 'Primero cruza la cabra, luego la lechuga, vuelve con la cabra, cruza el lobo, y finalmente cruza la cabra', 'es_correcta': True},
                    {'texto': 'Primero cruza la lechuga, luego la cabra, y finalmente el lobo', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de edades',
                'descripcion': 'Calcula las edades basándote en las pistas dadas',
                'contenido': 'Juan tiene el doble de la edad que Pedro tenía cuando Juan tenía la edad que Pedro tiene ahora. Si Pedro tiene 24 años, ¿cuántos años tiene Juan?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '2',
                'puntos': 20,
                'alternativas': [
                    {'texto': '30 años', 'es_correcta': False},
                    {'texto': '32 años', 'es_correcta': True},
                    {'texto': '28 años', 'es_correcta': False},
                    {'texto': '36 años', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Secuencia numérica',
                'descripcion': 'Encuentra el patrón y el número que sigue',
                'contenido': '¿Qué número sigue en la secuencia: 2, 6, 12, 20, 30, ?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Matemáticas Básicas',
                'respuesta_correcta': '4',
                'puntos': 10,
                'alternativas': [
                    {'texto': '40', 'es_correcta': False},
                    {'texto': '42', 'es_correcta': True},
                    {'texto': '44', 'es_correcta': False},
                    {'texto': '36', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de monedas',
                'descripcion': 'Divide las monedas de forma justa',
                'contenido': 'Tienes 12 monedas que parecen iguales, pero una de ellas es falsa y pesa ligeramente diferente. Con una balanza de platillos, ¿cuál es el mínimo número de pesadas necesarias para encontrar la moneda falsa?',
                'dificultad': 'D',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '1',
                'puntos': 30,
                'alternativas': [
                    {'texto': '2 pesadas', 'es_correcta': False},
                    {'texto': '3 pesadas', 'es_correcta': True},
                    {'texto': '4 pesadas', 'es_correcta': False},
                    {'texto': '5 pesadas', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Área del triángulo',
                'descripcion': 'Calcula el área de un triángulo especial',
                'contenido': 'Un triángulo rectángulo tiene catetos de 6 cm y 8 cm. ¿Cuál es el área del triángulo?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '3',
                'puntos': 10,
                'alternativas': [
                    {'texto': '24 cm²', 'es_correcta': True},
                    {'texto': '48 cm²', 'es_correcta': False},
                    {'texto': '14 cm²', 'es_correcta': False},
                    {'texto': '28 cm²', 'es_correcta': False},
                ]
            },
            
            {
                'titulo': 'Suma básica',
                'descripcion': 'Realiza una operación aritmética simple',
                'contenido': '¿Cuánto es 15 + 27?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '2',
                'puntos': 5,
                'alternativas': [
                    {'texto': '40', 'es_correcta': False},
                    {'texto': '42', 'es_correcta': True},
                    {'texto': '38', 'es_correcta': False},
                    {'texto': '45', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Patrón simple',
                'descripcion': 'Identifica el patrón numérico',
                'contenido': '¿Qué número sigue? 5, 10, 15, 20, ?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Matemáticas Básicas',
                'respuesta_correcta': '3',
                'puntos': 5,
                'alternativas': [
                    {'texto': '22', 'es_correcta': False},
                    {'texto': '30', 'es_correcta': False},
                    {'texto': '25', 'es_correcta': True},
                    {'texto': '35', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Multiplicación básica',
                'descripcion': 'Calcula el resultado de multiplicar',
                'contenido': '¿Cuánto es 7 × 8?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '3',
                'puntos': 5,
                'alternativas': [
                    {'texto': '54', 'es_correcta': False},
                    {'texto': '58', 'es_correcta': False},
                    {'texto': '56', 'es_correcta': True},
                    {'texto': '64', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Fracción simple',
                'descripcion': 'Simplifica una fracción básica',
                'contenido': 'Simplifica la fracción 12/16',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '1',
                'puntos': 8,
                'alternativas': [
                    {'texto': '3/4', 'es_correcta': True},
                    {'texto': '2/3', 'es_correcta': False},
                    {'texto': '4/5', 'es_correcta': False},
                    {'texto': '6/8', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Perímetro del cuadrado',
                'descripcion': 'Calcula el perímetro de una figura simple',
                'contenido': 'Un cuadrado tiene lados de 5 cm. ¿Cuál es su perímetro?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '2',
                'puntos': 8,
                'alternativas': [
                    {'texto': '15 cm', 'es_correcta': False},
                    {'texto': '20 cm', 'es_correcta': True},
                    {'texto': '25 cm', 'es_correcta': False},
                    {'texto': '10 cm', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Ecuación lineal simple',
                'descripcion': 'Resuelve una ecuación de primer grado',
                'contenido': 'Resuelve para x: 2x + 5 = 15',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '1',
                'puntos': 10,
                'alternativas': [
                    {'texto': '5', 'es_correcta': True},
                    {'texto': '10', 'es_correcta': False},
                    {'texto': '7.5', 'es_correcta': False},
                    {'texto': '8', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Porcentaje básico',
                'descripcion': 'Calcula un porcentaje simple',
                'contenido': '¿Cuánto es el 20% de 150?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '3',
                'puntos': 8,
                'alternativas': [
                    {'texto': '20', 'es_correcta': False},
                    {'texto': '25', 'es_correcta': False},
                    {'texto': '30', 'es_correcta': True},
                    {'texto': '35', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Lógica de hermanos',
                'descripcion': 'Problema de relaciones familiares',
                'contenido': 'Si María es hermana de Juan, y Juan es hermano de Pedro, ¿qué relación tiene María con Pedro?',
                'dificultad': 'F',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '1',
                'puntos': 8,
                'alternativas': [
                    {'texto': 'Hermanos', 'es_correcta': True},
                    {'texto': 'Primos', 'es_correcta': False},
                    {'texto': 'Tío/sobrino', 'es_correcta': False},
                    {'texto': 'No hay relación', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Área del rectángulo',
                'descripcion': 'Calcula el área de un rectángulo',
                'contenido': 'Un rectángulo mide 8 cm de largo y 3 cm de ancho. ¿Cuál es su área?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '4',
                'puntos': 8,
                'alternativas': [
                    {'texto': '11 cm²', 'es_correcta': False},
                    {'texto': '16 cm²', 'es_correcta': False},
                    {'texto': '20 cm²', 'es_correcta': False},
                    {'texto': '24 cm²', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'División básica',
                'descripcion': 'Realiza una división simple',
                'contenido': '¿Cuánto es 84 ÷ 7?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '2',
                'puntos': 8,
                'alternativas': [
                    {'texto': '10', 'es_correcta': False},
                    {'texto': '12', 'es_correcta': True},
                    {'texto': '14', 'es_correcta': False},
                    {'texto': '16', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Patrón de letras',
                'descripcion': 'Encuentra el patrón en una secuencia de letras',
                'contenido': '¿Qué letra sigue? A, C, E, G, ?',
                'dificultad': 'F',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '3',
                'puntos': 8,
                'alternativas': [
                    {'texto': 'H', 'es_correcta': False},
                    {'texto': 'F', 'es_correcta': False},
                    {'texto': 'I', 'es_correcta': True},
                    {'texto': 'J', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Volumen del cubo',
                'descripcion': 'Calcula el volumen de un cubo',
                'contenido': 'Un cubo tiene aristas de 3 cm. ¿Cuál es su volumen?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '4',
                'puntos': 10,
                'alternativas': [
                    {'texto': '9 cm³', 'es_correcta': False},
                    {'texto': '12 cm³', 'es_correcta': False},
                    {'texto': '18 cm³', 'es_correcta': False},
                    {'texto': '27 cm³', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Ecuación con fracciones',
                'descripcion': 'Resuelve una ecuación simple con fracciones',
                'contenido': 'Resuelve para x: x/4 = 3',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '2',
                'puntos': 10,
                'alternativas': [
                    {'texto': '7', 'es_correcta': False},
                    {'texto': '12', 'es_correcta': True},
                    {'texto': '9', 'es_correcta': False},
                    {'texto': '15', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Promedio simple',
                'descripcion': 'Calcula el promedio de números',
                'contenido': '¿Cuál es el promedio de 4, 8, 12 y 16?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '1',
                'puntos': 10,
                'alternativas': [
                    {'texto': '10', 'es_correcta': True},
                    {'texto': '12', 'es_correcta': False},
                    {'texto': '8', 'es_correcta': False},
                    {'texto': '14', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de tiempo',
                'descripcion': 'Calcula duraciones temporales',
                'contenido': 'Si son las 3:15 PM y pasan 45 minutos, ¿qué hora es?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '3',
                'puntos': 8,
                'alternativas': [
                    {'texto': '3:45 AM', 'es_correcta': False},
                    {'texto': '4:00 PM', 'es_correcta': False},
                    {'texto': '4:00 PM', 'es_correcta': True},
                    {'texto': '4:15 PM', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Lógica de direcciones',
                'descripcion': 'Problema de orientación espacial',
                'contenido': 'Si camino 5 km al norte, luego 3 km al este, y finalmente 5 km al sur, ¿a qué distancia estoy del punto de inicio?',
                'dificultad': 'F',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '2',
                'puntos': 10,
                'alternativas': [
                    {'texto': '0 km', 'es_correcta': False},
                    {'texto': '3 km', 'es_correcta': True},
                    {'texto': '5 km', 'es_correcta': False},
                    {'texto': '8 km', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Potenciación básica',
                'descripcion': 'Calcula potencias simples',
                'contenido': '¿Cuánto es 5² + 3²?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '4',
                'puntos': 8,
                'alternativas': [
                    {'texto': '16', 'es_correcta': False},
                    {'texto': '25', 'es_correcta': False},
                    {'texto': '30', 'es_correcta': False},
                    {'texto': '34', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Problema de edades simple',
                'descripcion': 'Calcula edades con datos básicos',
                'contenido': 'Pedro tiene 15 años y su hermana tiene 8 años. ¿Cuántos años tiene Pedro más que su hermana?',
                'dificultad': 'F',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '1',
                'puntos': 5,
                'alternativas': [
                    {'texto': '7 años', 'es_correcta': True},
                    {'texto': '8 años', 'es_correcta': False},
                    {'texto': '6 años', 'es_correcta': False},
                    {'texto': '9 años', 'es_correcta': False},
                ]
            },
            
            {
                'titulo': 'Sistema de ecuaciones',
                'descripcion': 'Resuelve un sistema de dos ecuaciones',
                'contenido': 'Resuelve el sistema: 2x + y = 10, x - y = 2',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 20,
                'alternativas': [
                    {'texto': 'x=3, y=4', 'es_correcta': False},
                    {'texto': 'x=4, y=2', 'es_correcta': False},
                    {'texto': 'x=4, y=2', 'es_correcta': True},
                    {'texto': 'x=5, y=0', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Teorema de Pitágoras',
                'descripcion': 'Aplica el teorema de Pitágoras',
                'contenido': 'Un triángulo rectángulo tiene catetos de 5 cm y 12 cm. ¿Cuánto mide la hipotenusa?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '2',
                'puntos': 20,
                'alternativas': [
                    {'texto': '13 cm', 'es_correcta': True},
                    {'texto': '15 cm', 'es_correcta': False},
                    {'texto': '17 cm', 'es_correcta': False},
                    {'texto': '19 cm', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de mezclas',
                'descripcion': 'Calcula proporciones en mezclas',
                'contenido': 'Se mezclan 4 litros de alcohol al 20% con 6 litros de alcohol al 40%. ¿Qué porcentaje de alcohol tiene la mezcla?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '4',
                'puntos': 25,
                'alternativas': [
                    {'texto': '28%', 'es_correcta': False},
                    {'texto': '30%', 'es_correcta': False},
                    {'texto': '31%', 'es_correcta': False},
                    {'texto': '32%', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Lógica de mentirosos',
                'descripcion': 'Problema clásico de lógica con mentirosos',
                'contenido': 'En una isla hay dos tribus: los que siempre dicen la verdad y los que siempre mienten. Te encuentras con dos personas. La primera dice: "Ambos somos mentirosos". ¿Qué puedes concluir?',
                'dificultad': 'M',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '1',
                'puntos': 25,
                'alternativas': [
                    {'texto': 'El primero miente, el segundo dice la verdad', 'es_correcta': True},
                    {'texto': 'Ambos dicen la verdad', 'es_correcta': False},
                    {'texto': 'Ambos mienten', 'es_correcta': False},
                    {'texto': 'El primero dice la verdad, el segundo miente', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Ecuación cuadrática',
                'descripcion': 'Resuelve una ecuación de segundo grado',
                'contenido': 'Resuelve: x² - 5x + 6 = 0',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '2',
                'puntos': 20,
                'alternativas': [
                    {'texto': 'x=1, x=6', 'es_correcta': False},
                    {'texto': 'x=2, x=3', 'es_correcta': True},
                    {'texto': 'x=-2, x=-3', 'es_correcta': False},
                    {'texto': 'x=0, x=5', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Área del círculo',
                'descripcion': 'Calcula el área de un círculo',
                'contenido': 'Un círculo tiene radio de 7 cm. ¿Cuál es su área? (Usa π=3.14)',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '3',
                'puntos': 20,
                'alternativas': [
                    {'texto': '43.96 cm²', 'es_correcta': False},
                    {'texto': '153.86 cm²', 'es_correcta': True},
                    {'texto': '21.98 cm²', 'es_correcta': False},
                    {'texto': '87.92 cm²', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de trabajo',
                'descripcion': 'Calcula tiempos de trabajo conjunto',
                'contenido': 'Juan puede hacer un trabajo en 6 horas, Pedro en 4 horas. ¿Cuánto tardan trabajando juntos?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '4',
                'puntos': 25,
                'alternativas': [
                    {'texto': '2 horas', 'es_correcta': False},
                    {'texto': '2.5 horas', 'es_correcta': False},
                    {'texto': '3 horas', 'es_correcta': False},
                    {'texto': '2.4 horas', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Probabilidad básica',
                'descripcion': 'Calcula probabilidades simples',
                'contenido': 'Al lanzar dos dados, ¿cuál es la probabilidad de que la suma sea 7?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Probabilidad',
                'respuesta_correcta': '2',
                'puntos': 20,
                'alternativas': [
                    {'texto': '1/6', 'es_correcta': False},
                    {'texto': '1/6', 'es_correcta': True},
                    {'texto': '1/12', 'es_correcta': False},
                    {'texto': '1/18', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Progresión aritmética',
                'descripcion': 'Encuentra términos en una progresión',
                'contenido': 'En la progresión 3, 7, 11, 15, ... ¿cuál es el término 10?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 20,
                'alternativas': [
                    {'texto': '35', 'es_correcta': False},
                    {'texto': '38', 'es_correcta': False},
                    {'texto': '39', 'es_correcta': True},
                    {'texto': '43', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Volumen del cilindro',
                'descripcion': 'Calcula el volumen de un cilindro',
                'contenido': 'Un cilindro tiene radio 4 cm y altura 10 cm. ¿Cuál es su volumen? (π=3.14)',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '4',
                'puntos': 25,
                'alternativas': [
                    {'texto': '125.6 cm³', 'es_correcta': False},
                    {'texto': '251.2 cm³', 'es_correcta': False},
                    {'texto': '376.8 cm³', 'es_correcta': False},
                    {'texto': '502.4 cm³', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Problema de relojes',
                'descripcion': 'Calcula ángulos entre manecillas',
                'contenido': '¿Qué ángulo forman las manecillas del reloj a las 3:15?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '1',
                'puntos': 25,
                'alternativas': [
                    {'texto': '7.5°', 'es_correcta': True},
                    {'texto': '15°', 'es_correcta': False},
                    {'texto': '30°', 'es_correcta': False},
                    {'texto': '45°', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Ecuación con valor absoluto',
                'descripcion': 'Resuelve ecuación con valor absoluto',
                'contenido': 'Resuelve: |2x - 4| = 10',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 25,
                'alternativas': [
                    {'texto': 'x=3', 'es_correcta': False},
                    {'texto': 'x=7', 'es_correcta': False},
                    {'texto': 'x=-3, x=7', 'es_correcta': True},
                    {'texto': 'x=3, x=-7', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Lógica de interruptores',
                'descripcion': 'Problema de lógica con interruptores',
                'contenido': 'Tienes 3 interruptores fuera de una habitación con una bombilla. Solo puedes entrar una vez. ¿Cómo sabes qué interruptor enciende la bombilla?',
                'dificultad': 'M',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '2',
                'puntos': 25,
                'alternativas': [
                    {'texto': 'Enciendo uno y entro inmediatamente', 'es_correcta': False},
                    {'texto': 'Enciendo uno, espero, lo apago, enciendo otro y entro', 'es_correcta': True},
                    {'texto': 'Enciendo los tres a la vez', 'es_correcta': False},
                    {'texto': 'Enciendo dos y entro', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Razones y proporciones',
                'descripcion': 'Resuelve problema de proporciones',
                'contenido': 'Si 5 libros cuestan $75, ¿cuánto cuestan 8 libros?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '4',
                'puntos': 20,
                'alternativas': [
                    {'texto': '$100', 'es_correcta': False},
                    {'texto': '$110', 'es_correcta': False},
                    {'texto': '$115', 'es_correcta': False},
                    {'texto': '$120', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Área superficial del cubo',
                'descripcion': 'Calcula el área superficial',
                'contenido': 'Un cubo tiene arista de 5 cm. ¿Cuál es su área superficial total?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '2',
                'puntos': 20,
                'alternativas': [
                    {'texto': '100 cm²', 'es_correcta': False},
                    {'texto': '150 cm²', 'es_correcta': True},
                    {'texto': '125 cm²', 'es_correcta': False},
                    {'texto': '175 cm²', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de velocidad',
                'descripcion': 'Calcula velocidades y distancias',
                'contenido': 'Un auto recorre 240 km en 3 horas. ¿Cuál es su velocidad promedio?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '1',
                'puntos': 20,
                'alternativas': [
                    {'texto': '80 km/h', 'es_correcta': True},
                    {'texto': '70 km/h', 'es_correcta': False},
                    {'texto': '90 km/h', 'es_correcta': False},
                    {'texto': '100 km/h', 'es_correcta': False},
                ]
            },
                        {
                'titulo': 'Factorización',
                'descripcion': 'Factoriza una expresión algebraica',
                'contenido': 'Factoriza: x² + 5x + 6',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 20,
                'alternativas': [
                    {'texto': '(x+1)(x+6)', 'es_correcta': False},
                    {'texto': '(x+2)(x+4)', 'es_correcta': False},
                    {'texto': '(x+2)(x+3)', 'es_correcta': True},
                    {'texto': '(x+1)(x+5)', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de intereses',
                'descripcion': 'Calcula interés simple',
                'contenido': '¿Cuánto interés genera un capital de $1000 al 5% anual en 3 años?',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '2',
                'puntos': 25,
                'alternativas': [
                    {'texto': '$125', 'es_correcta': False},
                    {'texto': '$150', 'es_correcta': True},
                    {'texto': '$175', 'es_correcta': False},
                    {'texto': '$200', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Lógica de pesos',
                'descripcion': 'Problema de comparación de pesos',
                'contenido': 'Tienes 9 bolas iguales, una más pesada. ¿Cuántas pesadas mínimas necesitas en una balanza?',
                'dificultad': 'M',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '1',
                'puntos': 25,
                'alternativas': [
                    {'texto': '2 pesadas', 'es_correcta': True},
                    {'texto': '3 pesadas', 'es_correcta': False},
                    {'texto': '4 pesadas', 'es_correcta': False},
                    {'texto': '5 pesadas', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Ecuación racional',
                'descripcion': 'Resuelve ecuación con fracciones algebraicas',
                'contenido': 'Resuelve: (x+3)/(x-2) = 2',
                'dificultad': 'M',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '4',
                'puntos': 25,
                'alternativas': [
                    {'texto': 'x=5', 'es_correcta': False},
                    {'texto': 'x=6', 'es_correcta': False},
                    {'texto': 'x=7', 'es_correcta': False},
                    {'texto': 'x=7', 'es_correcta': True},
                ]
            },
            
            {
                'titulo': 'Problema de relojes avanzado',
                'descripcion': 'Calcula tiempos de encuentro de manecillas',
                'contenido': '¿A qué hora después de las 3:00 se superponen por primera vez el horario y el minutero?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '3',
                'puntos': 35,
                'alternativas': [
                    {'texto': '3:15:00', 'es_correcta': False},
                    {'texto': '3:16:00', 'es_correcta': False},
                    {'texto': '3:16:21.8', 'es_correcta': True},
                    {'texto': '3:17:30', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Sistema de ecuaciones no lineales',
                'descripcion': 'Resuelve sistema complejo',
                'contenido': 'Resuelve: x² + y² = 25, x + y = 7',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '2',
                'puntos': 40,
                'alternativas': [
                    {'texto': 'x=3,y=4', 'es_correcta': False},
                    {'texto': 'x=3,y=4 y x=4,y=3', 'es_correcta': True},
                    {'texto': 'x=5,y=2', 'es_correcta': False},
                    {'texto': 'x=2,y=5', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de trabajo complejo',
                'descripcion': 'Trabajo con eficiencias variables',
                'contenido': 'A y B hacen un trabajo en 12 días. B y C en 15 días. A y C en 20 días. ¿Cuánto tardan los tres juntos?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '4',
                'puntos': 45,
                'alternativas': [
                    {'texto': '8 días', 'es_correcta': False},
                    {'texto': '9 días', 'es_correcta': False},
                    {'texto': '11 días', 'es_correcta': False},
                    {'texto': '10 días', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Lógica de caballeros y escuderos',
                'descripcion': 'Problema clásico de lógica avanzada',
                'contenido': 'En una isla, los caballeros siempre dicen verdad, escuderos siempre mienten. encuentras a dos personas. Uno dice: "Al menos uno de nosotros es escudero". ¿Qué son?',
                'dificultad': 'D',
                'tipo': 'L',
                'categoria': 'Lógica',
                'respuesta_correcta': '1',
                'puntos': 40,
                'alternativas': [
                    {'texto': 'El que habla es caballero, el otro escudero', 'es_correcta': True},
                    {'texto': 'Ambos caballeros', 'es_correcta': False},
                    {'texto': 'Ambos escuderos', 'es_correcta': False},
                    {'texto': 'El que habla es escudero, el otro caballero', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Ecuación exponencial',
                'descripcion': 'Resuelve ecuación con exponentes',
                'contenido': 'Resuelve: 2^(x+1) + 2^x = 24',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 35,
                'alternativas': [
                    {'texto': 'x=2', 'es_correcta': False},
                    {'texto': 'x=2.5', 'es_correcta': False},
                    {'texto': 'x=3', 'es_correcta': True},
                    {'texto': 'x=4', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Geometría analítica',
                'descripcion': 'Problema de rectas y distancias',
                'contenido': '¿Cuál es la distancia del punto (3,4) a la recta 3x + 4y - 10 = 0?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '2',
                'puntos': 40,
                'alternativas': [
                    {'texto': '2 unidades', 'es_correcta': False},
                    {'texto': '3 unidades', 'es_correcta': True},
                    {'texto': '4 unidades', 'es_correcta': False},
                    {'texto': '5 unidades', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Probabilidad condicional',
                'descripcion': 'Calcula probabilidad avanzada',
                'contenido': 'En una familia con 2 hijos, si al menos uno es niño, ¿cuál es la probabilidad de que ambos sean niños?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Probabilidad',
                'respuesta_correcta': '3',
                'puntos': 45,
                'alternativas': [
                    {'texto': '1/2', 'es_correcta': False},
                    {'texto': '1/3', 'es_correcta': True},
                    {'texto': '1/4', 'es_correcta': False},
                    {'texto': '2/3', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Progresión geométrica',
                'descripcion': 'Problema de progresiones complejas',
                'contenido': 'En una PG, el 3er término es 12 y el 6to término es 96. ¿Cuál es el primer término?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '1',
                'puntos': 35,
                'alternativas': [
                    {'texto': '3', 'es_correcta': True},
                    {'texto': '4', 'es_correcta': False},
                    {'texto': '6', 'es_correcta': False},
                    {'texto': '8', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Optimización geométrica',
                'descripcion': 'Maximiza área con perímetro fijo',
                'contenido': 'De todos los rectángulos con perímetro 40 cm, ¿cuál tiene área máxima?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Geometría',
                'respuesta_correcta': '4',
                'puntos': 40,
                'alternativas': [
                    {'texto': '8x12 cm', 'es_correcta': False},
                    {'texto': '5x15 cm', 'es_correcta': False},
                    {'texto': '9x11 cm', 'es_correcta': False},
                    {'texto': '10x10 cm', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Teorema de Bayes',
                'descripcion': 'Aplica teorema de Bayes',
                'contenido': 'En una fábrica, máquina A produce 60% con 2% defectuosos, B 40% con 3% defectuosos. Si un artículo es defectuoso, ¿probabilidad de que sea de A?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Probabilidad',
                'respuesta_correcta': '2',
                'puntos': 50,
                'alternativas': [
                    {'texto': '0.4', 'es_correcta': False},
                    {'texto': '0.5', 'es_correcta': True},
                    {'texto': '0.6', 'es_correcta': False},
                    {'texto': '0.7', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Ecuación logarítmica',
                'descripcion': 'Resuelve ecuación con logaritmos',
                'contenido': 'Resuelve: log₂(x) + log₂(x-2) = 3',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 35,
                'alternativas': [
                    {'texto': 'x=4', 'es_correcta': False},
                    {'texto': 'x=6', 'es_correcta': False},
                    {'texto': 'x=4', 'es_correcta': True},
                    {'texto': 'x=8', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Combinatoria avanzada',
                'descripcion': 'Problema de permutaciones y combinaciones',
                'contenido': '¿De cuántas formas pueden sentarse 5 personas en una mesa circular?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Probabilidad',
                'respuesta_correcta': '2',
                'puntos': 40,
                'alternativas': [
                    {'texto': '120', 'es_correcta': False},
                    {'texto': '24', 'es_correcta': True},
                    {'texto': '60', 'es_correcta': False},
                    {'texto': '30', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Límites algebraicos',
                'descripcion': 'Calcula límites de funciones',
                'contenido': 'Calcula: lim(x→2) (x²-4)/(x-2)',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 35,
                'alternativas': [
                    {'texto': '0', 'es_correcta': False},
                    {'texto': '1', 'es_correcta': False},
                    {'texto': '4', 'es_correcta': True},
                    {'texto': 'No existe', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Trigonometría avanzada',
                'descripcion': 'Problema de identidades trigonométricas',
                'contenido': 'Si senθ + cosθ = 1/√2, ¿cuánto vale senθcosθ?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Trigonometría',
                'respuesta_correcta': '4',
                'puntos': 45,
                'alternativas': [
                    {'texto': '1/4', 'es_correcta': False},
                    {'texto': '1/8', 'es_correcta': False},
                    {'texto': '-1/8', 'es_correcta': False},
                    {'texto': '-1/8', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Derivadas básicas',
                'descripcion': 'Calcula derivadas de funciones',
                'contenido': '¿Cuál es la derivada de f(x) = 3x⁴ - 2x² + 5x - 1?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '1',
                'puntos': 35,
                'alternativas': [
                    {'texto': '12x³ - 4x + 5', 'es_correcta': True},
                    {'texto': '12x³ - 2x + 5', 'es_correcta': False},
                    {'texto': '3x³ - 2x + 5', 'es_correcta': False},
                    {'texto': '12x³ - 4x', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Integral simple',
                'descripcion': 'Calcula integral indefinida',
                'contenido': '∫(3x² + 2x - 1)dx',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '2',
                'puntos': 40,
                'alternativas': [
                    {'texto': 'x³ + x² - x', 'es_correcta': False},
                    {'texto': 'x³ + x² - x + C', 'es_correcta': True},
                    {'texto': '3x³ + 2x² - x', 'es_correcta': False},
                    {'texto': '6x + 2 + C', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Problema de relojes múltiples',
                'descripcion': 'Sincronización de relojes',
                'contenido': 'Tres relojes se sincronizan a las 12:00. Uno se adelanta 2 min/hora, otro se atrasa 1 min/hora, el tercero es exacto. ¿Cuándo volverán a marcar la misma hora?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Aritmética',
                'respuesta_correcta': '4',
                'puntos': 50,
                'alternativas': [
                    {'texto': '10 días', 'es_correcta': False},
                    {'texto': '15 días', 'es_correcta': False},
                    {'texto': '20 días', 'es_correcta': False},
                    {'texto': '30 días', 'es_correcta': True},
                ]
            },
            {
                'titulo': 'Lógica de puertas',
                'descripcion': 'Problema de las tres puertas (Monty Hall)',
                'contenido': 'En el juego de las tres puertas (premio detrás de una), eliges una. Se abre una vacía de las otras dos. ¿Conviene cambiar?',
                'dificultad': 'D',
                'tipo': 'L',
                'categoria': 'Probabilidad',
                'respuesta_correcta': '1',
                'puntos': 45,
                'alternativas': [
                    {'texto': 'Sí, probabilidad 2/3', 'es_correcta': True},
                    {'texto': 'No, probabilidad 1/2', 'es_correcta': False},
                    {'texto': 'Da igual', 'es_correcta': False},
                    {'texto': 'Sí, probabilidad 3/4', 'es_correcta': False},
                ]
            },
            {
                'titulo': 'Análisis complejo',
                'descripcion': 'Problema de números complejos',
                'contenido': '¿Cuánto vale i⁵⁰, donde i es la unidad imaginaria?',
                'dificultad': 'D',
                'tipo': 'M',
                'categoria': 'Álgebra',
                'respuesta_correcta': '3',
                'puntos': 35,
                'alternativas': [
                    {'texto': 'i', 'es_correcta': False},
                    {'texto': '-i', 'es_correcta': False},
                    {'texto': '-1', 'es_correcta': True},
                    {'texto': '1', 'es_correcta': False},
                ]
            },
        ]
        
        for reto_data in retos_data:
            categoria_nombre = reto_data.pop('categoria')
            alternativas = reto_data.pop('alternativas')
            
            reto, created = Reto.objects.get_or_create(
                titulo=reto_data['titulo'],
                defaults={
                    'descripcion': reto_data['descripcion'],
                    'contenido': reto_data['contenido'],
                    'dificultad': reto_data['dificultad'],
                    'tipo': reto_data['tipo'],
                    'categoria': categorias[categoria_nombre],
                    'respuesta_correcta': reto_data['respuesta_correcta'],
                    'puntos': reto_data['puntos'],
                    'activo': True
                }
            )
            
            if created:
                self.stdout.write(f'Reto creado: {reto_data["titulo"]}')
                
                if alternativas and reto.tipo in ['M', 'L', 'P']:
                    for alt_data in alternativas:
                        Alternativa.objects.create(
                            reto=reto,
                            texto=alt_data['texto'],
                            es_correcta=alt_data['es_correcta']
                        )
                    self.stdout.write(f'  Alternativas creadas para: {reto_data["titulo"]}')
        
        if not User.objects.filter(username='usuario_ejemplo').exists():
            user = User.objects.create_user(
                username='usuario_ejemplo',
                password='password123',
                email='ejemplo@correo.com'
            )
            PerfilUsuario.objects.create(usuario=user)
            self.stdout.write('Usuario de ejemplo creado: usuario_ejemplo / password123')
        
        self.stdout.write(self.style.SUCCESS('¡Datos de ejemplo cargados exitosamente!'))